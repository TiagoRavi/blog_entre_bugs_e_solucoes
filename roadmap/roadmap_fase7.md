Roadmap de Refatoração

Projeto: Blog Entre Bugs e Soluções

Status atual
Projeto funcional
Estrutura baseada em Django
Apps:
blog
pages
Fase 7 — SEO
Objetivo

Melhorar indexação, compartilhamento em redes sociais e qualidade técnica do site, utilizando prioritariamente recursos nativos do Django e seguindo boas práticas de SEO.

Feature 7.1
Auditoria de SEO

Auditar:

Meta tags
<title>
Meta description
Canonical
Robots
Sitemap
Open Graph
Twitter Cards
Estrutura de headings
URLs
Imagens (alt, dimensões)
Links internos

Critérios:

Identificar duplicações.
Identificar metadados ausentes.
Evitar otimizações prematuras.

Status:

⬜

Feature 7.2
Padronização das meta tags

Refatorações:

Centralizar meta tags no template base.
Padronizar blocos de SEO nos templates.
Implementar:
Title
Description
Canonical
Open Graph
Twitter Cards

Critérios:

Reutilização.
Responsabilidade única.
Sem necessidade de um SEOManager se o contexto dos templates e context processors atenderem ao projeto.

Status:

⬜

Feature 7.3
Dados estruturados (Schema.org)

Adicionar quando aplicável:

Article
BreadcrumbList
Organization
Person
FAQPage

Critérios:

Utilizar JSON-LD.
Gerar apenas schemas pertinentes à página.
Evitar dados estruturados desnecessários.

Status:

⬜

Feature 7.4
Sitemap e Robots

Revisar:

sitemap.xml
robots.txt
URLs canônicas
Indexação de páginas relevantes

Status:

⬜

Feature 7.5
Auditoria Lighthouse

Objetivos:

Performance ≥ 95
Accessibility ≥ 95
Best Practices ≥ 95
SEO = 100

Ações:

Identificar gargalos.
Corrigir problemas encontrados.
Reexecutar auditoria.

Status:

⬜

Por que remover o "SEO Manager"?

Pelo que vimos nas fases anteriores, o projeto evita criar camadas sem necessidade. Em Django, a maior parte das informações de SEO pode ser tratada de forma simples com:

herança de templates (base.html + blocos específicos);
context processors (quando houver dados globais, como nome do site);
métodos dos próprios modelos (por exemplo, para título ou descrição de um post);
tags do template, se surgir lógica de apresentação reutilizável.

Isso mantém a solução mais simples e alinhada ao princípio YAGNI.

Próximo passo

Assim como nas fases anteriores, eu começaria pela Feature 7.1 — Auditoria de SEO.

O primeiro passo seria analisar:

base.html;
templates das páginas (home, lista de posts, detalhe do post e about);
configuração de robots.txt e sitemap.xml (se existirem).

A partir dessa auditoria definimos as melhorias incrementais e os commits, sem introduzir abstrações desnecessárias.