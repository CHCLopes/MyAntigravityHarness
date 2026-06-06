---
name: spec-driven-executor
description: L0/L2 orchestrator that reads business (PRODUTO.md), technical (DESIGN.md), and visual (DESIGN_SYSTEM.md) specifications to validate consistency and generate structured atomic plans.
---

# spec-driven-executor

Esta skill é responsável por orquestrar o planejamento inicial de qualquer tarefa técnica no repositório, estabelecendo um contrato claro de entrega baseado em três fontes de verdade (`PRODUTO.md`, `DESIGN.md`, `DESIGN_SYSTEM.md`).

## Mapeamento de Gatilhos
- **Comandos**: `!spec-execute`, `!sde-run`, `!sde-exec`
- **Linguagem Natural**: "executar spec-driven-executor", "gerar plano spec-driven", "orquestrar planejamento do repositório", "validar especificações"

## Operações Suportadas

### 1. Carregamento e Leitura das Especificações
O executor deve ler os seguintes caminhos relativos ao projeto:
- `PRODUTO.md`
- `DESIGN.md`
- `DESIGN_SYSTEM.md`

Se algum arquivo estiver ausente, o executor deve reportar no início do relatório, mas prosseguir com as especificações que encontrar (ou pausar se a tarefa exigir explicitamente uma especificação ausente).

### 2. Validação de Conflitos Lógicos
Analise a consistência cruzada entre as especificações. Exemplos de conflitos a detectar:
- Tecnologia/stack especificada em `DESIGN.md` incompatível com os tokens/componentes definidos em `DESIGN_SYSTEM.md` (ex: DESIGN.md diz Python/FastAPI, mas DESIGN_SYSTEM.md detalha componentes React).
- Features listadas em `PRODUTO.md` que violam restrições técnicas em `DESIGN.md` ou limitações de design em `DESIGN_SYSTEM.md`.

### 3. Geração do Plano Estruturado
O executor gera obrigatoriamente um plano contendo exatamente as 8 seções especificadas em `GEMINI.md`:
1. **SPEC_REFERENCES**: Commit e versão de `PRODUTO.md`, `DESIGN.md` e `DESIGN_SYSTEM.md`.
2. **ACCEPTANCE_CRITERIA**: Checkboxes vazios contendo a cópia fiel dos critérios de aceitação de `PRODUTO.md`.
3. **DESIGN_COMPLIANCE**: Requisitos e padrões de `DESIGN.md` a serem observados.
4. **DESIGN_SYSTEM_COMPLIANCE**: Componentes UI e regras de estilo de `DESIGN_SYSTEM.md` a serem seguidos.
5. **CONFORMANCE_CHECKLIST**: Passos pré-escrita de código para garantir o setup correto.
6. **PLANO_ATÔMICO**: Passos técnicos sequenciais, isolados e com escopo atômico de alteração.
7. **VALIDAÇÃO_AUTOMÁTICA**: Roteiro exato de verificação de cada critério de aceitação.
8. **SUCCESS_SIGNATURE**: Resumo quantitativo (ex: "0 de N itens completos").
