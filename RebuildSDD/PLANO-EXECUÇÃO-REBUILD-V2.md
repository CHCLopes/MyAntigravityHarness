# PLANO — Execução Rebuild SDD v2.0 (COM DESIGN_SYSTEM)

**Data de Planejamento**: 2026-06-06  
**Executor**: Antigravity (Gemini 3.5 Flash)  
**Revisor**: Você  
**Status**: Aguardando aprovação de arquitetura + plano

---

## BLOCO ESTRUTURADO DE RECUPERAÇÃO DA SESSÃO

```
PROJECT: Rebuild Antigravity para SDD v2.0 (com DESIGN_SYSTEM)

CONTEXT:
  - 363 skills em 5 camadas (L0-L4)
  - GEMINI.md atual governa, funciona
  - SESSION_LOG atual estrutura recuperação
  - Necessidade: Adicionar 3 specs versionadas no repo (PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md)

DECISIONS_LOCKED:
  - Rebuild completo (não incremental)
  - PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md como 3 fontes de verdade
  - spec-driven-executor como orquestradora (lê 3 arquivos)
  - specification-validator como gate automático (valida contra 3 specs)

CONSTRAINTS:
  - Simplicidade Cirúrgica: Nenhum boilerplate novo
  - Compatibilidade: Skills L3-L4 (execução/entrega) sem mudança
  - Versionamento: Tudo em branch novo rebuild-sdd-v2.0
```

---

## PREMISSAS TÉCNICAS ADOTADAS

1. **GEMINI.md é template base** → Adicionar seção SPEC-DRIVEN VALIDATION (com 3 refs), não reescrever
2. **SESSION_LOG estrutura se mantém** → 2 seções novas (SPEC_REFERENCES, SPEC_VALIDATION) mencionam 3 arquivos
3. **10 skills recebem adaptações** → Novos modos/flags (mencionam 3 specs onde relevante)
4. **2 skills novas** → spec-driven-executor (L0/L2 orquestra, lê 3 specs) + specification-validator (L1 gate, valida 3 specs)
5. **3 templates novos** → PRODUTO.md.template, DESIGN.md.template, DESIGN_SYSTEM.md.template
6. **Teste de conformidade** → Agente Storyteller V5 é caso de teste (tem PRODUTO.md, tem DESIGN.md, tem DESIGN_SYSTEM.md?)
7. **Versionamento de specs** → Git commit hash em SESSION_LOG para todos 3 arquivos

---

## PLANO ATÔMICO DE IMPACTO DE ARQUIVOS

**Arquivos a criar:**
1. PRODUTO.md.template (template base)
2. DESIGN.md.template (template base)
3. DESIGN_SYSTEM.md.template (template base — NOVO)
4. spec-driven-executor.skill (ou adapter em GEMINI.md)
5. specification-validator.skill
6. SPEC-DRIVEN-VALIDATION.md (seção separada, depois merged em GEMINI.md)

**Arquivos a modificar:**
1. GEMINI.md (adicionar seção SPEC-DRIVEN VALIDATION com 3 refs)
2. SESSION_LOG.md (adicionar seção SPEC_REFERENCES + SPEC_VALIDATION com 3 refs)
3. SKILLS_ORCHESTRATION.yaml (adicionar 2 skills novas + flags em 10 existentes, mencionando 3 specs)
4. SKILLS_HIERARCHY.md (adicionar 2 skills novas + notas sobre 3 specs)

**Nenhum arquivo L3/L4 é modificado.**

---

## ESTRATÉGIA DE VERIFICAÇÃO EMPÍRICA

1. **Testes de conformidade estrutural:**
   - PRODUTO.md.template: contém seções obrigatórias (Visão, Escopo, AC, Constraints, Decision Log)
   - DESIGN.md.template: contém seções obrigatórias (Arquitetura, Stack, Padrões, Testing, Perf, Security)
   - DESIGN_SYSTEM.md.template: contém seções obrigatórias (Cor & Tipografia, Componentes, Grid, Tokens Tailwind, Icons, Accessibility)
   
