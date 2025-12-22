# Entre Bugs e Soluções

Blog desenvolvido com **Django**, focado em conteúdo técnico sobre programação, bugs reais e soluções práticas.

Este README documenta **como rodar o projeto em desenvolvimento e em produção local**, antes do deploy.

---

## 📦 Requisitos

* Python 3.11+
* pip
* virtualenv (recomendado)

---

## 🧱 Setup inicial

Crie e ative o ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Rodar em desenvolvimento (DEV)

Usa configurações de desenvolvimento (`DEBUG=True`).

```bash
python manage.py runserver --settings=config.settings.dev
```

Acesse:

```
http://127.0.0.1:8000
```

---

## 🚀 Rodar em produção local (PROD)

Simula **exatamente** o ambiente de produção, sem fazer deploy.

### 1️⃣ Definir settings de produção

```bash
export DJANGO_SETTINGS_MODULE=config.settings.prod
```

### 2️⃣ Definir SECRET_KEY (obrigatório)

```bash
export SECRET_KEY="chave-secreta-temporaria"
```

> ⚠️ Em produção real essa variável vem do painel da plataforma (Render).

### 3️⃣ Coletar arquivos estáticos

```bash
python manage.py collectstatic
```

### 4️⃣ Rodar servidor

```bash
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000
```

---

## 🔄 Voltar para desenvolvimento

```bash
unset DJANGO_SETTINGS_MODULE
python manage.py runserver --settings=config.settings.dev
```

---

## 🛠 Comandos úteis

Criar superusuário:

```bash
python manage.py createsuperuser
```

Rodar migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

Rodar testes:

```bash
python manage.py test
```

---

## 📁 Estrutura de settings

```
config/settings/
├── base.py   # Configurações compartilhadas
├── dev.py    # Desenvolvimento
└── prod.py   # Produção
```

---

## ✅ Checklist antes do deploy

* [ ] Rodar projeto em PROD local
* [ ] `collectstatic` sem erros
* [ ] `DEBUG=False`
* [ ] `ALLOWED_HOSTS` configurado
* [ ] Busca funcionando
* [ ] Admin acessível

---

## 📌 Observações

* Este projeto usa **WhiteNoise** para servir arquivos estáticos
* Banco local padrão: **SQLite** (produção pode usar Postgres)
* Estrutura pronta para Render / Docker

---

Desenvolvido por **Tiago** 🚀
