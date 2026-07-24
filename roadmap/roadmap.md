# Roadmap de Refatoração

**Projeto:** Blog Entre Bugs e Soluções

## Status atual

* Projeto funcional
* Estrutura baseada em Django
* Apps:

  * `blog`
  * `pages`
* Boa separação inicial, porém existem responsabilidades misturadas.

---

# Fase 5 — CSS

## Objetivo

Escalabilidade.

---

## Feature 5.1

Migrar para arquitetura ITCSS ou CUBE CSS.

**Status:**

⬜

---

## Feature 5.2

Criar Design Tokens.

Arquivos:

```text
colors.css
spacing.css
typography.css
variables.css
```

**Status:**

⬜

---

# Fase 6 — JavaScript

## Objetivo

Modularização.

---

## Feature 6.1

Criar módulos.

```text
js/
├── components/
├── utils/
└── services/
```

**Status:**

⬜

---

## Feature 6.2

Remover scripts duplicados.

**Status:**

⬜

---

# Fase 7 — SEO

## Objetivo

Melhorar indexação.

---

## Feature 7.1

SEO Manager.

Responsável por:

* meta tags
* canonical
* Open Graph
* Twitter Cards

**Status:**

⬜

---

## Feature 7.2

Schema.org.

Adicionar:

* Article
* Breadcrumb
* FAQ
* Organization
* Person

**Status:**

⬜

---

## Feature 7.3

Auditoria Lighthouse.

Metas:

* Performance > 95
* SEO > 100
* Accessibility > 95

**Status:**

⬜

---

# Fase 8 — Performance

## Objetivo

Reduzir tempo de resposta.

---

## Feature 8.1

Cache de páginas.

**Status:**

⬜

---

## Feature 8.2

Cache de queries.

**Status:**

⬜

---

## Feature 8.3

Prefetch e Select Related.

**Status:**

⬜

---

# Fase 9 — Admin

## Objetivo

Melhor experiência para edição.

---

## Feature 9.1

Melhorar Admin.

* filtros
* busca
* ações
* previews

**Status:**

⬜

---

## Feature 9.2

Adicionar dashboards.

**Status:**

⬜

---

# Fase 10 — Testes

## Objetivo

Cobertura acima de 90%.

---

## Feature 10.1

Model Tests

⬜

---

## Feature 10.2

Selector Tests

⬜

---

## Feature 10.3

Service Tests

⬜

---

## Feature 10.4

Views Tests

⬜

---

## Feature 10.5

Integration Tests

⬜

---

# Fase 11 — Segurança

## Objetivo

Preparar para produção.

---

## Feature 11.1

Headers HTTP.

**Status:**

⬜

---

## Feature 11.2

Rate Limit.

**Status:**

⬜

---

## Feature 11.3

Proteção Anti Spam.

**Status:**

⬜

---

# Fase 12 — DevOps

## Objetivo

Automação.

---

## Feature 12.1

Pre-commit.

Ferramentas:

* black
* isort
* flake8
* ruff

**Status:**

⬜

---

## Feature 12.2

GitHub Actions.

Pipelines:

* testes
* lint
* deploy

**Status:**

⬜

---

# Fase 13 — Documentação

## Objetivo

Projeto profissional.

---

## Feature 13.1

Architecture.md

**Status:**

⬜

---

## Feature 13.2

Contributing.md

**Status:**

⬜

---

## Feature 13.3

API.md

**Status:**

⬜

---

# Fase 14 — Novas Funcionalidades

> Somente após toda a refatoração.

Possíveis features:

* ⬜ Newsletter
* ⬜ Comentários
* ⬜ Busca Full Text
* ⬜ API REST
* ⬜ RSS
* ⬜ Sitemap avançado
* ⬜ Dark Mode
* ⬜ Sistema de Tags
* ⬜ Série de Posts
* ⬜ Leitura estimada
* ⬜ Posts relacionados inteligentes
* ⬜ Analytics próprio
* ⬜ Dashboard SEO
* ⬜ Histórico de versões
* ⬜ Editor IA
* ⬜ Painel de métricas

---

# Critério de conclusão

Antes de iniciar qualquer nova feature:

* ✔ Cobertura de testes
* ✔ Lint
* ✔ Documentação
* ✔ Sem código duplicado
* ✔ Sem lógica nas views
* ✔ Sem regras nos templates
* ✔ Sem consultas N+1
* ✔ Arquitetura consistente