2. **Testes de spec-driven-executor:**
   - Lê PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md sem erro
   - Extrai AC de PRODUTO.md corretamente
   - Extrai padrões de DESIGN.md corretamente
   - Extrai componentes de DESIGN_SYSTEM.md corretamente
   - Gera PLANO com formato: SPEC_REFERENCES → AC → DESIGN_COMPLIANCE → DESIGN_SYSTEM_COMPLIANCE → CHECKLIST → PLANO_ATÔMICO → VALIDAÇÃO → SIGNATURE
   
3. **Testes de specification-validator:**
   - Recebe relatório de implementação
   - Valida contra AC de PRODUTO.md
   - Valida contra padrões de DESIGN.md
   - Valida contra componentes de DESIGN_SYSTEM.md
   - Output: "5/7 AC passed, 3/3 design patterns ✓, 4/5 UI components ✓" (binário)
   
4. **Testes de GEMINI.md:**
   - Seção SPEC-DRIVEN VALIDATION está presente
   - Protocolo diz "leia PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md"
   - SESSION_LOG foi adaptado com 3 refs
   
5. **Teste end-to-end:**
   - Usar Agente Storyteller V5 (ou outro projeto)
   - Criar PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md para o projeto
   - Executar spec-driven-executor
   - Validar relatório vs AC + design patterns + UI components
   - Score final: N/N items complete

---

## PASSOS ATÔMICOS (17 passos — expandido de 15)

### **PASSO 1: Criar PRODUTO.md.template**

**Aceitação:**
- [ ] Template contém seções: Visão, Escopo (In/Out), AC (por feature), Constraints, Decision Log
- [ ] Todas as seções têm exemplo ou placeholder
- [ ] Arquivo é versionável (plain markdown)
- [ ] Tamanho < 500 linhas (não boilerplate)

**Checklist de Validação:**
- [ ] Arquivo criado em `{project}/PRODUTO.md.template`
- [ ] Lido sem erro (verificar markdown syntax)
- [ ] Cada seção tem instrução clara (não ambígua)
- [ ] AC section tem checkbox template: `- [ ] AC descrição (verificável)`

**Conformance Signature:** 1/1 step complete ✓

---

### **PASSO 2: Criar DESIGN.md.template**

**Aceitação:**
- [ ] Template contém seções: Arquitetura Alto Nível, Stack & Rationale, Padrões de Código, Testing Strategy, Performance Targets, Security Constraints
- [ ] Exemplo ou placeholder em cada seção
- [ ] Arquivo é versionável (plain markdown)
- [ ] Tamanho < 500 linhas

**Checklist de Validação:**
- [ ] Arquivo criado em `{project}/DESIGN.md.template`
- [ ] Lido sem erro (markdown syntax)
- [ ] Seção "Arquitetura Alto Nível" tem placeholder para diagrama (ascii ou mermaid)
- [ ] Seção "Stack & Rationale" tem exemplo de por quê (ex: "Python porque X")

**Conformance Signature:** 1/1 step complete ✓

---

### **PASSO 3: Criar DESIGN_SYSTEM.md.template (NOVO)**

**Aceitação:**
- [ ] Template contém seções: Cor & Tipografia, Componentes UI Base, Grid & Layout, Tokens Tailwind, Icon System, Accessibility & Semantics
- [ ] Exemplos ou placeholders em cada seção
- [ ] Arquivo é versionável (plain markdown)
- [ ] Tamanho < 400 linhas
- [ ] Foco em padrões visuais/frontend (não arquitetura técnica)

**Checklist de Validação:**
- [ ] Arquivo criado em `{project}/DESIGN_SYSTEM.md.template`
- [ ] Lido sem erro (markdown syntax)
- [ ] Seção "Componentes UI Base" tem lista: Button, Input, Card, Modal, Navigation
- [ ] Seção "Tokens Tailwind" tem exemplo: `colors: { primary: '#...', secondary: '#...' }`
- [ ] Seção "Accessibility" menciona WCAG + ARIA

