# Fase 5 — CSS

## Objetivo

Melhorar a organização, escalabilidade e manutenção do CSS por meio de pequenas refatorações incrementais, mantendo uma arquitetura simples e alinhada aos princípios de responsabilidade única.

---

## Feature 5.1

### Auditoria e organização da estrutura CSS

Refatorações:

- Auditoria da estrutura atual.
- Remoção de arquivos legados.
- Verificação de responsabilidades.
- Separação de estilos específicos de páginas.
- Eliminação de código morto e duplicações.

Concluído:

- ✅ `style.css` auditado (mantido como entrypoint).
- ✅ `site.css` removido.
- ✅ `base.css` auditado.
- ✅ `layout.css` auditado.
- ✅ Estilos da página Sobre movidos para `about.css`.

**Status:**

✅ Concluído

---

## Feature 5.2

### Definir arquitetura CSS

Arquitetura adotada:

```
static/css/
├── tokens/
├── base.css
├── layout.css
├── components.css
├── blog.css
├── hero.css
├── newsletter.css
├── cookies.css
├── about.css
└── style.css
```

Decisões:

- `style.css` mantido como entrypoint.
- Organização por responsabilidade.
- Sem adoção de ITCSS ou CUBE CSS para evitar complexidade desnecessária.
- Arquitetura simples baseada em responsabilidade única.

Critérios atendidos:

- ✅ Simplicidade
- ✅ Escalabilidade
- ✅ Baixo acoplamento
- ✅ Responsabilidade única

**Status:**

✅ Concluído

---

## Feature 5.3

### Criar Design Tokens

Estrutura prevista:

```text
static/css/
└── tokens/
    ├── colors.css
    ├── spacing.css
    ├── typography.css
    └── variables.css
```

Objetivos:

- Centralizar cores
- Centralizar tipografia
- Centralizar espaçamentos
- Facilitar manutenção
- Reduzir valores duplicados

**Status:**

⬜ Pendente

---

## Feature 5.4

### Padronizar componentes CSS

Refatorações realizadas:

- Separação de componentes reutilizáveis.
- Extração do layout do Blog para `blog.css`.
- Extração da navegação para `layout.css`.
- Extração do banner de cookies para `cookies.css`.
- Organização do `components.css` contendo apenas componentes reutilizáveis.

Componentes padronizados:

- ✅ Post Card
- ✅ Sidebar CTA
- ✅ Post CTA
- ✅ Video Placeholder

Pendências:

- ⬜ Botões globais
- ⬜ Newsletter
- ⬜ Paginação
- ⬜ Hero
- ⬜ Footer
- ⬜ Header

**Status:**

🟡 Em andamento

---

## Feature 5.5

### Limpeza e otimização

Revisar todo o CSS para:

- Remover regras não utilizadas
- Eliminar seletores duplicados
- Revisar media queries
- Reduzir especificidade
- Melhorar legibilidade

**Status:**

⬜ Pendente