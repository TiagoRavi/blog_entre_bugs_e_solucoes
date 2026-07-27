document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("contactForm");
    const status = document.getElementById("formStatus");
    const button = document.getElementById("submitBtn");

    form.addEventListener("submit", async (e) => {

        e.preventDefault();

        button.disabled = true;
        button.innerText = "Enviando...";

        status.className = "form-status loading show";
        status.innerText = "Enviando sua mensagem...";

        const dados = {
            nome: form.name.value.trim(),
            email: form.email.value.trim(),
            telefone: form.phone.value.trim(),
            assunto: form.subject.value.trim(),
            categoria: form.category.value,
            mensagem: form.message.value.trim()
        };

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

            console.log("Status:", response.status);

            if (!response.ok) {
                const erro = await response.text();
                console.error("Resposta:", erro);
                throw new Error(erro);
            }

            const json = await response.json();

            console.log("Resposta JSON:", json);

            status.className = "form-status success show";
            status.innerText = json.mensagem;

            form.reset();

        } catch (error) {

            console.error("Erro:", error);

            status.className = "form-status error show";
            status.innerText =
                "Não foi possível enviar sua mensagem. Tente novamente.";

        } finally {

            button.disabled = false;
            button.innerText = "Enviar mensagem";

        }

    });

});