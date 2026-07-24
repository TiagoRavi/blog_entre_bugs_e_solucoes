# Fase 3 — Views

## Objetivo

Manter as Views enxutas, focadas na camada HTTP e utilizando Selectors para acesso aos dados.

As Views devem ser responsáveis apenas por:

* receber a requisição;
* obter os dados por meio dos Selectors;
* montar o contexto;
* retornar a resposta.

Regras de negócio permanecem nos Models e consultas reutilizáveis nos Managers e Selectors.

---

# Feature 3.1 — Auditoria das Views

## Objetivo

Revisar todas as Views para garantir que estejam focadas apenas na camada HTTP.

### Itens revisados

* ✅ Responsabilidades das Views.
* ✅ Uso correto dos Selectors.
* ✅ Construção do contexto.
* ✅ Identificação de duplicações.
* ✅ Simplificação de consultas.
* ✅ Reutilização de `get_posts_by_category()`.
* ✅ Remoção de duplicação de consultas nas Views.
* ✅ Revisão do uso de `select_related()`.

### Decisões

* Manter as Views responsáveis apenas pela camada HTTP.
* Centralizar consultas reutilizáveis em `selectors.py`.
* Não mover regras simples para Services.
* Manter `get_object_or_404()` para recuperação de uma única categoria na View.
* Remover consultas duplicadas quando já existirem Selectors equivalentes.

### Status

✅ Concluído

---

# Feature 3.2 — Avaliação da camada de Services

## Objetivo

Identificar se alguma View passou a concentrar regras de negócio que justifiquem um Service.

### Critérios

Criar Services apenas quando houver:

* orquestração entre múltiplos Models;
* integrações externas;
* transações;
* regras reutilizadas por diferentes fluxos.

### Situação atual

Nenhuma View apresenta complexidade suficiente para justificar uma camada de Services.

As responsabilidades permanecem bem distribuídas entre Views, Selectors, Managers e Models.

### Decisão

Não criar Services apenas para reduzir o tamanho das Views.

### Status

🔄 Em avaliação contínua

---

# Feature 3.3 — Auditoria das CBVs

## Objetivo

Verificar se as Views utilizam corretamente as Generic Views do Django.

### Revisão realizada

* ✅ Uso adequado de `ListView`.
* ✅ Uso adequado de `DetailView`.
* ✅ Métodos sobrescritos apenas quando necessário.
* ✅ Responsabilidades compatíveis com as Generic Views.
* ✅ Nenhuma FBV identificada que justifique migração.
* ✅ Nenhuma CBV adicional (`TemplateView`, `RedirectView` ou `FormView`) necessária no momento.

### Decisões

* Manter `ListView` e `DetailView`.
* Continuar utilizando CBVs quando reduzirem código e aumentarem a legibilidade.
* Avaliar novas Generic Views apenas quando surgirem novos casos de uso.

### Status

✅ Concluído

---

# Situação da Fase 3

| Feature                               | Status                   |
| ------------------------------------- | ------------------------ |
| 3.1 – Auditoria das Views             | ✅ Concluído              |
| 3.2 – Avaliação da camada de Services | 🔄 Em avaliação contínua |
| 3.3 – Auditoria das CBVs              | ✅ Concluído              |

## Resultado

A camada de Views permanece simples, coesa e alinhada com a arquitetura do projeto:

* **Views** tratam apenas da camada HTTP.
* **Selectors** concentram as consultas da aplicação.
* **Managers** encapsulam consultas de domínio.
* **Models** concentram as regras de negócio.
* **Services** continuam sendo introduzidos apenas quando houver necessidade real.

Essa organização reduz acoplamento, facilita a manutenção e mantém a arquitetura consistente com as fases anteriores.