**Conformance Signature:** 1/1 step complete ✓

---

### **PASSO 4: Criar arquivo SPEC-DRIVEN-VALIDATION.md (separado)**

**Aceitação:**
- [ ] Contém seção completa: "Protocol", "Estrutura de Plano Obrigatória", "Behavioral"
- [ ] Pronto para ser merged em GEMINI.md depois
- [ ] Referencia PRODUTO.md, DESIGN.md, DESIGN_SYSTEM.md como 3 fontes de verdade

**Checklist de Validação:**
- [ ] Arquivo criado em `SPEC-DRIVEN-VALIDATION.md`
- [ ] Protocol section diz "leia PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md antes de executar"
- [ ] Estrutura de Plano lista: SPEC_REFERENCES, ACCEPTANCE_CRITERIA, DESIGN_COMPLIANCE, DESIGN_SYSTEM_COMPLIANCE, CONFORMANCE_CHECKLIST, PLANO_ATÔMICO, VALIDAÇÃO_AUTOMÁTICA, SUCCESS_SIGNATURE (8 componentes)
- [ ] Behavioral section cita 3 motivos de parada: "Se AC falha", "Se padrão DESIGN falha", "Se UI não segue DESIGN_SYSTEM"

**Conformance Signature:** 1/1 step complete ✓

---

### **PASSO 5: Adaptar SESSION_LOG.md — Adicionar SPEC_REFERENCES + SPEC_VALIDATION com 3 refs**

**Aceitação:**
- [ ] Seção SPEC_REFERENCES contém: 3 arquivos, commit, versão cada um
- [ ] Seção SPEC_VALIDATION contém: AC count (PRODUTO), pattern count (DESIGN), component count (DESIGN_SYSTEM)

**Checklist de Validação:**
- [ ] SESSION_LOG.md atualizado (seção após FILE_STATUS)
- [ ] Exemplo incluído para 3 arquivos: `PRODUTO.md (commit: abc123, version: 1.0)`, `DESIGN.md (...)`, `DESIGN_SYSTEM.md (...)`
- [ ] SPEC_VALIDATION explica counts para todos 3

**Conformance Signature:** 1/1 step complete ✓

---

### **PASSO 6: Adaptar GEMINI.md — Adicionar seção SPEC-DRIVEN VALIDATION (com 3 refs)**

**Aceitação:**
- [ ] Seção SPEC-DRIVEN VALIDATION inserida após "MONITORAMENTO"
- [ ] Protocol diz "leia PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md"
- [ ] Força leitura de 3 specs antes de qualquer execução

**Checklist de Validação:**
- [ ] GEMINI.md lido sem erro
- [ ] Seção está no lugar correto (após MONITORAMENTO, antes de SKILLS)
- [ ] Estrutura de Plano lista 8 componentes (inclui DESIGN_COMPLIANCE e DESIGN_SYSTEM_COMPLIANCE)
- [ ] Behavioral section tem 3+ regras de parada (AC, Design, Design System)

**Conformance Signature:** 1/1 step complete ✓

---

### **PASSO 7: Adaptar SKILLS_ORCHESTRATION.yaml — Adicionar 2 skills novas (com 3 refs)**

**Aceitação:**
- [ ] `spec-driven-executor` adicionada em L0/L2 com descrição que menciona 3 specs
- [ ] `specification-validator` adicionada em L1 com descrição que menciona validação contra 3 specs

**Checklist de Validação:**
- [ ] SKILLS_ORCHESTRATION.yaml lido sem erro
- [ ] spec-driven-executor em layer L2 com descrição: "Orquestra fluxo spec-driven lendo PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md"
- [ ] specification-validator em layer L1 com descrição: "Valida implementação contra AC + design patterns + UI components"

**Conformance Signature:** 1/1 step complete ✓

---

### **PASSO 8: Adaptar SKILLS_ORCHESTRATION.yaml — Adicionar flags/modos em 10 skills**

