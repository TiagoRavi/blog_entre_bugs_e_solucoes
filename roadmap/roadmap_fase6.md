Roadmap de Refatoração

Projeto: Blog Entre Bugs e Soluções

Status atual
Projeto funcional
Estrutura baseada em Django
Apps:
blog
pages
JavaScript modular por arquivo e com boa separação de responsabilidades.
Fase 6 — JavaScript
Objetivo

Melhorar a organização, manutenção e reutilização dos scripts por meio de pequenas refatorações incrementais, mantendo uma arquitetura simples e alinhada aos princípios de responsabilidade única.

Feature 6.1
Auditoria da estrutura JavaScript

Refatorações realizadas:

Auditoria de todos os arquivos JavaScript.
Verificação de responsabilidades.
Identificação de código duplicado.
Verificação de oportunidades de modularização.
Revisão de consistência entre componentes.

Arquivos auditados:

✅ cookies.js
✅ menu-submenu.js
✅ search.js
✅ share-fab.js
✅ post-toc.js

Refatorações realizadas:

✅ Remoção de menu.js (duplicado)
✅ Unificação da lógica de navegação
✅ Identificação de pequenas melhorias de legibilidade
✅ Confirmação de responsabilidade única nos módulos

Conclusões:

Não há necessidade de criar services/.
utils/ somente será criado quando existir código compartilhado.
A estrutura atual é suficiente para o tamanho do projeto.

Status:

✅ Concluído

Feature 6.2
Limpeza e padronização dos scripts

Refatorações:

Remover código de depuração (console.log).
Padronizar uso de arrow functions.
Padronizar nomes de variáveis.
Aplicar guard clauses quando apropriado.
Extrair pequenas funções privadas para melhorar legibilidade.
Remover estilos inline em favor do CSS quando aplicável.

Pendências:

⬜ Ajustes em cookies.js
⬜ Ajustes em search.js
⬜ Ajustes em share-fab.js
⬜ Ajustes em post-toc.js

Status:

🟡 Em andamento

Feature 6.3
Modularização

Objetivos:

Manter um arquivo por componente.
Extrair utilitários apenas quando houver reutilização.
Evitar abstrações prematuras.

Estrutura atual:

static/js/
├── cookies.js
├── menu-submenu.js
├── post-toc.js
├── search.js
└── share-fab.js

Estrutura futura (se necessária):

static/js/
├── cookies.js
├── menu-submenu.js
├── post-toc.js
├── search.js
├── share-fab.js
└── utils/

utils/ será criado apenas se surgir código compartilhado.

Status:

⬜

Situação da Fase 6
Feature	Status
6.1 Auditoria da estrutura	✅
6.2 Limpeza e padronização	🟡
6.3 Modularização	⬜
Próximos passos

A próxima etapa natural é concluir a Feature 6.2, aplicando as pequenas melhorias identificadas durante a auditoria (remoção de logs, padronização de callbacks, extração de funções auxiliares e eliminação de estilos inline). Somente após essa limpeza vale reavaliar se existe código compartilhado suficiente para justificar a criação de um diretório utils/. Até o momento, a resposta é não.