# Roadmap — Fase 1: Organização da Arquitetura

**Projeto:** Blog Entre Bugs e Soluções

## Objetivo

Preparar a arquitetura do projeto para crescer de forma organizada, reduzindo acoplamento, melhorando a separação de responsabilidades e criando uma base sólida para as próximas refatorações e funcionalidades.

---

# Feature 1.1 — Estruturar o app Blog em camadas

## Objetivo

Organizar o app `blog` em camadas de responsabilidade, facilitando manutenção, testes e evolução do projeto.

### Estrutura alvo

```text
blog/
├── services/
├── selectors/
├── repositories/
├── usecases/
├── validators/
└── utils/
```

### Status

* ✅ `utils/` criado
* ✅ `selectors.py` consolidado como camada de consultas
* 🔄 Demais camadas serão criadas conforme a necessidade (evitando diretórios vazios e abstrações prematuras)

### Entregas realizadas

* Extração do helper do YouTube para:

```text
blog/utils/youtube.py
```

* Consolidação da camada de consultas em `selectors.py`.

### Próximos passos

* Criar `services/` quando houver regras de negócio que justifiquem essa camada.
* Criar `repositories/` apenas se a complexidade de acesso aos dados aumentar.
* Criar `usecases/` quando existirem fluxos de negócio compostos.
* Criar `validators/` para validações reutilizáveis.

---

# Feature 1.2 — Padronizar imports

## Objetivo

Padronizar todos os imports do projeto para melhorar legibilidade e consistência.

### Tarefas

* Organizar imports conforme PEP 8.
* Aplicar `isort`.
* Aplicar `black`.
* Remover imports não utilizados.
* Revisar imports relativos desnecessários.

### Status

⬜ Não iniciado

---

# Feature 1.3 — Melhorar organização das configurações

## Objetivo

Modularizar as configurações do projeto para facilitar manutenção e escalabilidade.

### Estrutura atual

```text
config/settings/
├── base.py
├── dev.py
└── prod.py
```

### Estrutura alvo

```text
config/settings/
├── base.py
├── dev.py
├── prod.py
├── logging.py
├── cache.py
├── email.py
└── security.py
```

### Benefícios

* Melhor organização.
* Configurações isoladas por responsabilidade.
* Maior facilidade de manutenção.

### Status

⬜ Não iniciado

---

# Auditoria do Models

## Objetivo

Refatorar o domínio antes de evoluir o restante da aplicação.

### RF-001 — Extrair helper do YouTube

**Status:** ✅ Concluído

**Resultado:**

* Criado `blog/utils/youtube.py`.
* Removida a lógica de extração do `models.py`.
* Redução do acoplamento.

---

### RF-002 — Refatorar o método `save()`

**Status:** ✅ Concluído

**Resultado:**

O `save()` passou a atuar apenas como orquestrador.

Métodos extraídos:

* `_generate_slug()`
* `_generate_excerpt()`
* `_sync_publication()`
* `_normalize_youtube()`

---

### RF-003 — Avaliação da camada de Service

**Status:** ✅ Concluído

**Decisão arquitetural:**

Manter `publish()` e `unpublish()` no modelo neste momento.

**Motivo:**

* Regras de negócio ainda simples.
* Evitar abstração prematura (YAGNI).
* Manter alta coesão do domínio.

---

# Auditoria das Views

## Objetivo

Validar se as views possuem responsabilidades adequadas e identificar oportunidades de extração de lógica.

### Resultado

**Status:** ✅ Concluído

### Conclusões

* As CBVs possuem boa separação de responsabilidades.
* A lógica de acesso aos dados já está centralizada nos selectors.
* Não foi identificada necessidade de criação de Services.
* O uso de cache está adequado.
* As consultas estão organizadas e reutilizáveis.

**Nota da auditoria:** **9,4/10**

---

# Auditoria dos Selectors

## Objetivo

Padronizar e simplificar a camada de consultas da aplicação.

### RF-004 — Limpeza de imports

**Status:** ✅ Concluído

**Resultado:**

* Remoção de imports duplicados.
* Remoção de imports não utilizados.
* Organização conforme PEP 8.

---

### RF-005 — Padronização de tipagem

**Status:** ✅ Concluído

**Resultado:**

* Padronização das assinaturas dos selectors.
* Uso consistente de `QuerySet[Post]`.
* Melhoria na legibilidade das anotações de tipo.

---

### RF-006 — Reutilização de consultas

**Status:** ✅ Concluído

**Resultado:**

* `get_related_video_posts()` passou a reutilizar `get_published_posts()`.
* Eliminação de duplicação de regras de consulta.
* Centralização da lógica de posts publicados.

---

### RF-007 — Avaliação do filtro de vídeos

**Status:** ✅ Concluído

**Decisão arquitetural:**

Não adicionar filtros para `youtube_video_id=""`.

**Motivo:**

* O modelo já normaliza valores vazios para `None`.
* Evita duplicação de responsabilidade.
* Mantém os selectors simples e focados apenas nas consultas.

---

# Auditoria do Admin

## Objetivo

Revisar a configuração do Django Admin para melhorar organização, usabilidade e identificar oportunidades de otimização.

### Resultado

**Status:** ✅ Concluído

### Conclusões

* Estrutura do arquivo organizada e de fácil manutenção.
* Uso adequado de `@admin.register`.
* `fieldsets` bem definidos e separados por responsabilidade.
* `Inline`s configurados corretamente.
* `search_fields`, `list_filter` e `readonly_fields` apropriados.
* Mantida a ordenação por `created_at` em `PostAdmin` e `CTAAdmin`, priorizando os registros mais recentes.
* Avaliada a utilização de `list_select_related`, mas descartada por não trazer benefício prático no estado atual da aplicação (YAGNI).

**Nota da auditoria:** **9,6/10**

---

# Próxima etapa

## Feature 1.2 — Padronizar imports

### Objetivos

* Organizar imports conforme a PEP 8.
* Aplicar `isort`.
* Aplicar `black`.
* Remover imports não utilizados.
* Revisar imports relativos desnecessários.

### Status

🔄 Próxima atividade da Fase 1.
