---
PROJECT: [nome do projeto]
STACK: [lista separada por vírgula]
LAST_SESSION: [YYYY-MM-DD]
SESSION_COUNT: [número inteiro]

## DECISIONS_LOCKED
[imutável — apenas adição permitida]
- [decisão]: [justificativa em 1 linha]

## CONSTRAINTS
[imutável — apenas adição permitida]
- PROIBIDO: [o que não pode ser feito]
- SELADO: [arquivos intocáveis]
- REQUER_APROVAÇÃO: [o que precisa de gate]

## FILE_STATUS
[mutável — substituído a cada !sl-update]
| Arquivo | Status | Sessão |
|---|---|---|
| [caminho] | SEALED/IN_WORK/PENDING/DONE | [número] |

## SPEC_REFERENCES
- PRODUTO.md (commit: [hash], version: [versão])
- DESIGN.md (commit: [hash], version: [versão])
- DESIGN_SYSTEM.md (commit: [hash], version: [versão])

## SPEC_VALIDATION
- PRODUTO.md AC count: [número]
- DESIGN.md patterns count: [número]
- DESIGN_SYSTEM.md components count: [número]
- Conflicts with current impl: [lista ou "none"]

## COMPLETED
[append-only — máximo 10 itens, remover o mais antigo ao adicionar]
- [sessão N] [data] ✅ [o que foi entregue e aprovado]

## IN_PROGRESS
[mutável]
Tarefa: [descrição]
Progresso: [o que foi feito dentro da tarefa]
Bloqueio: [descrição ou NENHUM]

## NEXT_STEP
[mutável — única linha, primeira ação da próxima sessão]
[instrução atômica e executável]

## BLOCKERS
[mutável — vazio se nenhum]
- [bloqueio]: [o que está impedindo]
---
