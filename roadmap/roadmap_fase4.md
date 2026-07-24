# Fase 4 — Templates

## Objetivo

Manter os Templates organizados, reutilizáveis e focados exclusivamente na camada de apresentação.

---

# Feature 4.1 — Auditoria dos Templates

## Objetivo

Revisar todos os Templates para identificar oportunidades de simplificação, reutilização e padronização.

### Itens revisados

* ✅ Estrutura dos Templates.
* ✅ Uso de `extends`.
* ✅ Uso de `block`.
* ✅ Uso de `include`.
* ✅ Organização inicial dos diretórios.
* ✅ Identificação dos primeiros componentes reutilizáveis.
* ✅ Auditoria de `home.html`.
* ✅ Auditoria de `post_list.html`.
* ✅ Auditoria de `post_detail.html`.
* ✅ Auditoria de duplicações.
* ✅ Avaliação de lógica excessiva.

### Decisões

* Manter os Templates responsáveis apenas pela apresentação.
* Evitar lógica complexa nos Templates.
* Componentizar apenas trechos com reutilização comprovada.
* Não criar componentes para uso único.
* Manter os blocos de SEO e JSON-LD no próprio `post_detail.html`, pois pertencem exclusivamente a essa página.
* Manter componentes específicos de uma página em `includes/`.

### Resultado

A auditoria confirmou que os Templates já apresentam boa organização e baixo acoplamento.

### Status

✅ Concluído

---

# Feature 4.2 — Componentização

## Objetivo

Extrair trechos reutilizados em múltiplos Templates para componentes.

### Componentes

```text
components/
├── newsletter.html      ✅
└── post_card.html       ✅
```

### Componentes mantidos como `includes`

```text
includes/
├── post_author_box.html
├── post_content.html
├── post_cta_box.html
├── post_faq.html
├── post_featured_image.html
├── post_header.html
├── post_related.html
├── post_sidebar.html
├── post_toc.html
├── post_video.html
├── hero.html
├── pagination.html
└── post_grid.html
```

### Refatorações concluídas

* ✅ Extraído `post_card.html`.
* ✅ Simplificado `post_grid.html`.
* ✅ Corrigida a nomenclatura de `post_sidebar.html`.
* ✅ `newsletter.html` classificado como componente reutilizável.

### Decisões

* Componentes representam elementos reutilizáveis da interface.
* `includes` permanecem para estruturas específicas de uma página.
* Não criar componentes apenas por convenção.

### Status

🔄 Em andamento

---

# Feature 4.3 — Padronização dos Includes

## Objetivo

Padronizar o uso de `include` para melhorar organização e reutilização.

### Revisão

* ✅ Separação entre `includes/` e `components/`.
* ✅ `post_grid.html` atua apenas como estrutura da grade.
* ✅ Padronização da nomenclatura de `post_sidebar.html`.
* ✅ Auditoria dos principais `include`s.
* 🔄 Avaliar reorganização por contexto apenas se houver ganho real.

### Critérios

Cada `include` deve possuir responsabilidade única e representar uma estrutura específica da página.

### Status

🔄 Em andamento

---

# Situação da Fase 4

| Feature                         | Status          |
| ------------------------------- | --------------- |
| 4.1 – Auditoria dos Templates   | ✅ Concluído     |
| 4.2 – Componentização           | 🔄 Em andamento |
| 4.3 – Padronização dos Includes | 🔄 Em andamento |

## Progresso

### ✅ Concluído

* Auditoria completa dos principais Templates.
* Auditoria de `home.html`.
* Auditoria de `post_list.html`.
* Auditoria de `post_detail.html`.
* Extração de `post_card.html`.
* Simplificação de `post_grid.html`.
* Separação entre `includes/` e `components`.
* Padronização de `post_sidebar.html`.
* Identificação de `newsletter.html` como componente reutilizável.

### 🔜 Próximos passos

1. Concluir a migração de `newsletter.html` para `components/` (caso ainda não tenha sido realizada).
2. Revisar os demais Templates do projeto (`pages/` e eventuais templates administrativos personalizados).
3. Encerrar a Feature 4.2 quando não houver novas oportunidades reais de reutilização.
4. Encerrar a Feature 4.3 após validar que todos os `include`s seguem o padrão definido.