**Aceitação:**
- [ ] Todas 10 skills têm campo `modes` ou `flags` com descrição
- [ ] Onde relevante, modos/flags mencionam "valide contra DESIGN.md" ou "valide contra DESIGN_SYSTEM.md"
- [ ] Nenhuma skill foi deletada

**Skills a adaptar:**
1. session-log: `spec_aware: true` (3 refs)
2. diagnose: modo `--spec-compliance` (3 refs)
3. find-skills: modo `--infer-from-spec` (3 refs)
4. audit-integrity: check `spec_compliance_score` (3 refs)
5. impeccable: modo `--mode spec-teach` (inclui DESIGN_SYSTEM padrões)
6. breakdown-epic-pm: modo `--output producto.md`
7. breakdown-epic-arch: modo `--output design.md`
8. breakdown-feature-prd: modo `--update producto.md`
9. breakdown-feature-implementation: flag `--validate-against design.md design_system.md`
10. structured-autonomy-* (3 skills): flag `--spec-source produto.md design.md design_system.md`

**Checklist de Validação:**
- [ ] SKILLS_ORCHESTRATION.yaml lido sem erro
- [ ] Cada skill tem >= 1 modo/flag novo
- [ ] Skills 5, 9, 10 explicitamente mencionam DESIGN_SYSTEM

**Conformance Signature:** 10/10 skills adaptadas ✓

---

### **PASSO 9: Adaptar SKILLS_HIERARCHY.md — Adicionar 2 skills novas + refs 3 specs**

**Aceitação:**
- [ ] spec-driven-executor aparece em L0/L2 na hierarquia visual (mermaid)
- [ ] specification-validator aparece em L1 na hierarquia visual
- [ ] Tabela de routing inclui ambas com contextos que mencionam 3 specs

**Checklist de Validação:**
- [ ] SKILLS_HIERARCHY.md lido sem erro (markdown + mermaid)
- [ ] Diagrama mermaid compila
- [ ] Tabela routing tem linhas:
  - "Spec-driven executor quando precisa validar contra PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md"
  - "Specification-validator quando precisa gate de conformidade automático (3 specs)"

**Conformance Signature:** 1/1 step complete ✓

---

### **PASSO 10: Criar spec-driven-executor (com validação 3 specs)**

**Aceitação:**
- [ ] Lê PRODUTO.md (caminho relativo)
- [ ] Lê DESIGN.md (caminho relativo)
- [ ] Lê DESIGN_SYSTEM.md (caminho relativo)
- [ ] Valida conflitos básicos entre 3 specs
- [ ] Gera PLANO com 8 seções obrigatórias: SPEC_REFERENCES (3 refs) → AC → DESIGN_COMPLIANCE → DESIGN_SYSTEM_COMPLIANCE → CHECKLIST → PLANO_ATÔMICO → VALIDAÇÃO → SIGNATURE

**Checklist de Validação:**
- [ ] Arquivo criado: `spec-driven-executor.{ext}`
- [ ] Função "ler 3 specs": testa lendo 3 arquivos existentes
- [ ] Função "validar conflitos": detecta desvios entre specs (ex: DESIGN diz Python, DESIGN_SYSTEM diz React frontend incompatível)
- [ ] Função "gerar PLANO": output tem 8 seções todas preenchidas
- [ ] SPEC_REFERENCES mostra commit + versão de 3 arquivos

**Test (simular):**
```
Input: PRODUTO.md (3 AC), DESIGN.md (Python stack), DESIGN_SYSTEM.md (React + Tailwind)
Output: PLANO com:
  SPEC_REFERENCES: 3/3 ✓
  ACCEPTANCE_CRITERIA: 3/3 AC ✓
  DESIGN_COMPLIANCE: checklist ✓
  DESIGN_SYSTEM_COMPLIANCE: checklist ✓
  CONFORMANCE_CHECKLIST: 7-10 items ✓
  PLANO_ATÔMICO: steps técnicos ✓
  VALIDAÇÃO_AUTOMÁTICA: checklist ✓
  SUCCESS_SIGNATURE: N/N ✓
Status: PASSED
```

