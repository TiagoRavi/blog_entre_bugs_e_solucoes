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
* ✅ Auditoria de `post_detail.html`.
* 🔄 Auditoria de duplicações em andamento.
* 🔄 Avaliação de lógica excessiva em andamento.

### Decisões

* Manter os Templates responsáveis apenas pela apresentação.
* Evitar lógica complexa nos Templates.
* Componentizar apenas trechos com reutilização comprovada.
* Não criar componentes para uso único.
* Manter os blocos de SEO e JSON-LD no próprio `post_detail.html`, pois pertencem exclusivamente a essa página.

### Status

🔄 Em andamento

---

# Feature 4.2 — Componentização

## Objetivo

Extrair trechos reutilizados em múltiplos Templates para componentes.

### Componentes

```text
components/
├── post_card.html        ✅
├── author_box.html       ⬜
├── badge.html            ⬜
├── newsletter.html       ⬜
├── share_buttons.html    ⬜
└── toc.html              ⬜
```

### Refatorações concluídas

* ✅ Extraído `post_card.html`.
* ✅ Simplificado `includes/post_grid.html`, delegando a renderização de cada post ao componente.
* ✅ Corrigida a nomenclatura de `post_sidebar.html`.

### Critérios

* Criar componentes apenas quando houver reutilização ou ganho claro de manutenção.
* Evitar componentes utilizados apenas uma vez.
* Manter responsabilidade única para cada componente.

### Status

🔄 Em andamento

---

# Feature 4.3 — Padronização dos Includes

## Objetivo

Padronizar o uso de `include` para melhorar organização e reutilização.

### Revisão

* ✅ Separação inicial entre `includes/` e `components/`.
* ✅ `post_grid.html` simplificado para atuar apenas como estrutura da grade.
* ✅ Padronização da nomenclatura para `post_sidebar.html`.
* 🔄 Revisar os demais `include`s do projeto.
* 🔄 Validar a organização da pasta `components`.
* 🔄 Avaliar futura organização por contexto (ex.: `post/`), apenas se houver ganho real.

### Critérios

Cada componente deve possuir responsabilidade única e ser reutilizável.

### Status

🔄 Em andamento

---

# Situação da Fase 4

| Feature                         | Status          |
| ------------------------------- | --------------- |
| 4.1 – Auditoria dos Templates   | 🔄 Em andamento |
| 4.2 – Componentização           | 🔄 Em andamento |
| 4.3 – Padronização dos Includes | 🔄 Em andamento |

## Progresso

### ✅ Concluído

* Estrutura inicial dos Templates auditada.
* Auditoria de `home.html`.
* Auditoria de `post_detail.html`.
* Componente `post_card.html` extraído.
* `post_grid.html` simplificado.
* Separação inicial entre `includes/` e `components/`.
* Padronização da nomenclatura de `post_sidebar.html`.

### 🔜 Próximos passos

1. Auditar `post_list.html`.
2. Verificar reutilização de `post_grid.html` e `pagination.html`.
3. Identificar novos componentes realmente reutilizáveis.
4. Revisar os demais `include`s para manter um padrão consistente.
5. Encerrar a auditoria dos Templates e decidir se novas extrações são realmente necessárias.
