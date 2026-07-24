Fase 5 — CSS
Objetivo

Melhorar a organização, escalabilidade e manutenção do CSS por meio de pequenas refatorações incrementais, mantendo uma arquitetura simples e alinhada aos princípios de responsabilidade única.

Feature 5.1
Auditoria e organização da estrutura CSS

Refatorações:

Auditoria completa da estrutura CSS.
Remoção de arquivos legados.
Verificação de responsabilidades.
Separação de estilos específicos por domínio/página.
Eliminação de pequenas duplicações.
Revisão de todos os arquivos CSS.

Concluído:

✅ style.css auditado (mantido como entrypoint)
✅ site.css removido
✅ base.css auditado
✅ layout.css auditado
✅ components.css auditado
✅ blog.css auditado
✅ hero.css auditado
✅ newsletter.css auditado
✅ cookies.css auditado
✅ about.css auditado

Status:

✅ Concluído

Feature 5.2
Definir arquitetura CSS

Arquitetura adotada:

static/css/
├── tokens/
│   ├── colors.css
│   ├── spacing.css
│   ├── typography.css
│   └── variables.css
├── base.css
├── layout.css
├── components.css
├── blog.css
├── hero.css
├── newsletter.css
├── cookies.css
├── about.css
└── style.css

Decisões:

style.css mantido como entrypoint.
Organização por responsabilidade.
Componentes reutilizáveis centralizados em components.css.
Estilos específicos separados por domínio/página.
Sem adoção de ITCSS, SMACSS ou CUBE CSS (YAGNI).
Arquitetura simples baseada em responsabilidade única.

Critérios atendidos:

✅ Simplicidade
✅ Escalabilidade
✅ Baixo acoplamento
✅ Responsabilidade única

Status:

✅ Concluído

Feature 5.3
Criar Design Tokens

Estrutura criada:

static/css/tokens/
├── colors.css
├── spacing.css
├── typography.css
└── variables.css

Objetivos alcançados:

✅ Centralização de cores
✅ Centralização de tipografia
✅ Centralização de espaçamentos
✅ Centralização de border-radius
✅ Centralização de box-shadow
✅ Centralização de transitions

Status:

✅ Concluído

Feature 5.4
Padronizar componentes CSS

Refatorações realizadas:

Organização dos componentes reutilizáveis.
Extração do layout do Blog para blog.css.
Extração da navegação para layout.css.
Extração do Hero para hero.css.
Extração da Newsletter para newsletter.css.
Extração do banner de cookies para cookies.css.
Extração da página Sobre para about.css.
Organização do components.css.

Componentes padronizados:

✅ Post Card
✅ Sidebar CTA
✅ Post CTA
✅ Video Placeholder
✅ Hero
✅ Newsletter
✅ Cookie Banner
✅ Página About

Pendências:

⬜ Botões globais
⬜ Paginação
⬜ Header
⬜ Footer

Status:

🟡 Em andamento

Observação: Header e Footer permanecem em layout.css por fazerem parte da estrutura global do site, não sendo necessário separá-los neste momento.

Feature 5.5
Limpeza e otimização

Refatorações concluídas:

✅ Auditoria completa de todos os arquivos CSS
✅ Remoção de pequenas duplicações
✅ Simplificação de seletores
✅ Padronização de cores com Design Tokens
✅ Padronização de border-radius
✅ Padronização de box-shadow
✅ Padronização de transitions
✅ Padronização de font-weight
✅ Padronização de font-family (quando aplicável)
✅ Padronização de espaçamentos recorrentes com tokens
✅ Aplicação consistente de Design Tokens em todos os módulos

Pendências:

⬜ Remover possíveis estilos não utilizados (após auditoria do projeto completo)
⬜ Revisão final de media queries
⬜ Revisão de especificidade dos seletores
⬜ Revisão geral de consistência visual

Status:

🟡 Em andamento

Situação da Fase 5
Feature	Status
5.1 Auditoria da estrutura	✅
5.2 Arquitetura CSS	✅
5.3 Design Tokens	✅
5.4 Padronização dos componentes	🟡
5.5 Limpeza e otimização	🟡

A Fase 5 está praticamente concluída. O que resta é uma revisão transversal do projeto (identificar CSS não utilizado, revisar media queries e especificidade) e decidir, se fizer sentido, a criação de componentes globais para elementos como botões e paginação. Essas tarefas podem ser tratadas como pequenos commits independentes, mantendo a estratégia incremental adotada até aqui.