**Conformance Signature:** 1/1 step complete ✓

---

### **PASSO 11: Criar specification-validator (com validação 3 specs)**

**Aceitação:**
- [ ] Recebe relatório de implementação
- [ ] Recebe PRODUTO.md (extrai AC)
- [ ] Recebe DESIGN.md (extrai padrões técnicos)
- [ ] Recebe DESIGN_SYSTEM.md (extrai componentes UI)
- [ ] Compara e gera score ternário: AC compliance, Design compliance, UI compliance
- [ ] Output binário para cada: "N/M items ✓"

**Checklist de Validação:**
- [ ] Arquivo criado: `specification-validator.{ext}`
- [ ] Função "extrair de 3 specs": parse 3 arquivos markdown
- [ ] Função "comparar vs relatório": match claims do relatório contra 3 specs
- [ ] Função "gerar score": 3 scores (AC, Design, UI)

**Test (simular):**
```
Input: 
  - PRODUTO.md com 3 AC
  - DESIGN.md com 2 padrões (State machine, Async pattern)
  - DESIGN_SYSTEM.md com 4 componentes (Button, Input, Card, Modal)
  - Relatório: "Implementei AC 1, AC 2. State machine ✓. Button ✓, Input ✓, Card ✗, Modal ✓"
  
Output: 
  AC Compliance: 2/3 ✓✓✗
  Design Compliance: 1/2 ✓✗
  UI Compliance: 3/4 ✓✓✗✓
  
Overall: 6/9 items passed ✓
Status: PASSED
```

**Conformance Signature:** 1/1 step complete ✓

---

### **PASSO 12: Teste Unitário — spec-driven-executor com 3 specs reais**

**Aceitação:**
- [ ] PRODUTO.md criado com: Visão, 3 AC bem definidas, Constraints
- [ ] DESIGN.md criado com: Stack (Python/FastAPI/WebSocket), 2 padrões
- [ ] DESIGN_SYSTEM.md criado com: Cores, 4 componentes UI base, Tailwind tokens
- [ ] spec-driven-executor executa sem erro contra os 3
- [ ] PLANO contém SPEC_REFERENCES com 3 commit hashes corretos

**Checklist de Validação:**
- [ ] 3 specs no branch (Agente Storyteller V5), commit hashes válidos
- [ ] spec-driven-executor lê 3 sem erro
- [ ] PLANO tem 8 seções, todas preenchidas
- [ ] SPEC_REFERENCES mostra 3 commits corretos
- [ ] DESIGN_COMPLIANCE e DESIGN_SYSTEM_COMPLIANCE sections estão presentes

**Output esperado:**
```
Test: spec-driven-executor com 3 specs reais
PRODUTO.md: presente (commit abc123) ✓
DESIGN.md: presente (commit abc123) ✓
DESIGN_SYSTEM.md: presente (commit abc123) ✓
PLANO gerado com 8 seções: ✓
SPEC_REFERENCES: 3/3 ✓
Design checks: presentes ✓
UI checks: presentes ✓
Status: PASSED
```

**Conformance Signature:** 1/1 teste passed ✓

---

### **PASSO 13: Teste Unitário — specification-validator com 3 specs + relatório mock**

**Aceitação:**
- [ ] Relatório mock implementa 2/3 AC, 1/2 design patterns, 3/4 UI components
- [ ] specification-validator match correto em 3 dimensões
- [ ] Output ternário (AC score, Design score, UI score)

**Checklist de Validação:**
- [ ] Relatório descreve implementação realista
- [ ] specification-validator extrai 3 specs corretamente
- [ ] Scores são precisos e binários
- [ ] Output final: "2/3 AC, 1/2 Design, 3/4 UI = 6/9 overall"

**Output esperado:**
```
Test: specification-validator com 3 specs
AC Compliance: 2/3 ✓✓✗
Design Compliance: 1/2 ✓✗
UI Compliance: 3/4 ✓✓✗✓
Overall Score: 6/9 items passed ✓
Status: PASSED
```

