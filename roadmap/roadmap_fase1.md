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

Padronizar o estilo do código e unificar a organização dos imports em todo o projeto.

### Entregas realizadas

* Configuração do **Black** via `pyproject.toml`.
* Configuração do **isort** utilizando o perfil do Black.
* Inclusão das ferramentas no ambiente do projeto.
* Padronização dos imports conforme a PEP 8.
* Formatação automática de todo o código-fonte.
* Remoção de inconsistências de estilo.

### Benefícios

* Código padronizado em todo o projeto.
* Maior legibilidade.
* Menor difusão de estilos entre desenvolvedores.
* Base preparada para futuras integrações com CI/CD e pre-commit.

### Status

✅ Concluído

---

# Feature 1.3 — Auditoria e simplificação das configurações

## Objetivo

Avaliar a organização das configurações do Django e identificar oportunidades reais de melhoria, evitando modularizações desnecessárias.

### Estrutura atual

```text
config/settings/
├── base.py
├── dev.py
└── prod.py
```

### Auditoria realizada

Foi realizada uma revisão completa do `base.py` com foco em:

* organização por responsabilidade;
* separação lógica das configurações;
* legibilidade;
* simplificação do código;
* aderência ao princípio YAGNI.

### Entregas realizadas

* Substituição de `os.getenv()` por `getenv()`.
* Criação da constante `MAX_UPLOAD_SIZE`.
* Melhoria na organização visual das seções.
* Isolamento da configuração do TinyMCE em um bloco próprio.
* Revisão geral da estrutura do arquivo.

### Decisões arquiteturais

Após a auditoria, concluiu-se que **não há necessidade de modularizar** o pacote `config/settings` neste momento.

As configurações atuais apresentam:

* boa organização;
* responsabilidades bem definidas;
* baixo acoplamento;
* tamanho adequado para um único `base.py`.

A criação de módulos como `logging.py`, `cache.py`, `email.py` e `security.py` foi descartada por não haver complexidade suficiente que justificasse essa divisão.

### Benefícios

* Configuração mais simples.
* Menor quantidade de arquivos para manutenção.
* Evolução guiada por necessidade real.
* Arquitetura alinhada ao princípio YAGNI.

### Status

✅ Concluído

---

# Auditoria do Models

## Objetivo

Refatorar o domínio antes de evoluir o restante da aplicação.

### RF-001 — Extrair helper do YouTube

**Status:** ✅ Concluído

### RF-002 — Refatorar o método `save()`

**Status:** ✅ Concluído

Métodos extraídos:

* `_generate_slug()`
* `_generate_excerpt()`
* `_sync_publication()`
* `_normalize_youtube()`

### RF-003 — Avaliação da camada de Service

**Status:** ✅ Concluído

**Decisão arquitetural:**

Manter `publish()` e `unpublish()` no modelo.

---

# Auditoria das Views

## Status

✅ Concluído

### Conclusões

* Boa separação de responsabilidades.
* Uso adequado de CBVs.
* Cache corretamente aplicado.
* Consultas delegadas aos selectors.
* Nenhuma necessidade de criação de Services.

**Nota:** **9,4/10**

---

# Auditoria dos Selectors

## RF-004 — Limpeza de imports

✅ Concluído

## RF-005 — Padronização de tipagem

✅ Concluído

## RF-006 — Reutilização de consultas

✅ Concluído

## RF-007 — Avaliação do filtro de vídeos

✅ Concluído

**Decisão:**

Não adicionar filtros redundantes para `youtube_video_id=""`, pois o modelo já garante a normalização.

---

# Auditoria do Admin

## Status

✅ Concluído

### Conclusões

* Estrutura organizada.
* Uso adequado de `ModelAdmin`.
* `fieldsets` bem definidos.
* `Inline`s corretamente configurados.
* Ordenação mantida por data de criação.
* `list_select_related` avaliado e descartado por YAGNI.

**Nota:** **9,6/10**

---

# Fase 1 — Status Geral

## Concluído

* ✅ Feature 1.1 — Estruturação da arquitetura
* ✅ Feature 1.2 — Padronização de imports e formatação
* ✅ Feature 1.3 — Auditoria e simplificação das configurações
* ✅ Auditoria dos Models
* ✅ Auditoria das Views
* ✅ Auditoria dos Selectors
* ✅ Auditoria do Admin

## Resultado

A Fase 1 estabeleceu uma base arquitetural sólida para o projeto, priorizando simplicidade, legibilidade e evolução incremental. As decisões seguiram os princípios de Clean Code e YAGNI, evitando abstrações prematuras e mantendo o código preparado para crescer conforme novas necessidades surgirem.

---

# Próxima etapa

## Fase 2 — Evolução Funcional

A próxima fase deverá concentrar-se na implementação de novas funcionalidades e melhorias orientadas pelas necessidades do domínio, utilizando a base arquitetural consolidada na Fase 1.
