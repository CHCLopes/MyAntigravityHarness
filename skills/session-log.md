---
name: session-log
description: L0 session persistence management using SESSION_LOG.md to prevent context loss and prompt fatigue.
---

# session-log

Esta skill é responsável pela governança de persistência de estado e contexto de desenvolvimento entre sessões utilizando o arquivo `SESSION_LOG.md`.

## Mapeamento de Aliases e Comandos Amigáveis

Esta skill é altamente flexível e reconhece tanto os comandos tradicionais baseados em código quanto comandos amigáveis e frases equivalentes de linguagem natural em português ou inglês:

| Comando Base | Aliases Amigáveis (Código) | Gatilhos em Linguagem Natural |
|---|---|---|
| `!sl-read` | `!sl-load`, `!sessao-ler`, `!carregar-sessao` | "ler sessão", "restaurar progresso", "carregar histórico", "carregar progresso", "ler session log" |
| `!sl-update` | `!sl-save`, `!sessao-salvar`, `!atualizar-sessao` | "salvar sessão", "salvar progresso", "atualizar sessão", "atualizar progresso", "atualizar estado" |
| `!sl-close` | `!sl-exit`, `!fechar-sessao`, `!encerrar-sessao` | "fechar sessão", "encerrar conversa", "salvar e fechar", "concluir sessão" |
| `!sl-lock` | `!sl-block`, `!sessao-travar`, `!decisao-bloquear` | "travar decisão", "bloquear arquivo", "adicionar restrição", "definir imutável" |

---

## Operações Suportadas

### 1. Operação `!sl-read` (Carregar/Ler Sessão)
*   **Trigger**: Usuário envia `!sl-read [caminho/SESSION_LOG.md]`, qualquer um de seus aliases (ex: `!sessao-ler`), ou frases correspondentes em linguagem natural (ex: "carregar histórico da sessão"), bem como no início de sessão ao identificar a presença física de um arquivo `SESSION_LOG.md`.
*   **Comportamento**:
    1. Leia o arquivo `SESSION_LOG.md` no caminho especificado (ou na raiz do projeto Sandbox/WorkSpace).
    2. Valide as seções obrigatórias.
    3. Confirme o estado emitindo **exclusivamente** a resposta estruturada abaixo:

```
SESSÃO RESTAURADA:
Projeto: [PROJECT]
Último estado: [último item de COMPLETED]
Em andamento: [IN_PROGRESS.Tarefa]
Próximo passo: [NEXT_STEP]
Arquivos selados: [lista de SEALED em FILE_STATUS]
Arquivos em trabalho: [lista de IN_WORK em FILE_STATUS]
Bloqueadores: [BLOCKERS ou NENHUM]
Aguardando instrução.
```

    4. **Regra estrita**: Não inicie nenhuma tarefa técnica de codificação, refatoração ou planejamento após exibir essa resposta. Aguarde por uma instrução explícita do usuário.

---

### 2. Operação `!sl-update` (Salvar/Atualizar Progresso)
*   **Trigger**: Usuário envia `!sl-update`, aliases correspondentes (ex: `!sessao-salvar`), ou frases em linguagem natural (ex: "salvar progresso da sessão", "atualizar estado").
*   **Comportamento**:
    1. Analise o trabalho realizado na sessão atual (arquivos modificados, progresso das tarefas, bloqueios identificados, próximas etapas e entregas).
    2. Gere as atualizações propostas para os campos mutáveis e apresente um diff estruturado para aprovação do usuário antes de realizar qualquer gravação física:

```
ATUALIZAÇÃO PROPOSTA:
FILE_STATUS: [mudanças em relação ao estado anterior]
IN_PROGRESS: [novo estado da tarefa e progresso]
NEXT_STEP: [nova primeira ação imediata da próxima sessão]
COMPLETED: [nova entrada no histórico de entregas se houver algo finalizado]
BLOCKERS: [nova lista de bloqueios ou NENHUM]

Aprovado? [s/n]
```

    3. **Regra de Escrita**: Somente após a resposta afirmativa explícita do usuário (`s` ou similar), efetue a escrita do arquivo `SESSION_LOG.md`.
    4. **Preservação de Imutabilidade**: Campos imutáveis (`DECISIONS_LOCKED`, `CONSTRAINTS`) **nunca** devem ser modificados ou sobrescritos pela operação `!sl-update`.

---

### 3. Operação `!sl-close` (Encerrar/Fechar Sessão)
*   **Trigger**: Usuário envia `!sl-close`, aliases equivalentes (ex: `!fechar-sessao`), ou frases em linguagem natural (ex: "encerrar conversa", "fechar sessão").
*   **Comportamento**:
    1. Execute a operação `!sl-update` internamente, gerando o diff e aguardando a aprovação explícita de gravação.
    2. Após o usuário aprovar e a escrita em disco ser concluída com sucesso, emita a resposta de fechamento e finalize a conversa:

```
SESSÃO ENCERRADA.
SESSION_LOG atualizado em: [caminho]
Para retomar: inicie nova conversa e envie:
!sl-read [caminho/SESSION_LOG.md]
NÃO reabra esta conversa.
```

    3. **Regra estrita de encerramento**: Não responda a nenhuma instrução técnica subsequente após emitir essa mensagem.

---

### 4. Operação `!sl-lock [conteúdo]` (Travar Decisões/Restrições)
*   **Trigger**: Usuário envia `!sl-lock [conteúdo]`, aliases (ex: `!decisao-bloquear [conteúdo]`), ou comandos em linguagem natural (ex: "travar decisão: [conteúdo]").
*   **Comportamento**:
    1. Identifique se o conteúdo trata-se de uma decisão estrutural (`DECISIONS_LOCKED`) ou restrição de escopo/limite (`CONSTRAINTS`).
    2. Adicione a nova entrada preservando integralmente todas as entradas preexistentes (operação append-only de segurança).
    3. Apresente o diff proposto e solicite aprovação do usuário antes de efetuar a gravação.

---

## Regras Globais e Restrições de Segurança
*   **Aprovação Mandatória**: Toda e qualquer alteração no `SESSION_LOG.md` requer a visualização do diff e aprovação afirmativa do usuário antes da escrita física no disco.
*   **Escopo de Escrita**: Para arquivos de projetos que estejam fora do Sandbox e residam no WorkSpace do usuário, é obrigatório solicitar autorização de caminho explícita.
*   **Inicialização Automática**: Se o usuário acionar o `!sl-read` e um arquivo `SESSION_LOG.md` não existir no diretório de destino do projeto, copie o template em `.antigravity/templates/_TEMPLATES/SESSION_LOG.md` para a raiz do projeto e solicite o preenchimento dos campos iniciais (`PROJECT`, `STACK`, etc.) antes de prosseguir com qualquer trabalho.