**Conformance Signature:** 1/1 teste passed ✓

---

### **PASSO 14: Teste Integração — Fluxo Completo (Prompt → Plano com 3 specs → Validação)**

**Aceitação:**
- [ ] Prompt diz: "Implemente Feature X validando contra PRODUTO.md, DESIGN.md, DESIGN_SYSTEM.md"
- [ ] spec-driven-executor gera PLANO com AC + Design checks + UI checks
- [ ] Implementação mock (2/3 AC, 1/2 design, 3/4 UI)
- [ ] specification-validator valida ternário
- [ ] Score final é acionável: "Faltam AC 3, Design pattern Y, UI component Z"

**Checklist de Validação:**
- [ ] Prompt claro e específico
- [ ] PLANO contém 3 dimensões de validação
- [ ] Implementação mock é realista
- [ ] Validação ternária é precisa
- [ ] Ação sugerida para cada falha

**Output esperado:**
```
Test: Fluxo completo (3 specs)
Prompt clarity: ✓
PLANO dimensions: AC ✓, Design ✓, UI ✓
Implementação mock: realista ✓
Validação ternária: AC 2/3, Design 1/2, UI 3/4 ✓
Ações sugeridas: presentes ✓
Status: PASSED
```

**Conformance Signature:** 1/1 teste integração passed ✓

---

### **PASSO 15: Merge — SPEC-DRIVEN-VALIDATION em GEMINI.md (com 3 refs)**

**Aceitação:**
- [ ] Conteúdo de SPEC-DRIVEN-VALIDATION.md integrado em GEMINI.md seção 3
- [ ] Sem perda de conteúdo (inclui 3 specs em Protocol, Estrutura, Behavioral)
- [ ] SPEC-DRIVEN-VALIDATION.md deletado após merge
- [ ] GEMINI.md lido sem erro

**Checklist de Validação:**
- [ ] GEMINI.md seção 3 contém completo: Protocol (3 refs) + Estrutura (8 componentes) + Behavioral (3 paradas)
- [ ] Nenhuma seção anterior modificada
- [ ] SPEC-DRIVEN-VALIDATION.md deletado/archived
- [ ] Git log mostra merge commit

**Conformance Signature:** 1/1 merge complete ✓

---

### **PASSO 16: Relatório Final — Conformidade Completa do Rebuild**

**Aceitação (Validação de AC Globais):**
- [ ] PRODUTO.md.template criado
- [ ] DESIGN.md.template criado
- [ ] DESIGN_SYSTEM.md.template criado (NOVO)
- [ ] SPEC-DRIVEN VALIDATION seção em GEMINI.md (com 3 refs)
- [ ] SESSION_LOG adaptado (SPEC_REFERENCES + SPEC_VALIDATION com 3 refs)
- [ ] SKILLS_ORCHESTRATION.yaml: 2 skills novas adicionadas (com 3 refs)
- [ ] SKILLS_ORCHESTRATION.yaml: 10 skills com flags/modes (mencionando 3 specs)
- [ ] SKILLS_HIERARCHY.md atualizado (diagrama + tabela routing com 3 refs)
- [ ] spec-driven-executor implementado (lê + valida 3 specs)
- [ ] specification-validator implementado (valida ternário contra 3 specs)
- [ ] Teste unitário spec-driven-executor: PASSED
- [ ] Teste unitário specification-validator: PASSED
- [ ] Teste integração fluxo completo: PASSED
- [ ] SPEC-DRIVEN-VALIDATION merged em GEMINI.md
- [ ] Branch rebuild-sdd-v2.0 pronto para review

**Checklist de Validação Final:**
- [ ] Todos 15 passos anteriores: ✓
- [ ] DESIGN_SYSTEM.md.template existe e está completo: ✓
- [ ] Nenhuma skill L3/L4 foi modificada: ✓
- [ ] Nenhuma skill deletada (apenas estendida): ✓
- [ ] Todos os testes passaram (3 testes): ✓
- [ ] Git log tem 16 commits atômicos (1 por passo): ✓
- [ ] Branch rebuild-sdd-v2.0 tem todas mudanças: ✓

