---
name: specification-validator
description: L1 quality gate that performs ternary validation of implementation compliance against business (PRODUTO.md), technical (DESIGN.md), and visual (DESIGN_SYSTEM.md) requirements.
---

# specification-validator

Esta skill atua como um gate automático de qualidade transversal, avaliando se as modificações implementadas estão em total conformidade com as especificações.

## Mapeamento de Gatilhos
- **Comandos**: `!spec-validate`, `!sv-run`, `!sv-check`
- **Linguagem Natural**: "validar entrega com specification-validator", "rodar gate de conformidade", "validação ternária", "checar especificações"

## Operações Suportadas

### 1. Extração de Requisitos das Specs
- Lê `PRODUTO.md` e extrai todos os critérios de aceitação (AC).
- Lê `DESIGN.md` e extrai todas as restrições arquiteturais e padrões de código exigidos.
- Lê `DESIGN_SYSTEM.md` e extrai todos os componentes de UI e tokens visuais definidos.

### 2. Comparação vs. Relatório de Implementação
- Faz o parse do relatório de implementação fornecido pelo agente.
- Mapeia as claims do relatório contra cada requisito extraído das especificações.

### 3. Emissão de Score Ternário
Gera um relatório binário quantitativo dividido em três dimensões:
- **AC Compliance**: N de M critérios de aceitação cumpridos.
- **Design Compliance**: X de Y padrões arquiteturais respeitados.
- **UI Compliance**: A de B componentes/tokens visuais implementados corretamente.

A saída de verificação deve seguir estritamente o formato binário consolidado (ex: "AC Compliance: 3/3, Design: 2/2, UI: 4/4. Overall: 9/9 items passed").
Se qualquer item falhar, o status final é bloqueado e a entrega é pausada com recomendações específicas de ajuste para o item faltante.
