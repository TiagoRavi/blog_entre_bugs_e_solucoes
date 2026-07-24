# Roadmap de Refatoração

**Projeto:** Blog Entre Bugs e Soluções

## Status atual

- Projeto funcional.
- Arquitetura organizada após a Fase 1.
- Camada de consultas consolidada em `selectors.py`.
- Base preparada para evoluções incrementais.

---

# Fase 2 — Evolução do Domínio

## Objetivo

Fortalecer o domínio da aplicação, mantendo os Models coesos e evoluindo a arquitetura apenas quando houver necessidade real.

---

# Feature 2.1 — Auditoria dos Models

## Objetivo

Revisar cada Model para identificar oportunidades de simplificação e melhoria.

### Itens revisados

- ✅ Responsabilidades dos Models.
- ✅ Regras de negócio.
- ✅ Coesão.
- ✅ Métodos públicos.
- ✅ Métodos privados.
- ✅ Consultas pertencentes ao domínio.
- ✅ Organização do `save()` como orquestrador.
- ✅ Extração do helper do YouTube para `utils`.
- ✅ Remoção do índice redundante de `slug`.
- ✅ Padronização de tipagem dos métodos.
- ✅ Revisão dos índices existentes.

### Decisões

- Manter `publish()` e `unpublish()` no Model.
- Não criar camada de Services.
- Não criar Repository.
- Não dividir `models.py`.
- Manter `PostQuerySet` como Manager do domínio.

### Status

✅ Concluído

---

# Feature 2.2 — Avaliação da camada de Services

## Objetivo

Identificar regras de negócio que justifiquem a criação de Services.

### Critérios

Criar Services apenas quando houver:

- orquestração entre múltiplos Models;
- integração com APIs externas;
- transações complexas;
- regras reutilizadas por diferentes pontos da aplicação.

### Situação atual

Nenhuma regra identificada que justifique a criação de Services.

A lógica existente permanece naturalmente encapsulada nos Models.

### Status

🔄 Em avaliação contínua

---

# Feature 2.3 — Avaliação dos Managers

## Objetivo

Revisar se existem consultas de domínio que pertencem naturalmente aos Managers.

### Revisão realizada

- ✅ Auditoria do `PostQuerySet`.
- ✅ Validação da separação entre Managers e Selectors.
- ✅ Confirmação de que `published()` pertence ao domínio do `Post`.
- ✅ Reutilização de `Post.objects.published()` pelos Selectors.
- ✅ Nenhuma duplicação identificada.
- ✅ Nenhuma consulta dos Selectors deve migrar para o Manager.
- ✅ Nenhum novo Manager se justifica neste momento.

### Decisões

- Managers permanecem responsáveis por consultas reutilizáveis do domínio.
- Selectors continuam concentrando consultas específicas da aplicação.
- Novos métodos como `with_video()` ou `featured()` serão criados apenas quando houver necessidade real.

### Status

✅ Concluído

---

# Feature 2.4 — Auditoria de índices do banco

## Objetivo

Verificar se os índices atuais atendem aos padrões de consulta da aplicação.

### Revisado

- ✅ Índice redundante de `slug` removido.
- ✅ Confirmado índice automático da `ForeignKey` (`category`).
- ✅ Mantido índice composto (`status`, `published_at`).

### Situação atual

Os índices existentes atendem às consultas atuais da aplicação.

Novos índices serão adicionados apenas se surgirem consultas que justifiquem sua criação.

### Status

✅ Concluído

---

# Situação da Fase 2

| Feature | Status |
|---------|--------|
| 2.1 – Auditoria dos Models | ✅ Concluído |
| 2.2 – Avaliação da camada de Services | 🔄 Em avaliação contínua |
| 2.3 – Avaliação dos Managers | ✅ Concluído |
| 2.4 – Auditoria de índices | ✅ Concluído |

## Resultado

A arquitetura atual permanece simples, coesa e preparada para evoluir conforme novas necessidades surgirem, evitando abstrações prematuras e mantendo uma clara separação entre domínio, consultas reutilizáveis e casos de uso da aplicação.