**Output Esperado (Relatório Final):**
```
═══════════════════════════════════════════════════════════════
  REBUILD SDD v2.0 (COM DESIGN_SYSTEM) — CONFORMIDADE FINAL
═══════════════════════════════════════════════════════════════

Passos Completados: 16/16 ✓
  1. PRODUTO.md.template ✓
  2. DESIGN.md.template ✓
  3. DESIGN_SYSTEM.md.template ✓ (NOVO)
  4. SPEC-DRIVEN-VALIDATION.md ✓
  5. SESSION_LOG adaptado (3 refs) ✓
  6. GEMINI.md seção nova (3 refs) ✓
  7. SKILLS_ORCHESTRATION (2 novas, 3 refs) ✓
  8. SKILLS_ORCHESTRATION (10 adaptadas, 3 refs) ✓
  9. SKILLS_HIERARCHY atualizado (3 refs) ✓
  10. spec-driven-executor (3 specs) ✓
  11. specification-validator (3 specs) ✓
  12. Teste unitário executor ✓
  13. Teste unitário validator ✓
  14. Teste integração ✓
  15. Merge SPEC-DRIVEN-VALIDATION ✓
  16. Relatório final ✓

AC Globais: 16/16 COMPLETE ✓

Testes: 3/3 PASSED ✓
  - spec-driven-executor com 3 specs: PASSED
  - specification-validator com 3 specs: PASSED
  - Fluxo completo (ternário): PASSED

Specs Versionadas:
  - PRODUTO.md (negócio): ✓
  - DESIGN.md (arquitetura técnica): ✓
  - DESIGN_SYSTEM.md (padrões visuais): ✓

Compatibilidade:
  - Skills L3/L4 sem mudança: ✓
  - Nenhuma skill deletada: ✓
  - GEMINI.md sections anteriores intactas: ✓

Versionamento:
  - Branch: rebuild-sdd-v2.0 ✓
  - Commits atômicos: 16/16 ✓
  - Cada passo com commit próprio: ✓

═══════════════════════════════════════════════════════════════
STATUS FINAL: REBUILD PRONTO PARA MERGE
═══════════════════════════════════════════════════════════════

Próximo passo (você decide):
  1. Revisar branch rebuild-sdd-v2.0 em seu repo
  2. Validar mudanças contra ARQUITETURA-SDD-v2.0.md
  3. Testar em projeto real (Agente Storyteller V5?)
  4. Se tudo ok: git merge rebuild-sdd-v2.0 → main
  5. Se encontrar problemas: volte para o passo específico

═══════════════════════════════════════════════════════════════
```

**FIM DO REBUILD. OPERAÇÃO COMPLETA.**

---

## RESTRIÇÕES DURANTE EXECUÇÃO

Você DEVE respeitar estas regras:

1. **Simplicidade Cirúrgica**: Nenhum boilerplate. Cada arquivo novo é minimal.
2. **Sem Breaking Changes**: Skills L3/L4 não são tocadas.
3. **Compatibilidade**: Nenhuma skill é deletada, apenas estendida.
4. **Versionamento**: Cada passo = 1 commit com mensagem clara.
5. **Validação a cada passo**: Antes de passar para próximo, confirme AC = PASSED.
6. **Branch novo**: Toda mudança em `rebuild-sdd-v2.0`, não em `main`.
7. **3 Specs = 1 Contract**: PRODUTO + DESIGN + DESIGN_SYSTEM são 3 dimensões de 1 contrato. Não pense nelas isoladamente.

---

**Próximo passo**: Você aprova ARQUITETURA + PLANO (versão com DESIGN_SYSTEM) → Gerar PROMPT-ANTIGRAVITY-REBUILD.md atualizado → Você leva para Antigravity.
