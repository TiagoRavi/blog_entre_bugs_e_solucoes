
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("contactForm");
    const status = document.getElementById("formStatus");
    const button = document.getElementById("submitBtn");

    // Evita erros caso o script seja carregado em outra página.
    if (!form || !status || !button) {
        return;
    }

    const getField = (name) => form.elements.namedItem(name);

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        // Verificação adicional antes de enviar os dados.
        if (!form.reportValidity()) {
            return;
        }

        const name = getField("name");
        const email = getField("email");
        const phone = getField("phone");
        const subject = getField("subject");
        const category = getField("category");
        const message = getField("message");

        if (!name || !email || !phone || !subject || !category || !message) {
            status.className = "form-status error show";
            status.innerText =
                "Não foi possível identificar todos os campos do formulário.";
            return;
        }

        const dados = {
            nome: name.value.trim(),
            email: email.value.trim(),
            telefone: phone.value.trim(),
            assunto: subject.value.trim(),
            categoria: category.value,
            mensagem: message.value.trim()
        };

        // Impede o envio de campos obrigatórios vazios após remover espaços.
        if (
            !dados.nome ||
            !dados.email ||
            !dados.assunto ||
            !dados.categoria ||
            !dados.mensagem
        ) {
            status.className = "form-status error show";
            status.innerText =
                "Preencha todos os campos obrigatórios antes de enviar.";
            return;
        }

        button.disabled = true;
        button.innerText = "Enviando...";
        status.className = "form-status loading show";
        status.innerText = "Enviando sua mensagem...";

        try {
            const response = await fetch(
                "https://automacao.entrebugsesolucoes.com.br/webhook/contato",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(dados)
                }
            );

            if (!response.ok) {
                throw new Error(`Erro HTTP ${response.status}`);
            }

            const texto = await response.text();
            let mensagemSucesso = "Mensagem enviada com sucesso!";

            if (texto.trim()) {
                try {
                    const json = JSON.parse(texto);

                    if (
                        typeof json.mensagem === "string" &&
                        json.mensagem.trim()
                    ) {
                        mensagemSucesso = json.mensagem;
                    }
                } catch {
                    // Respostas não JSON são aceitas se o HTTP indicar sucesso.
                }
            }

            status.className = "form-status success show";
            status.innerText = mensagemSucesso;
            form.reset();

        } catch (error) {
            console.error("Erro ao enviar formulário:", error);

            status.className = "form-status error show";
            status.innerText =
                "Não foi possível enviar sua mensagem. Tente novamente.";

        } finally {
            button.disabled = false;
            button.innerText = "Enviar mensagem";
        }
    });
});
