# PROMPT — Antigravity Rebuild SDD v2.0 (COM DESIGN_SYSTEM)

**Data de Criação**: 2026-06-06  
**Executor**: Antigravity (Gemini 3.5 Flash)  
**Contexto**: Rebuild com 3 fontes de verdade (PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md)  
**Duração Estimada**: 2-3 turnos  

---

## PRÉ-CONDIÇÕES

Antes de executar este prompt:

1. ✅ Você leu ARQUITETURA-SDD-v2.0.md atualizado (entende 3 specs)
2. ✅ Você leu PLANO-EXECUÇÃO-REBUILD-V2.md (sabe os 16 passos)
3. ✅ Você tem acesso aos arquivos originais:
   - GEMINI.md (configuração atual)
   - SESSION_LOG.md (template de persistência)
   - SKILLS_ORCHESTRATION.yaml (mapa de skills)
   - SKILLS_HIERARCHY.md (hierarquia visual)
4. ✅ Você tem um branch Git novo: `rebuild-sdd-v2.0`
5. ✅ Você NÃO vai modificar skills L3 ou L4 (execução/entrega)
6. ✅ Você vai tratar PRODUTO.md, DESIGN.md, DESIGN_SYSTEM.md como **3 dimensões de 1 contrato** (não isoladamente)

---

## OBJETIVO

Executar 16 passos atômicos para transformar Antigravity para **spec-driven com 3 specs**:

```
De: NotebookLM → Gemini Web (verdade) → Prompt → Antigravity
Para: PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md (repo) → Prompt → Antigravity [lê 3 specs]
```

**Resultado esperado:**
- 3 templates criados (PRODUTO.md, DESIGN.md, DESIGN_SYSTEM.md)
- GEMINI.md adaptado (+ seção SPEC-DRIVEN VALIDATION com 3 refs)
- SESSION_LOG adaptado (+ SPEC_REFERENCES com 3 refs)
- 10 skills com novos modos/flags (mencionando 3 specs onde relevante)
- 2 skills novas (spec-driven-executor com 3 specs, specification-validator com validação ternária)
- 3 testes de conformidade passando
- Branch rebuild-sdd-v2.0 com 16 commits atômicos, pronto para review

---

## CONTEXTO

### Situação Atual
- 363 skills, 5 camadas (L0-L4)
- GEMINI.md governa protocolo, funciona bem
- SESSION_LOG estrutura recuperação de contexto
- **Gargalo**: Especificação fica em chat (Gemini Web, NotebookLM), sem versionamento
- **Problema adicional**: Padrões visuais/design system não têm versão versionada

### Solução Proposta (SDD v2.0 com 3 Specs)
- **PRODUTO.md no repo**: Fonte de verdade sobre **negócio** (visão, features, AC)
- **DESIGN.md no repo**: Fonte de verdade sobre **arquitetura técnica** (stack, padrões, segurança)
- **DESIGN_SYSTEM.md no repo**: Fonte de verdade sobre **padrões visuais/frontend** (UI, componentes, tokens)
- **spec-driven-executor**: Orquestra fluxo lendo **3 specs**
- **specification-validator**: Gate automático com validação **ternária** (AC ✓, Design ✓, UI ✓)
- **Gemini Web reduzido**: Consultor ocasional, não fonte de verdade

### Impacto
| Antes | Depois |
|---|---|
| Verdade em chat (2 conceitos) | Verdade em repo (3 specs, 3 conceitos) |
| Validação narrativa | Validação ternária (AC + Design + UI) |
| Padrões visuais "por instinto" | DESIGN_SYSTEM.md versionado |
| UI inconsistente entre turnos | UI consistente (conforme spec) |

---

## ESCOPO — 16 PASSOS ATÔMICOS

Você vai executar **exatamente estes 16 passos na sequência**. Cada passo tem AC (Acceptance Criteria) que você DEVE validar antes de passar para próximo.

**Os primeiros 3 passos criam templates. Os próximos criam skills. Os últimos 3 testam ternário.**

### Passo 1: Criar PRODUTO.md.template

**Descrição:**  
Template base para especificação de negócio (visão, features, AC, constraints). Sem mudanças vs versão anterior.

**Aceitação:**
- [ ] Template contém seções: Visão, Escopo (In/Out), AC (com checkboxes), Constraints, Decision Log
- [ ] Plain markdown, < 500 linhas
- [ ] Cada seção tem instrução clara

**Checklist:**
- [ ] Arquivo criado em `{project}/PRODUTO.md.template`
- [ ] Markdown syntax válido
- [ ] AC template: `- [ ] AC (verificável)`

**Output esperado:**
```
Arquivo: {project}/PRODUTO.md.template
Status: PASSED
```

**Passe para Passo 2.**

---

### Passo 2: Criar DESIGN.md.template

**Descrição:**  
Template base para especificação técnica (arquitetura, stack, padrões, testes, perf, segurança). Sem mudanças vs versão anterior.

**Aceitação:**
- [ ] Template contém seções: Arquitetura Alto Nível, Stack & Rationale, Padrões, Testing, Perf, Security
- [ ] Plain markdown, < 500 linhas
- [ ] Exemplos em cada seção

**Checklist:**
- [ ] Arquivo criado em `{project}/DESIGN.md.template`
- [ ] Markdown syntax válido
- [ ] Stack & Rationale tem exemplo: "Backend: Python — porque X"

**Output esperado:**
```
Arquivo: {project}/DESIGN.md.template
Status: PASSED
```

**Passe para Passo 3.**

---

### Passo 3: Criar DESIGN_SYSTEM.md.template (NOVO)

**Descrição:**  
Template base para especificação visual/frontend (cores, componentes, grid, tokens, icons, accessibility).

**Aceitação:**
- [ ] Template contém seções: Cor & Tipografia, Componentes UI Base, Grid & Layout, Tokens Tailwind, Icon System, Accessibility & Semantics
- [ ] Plain markdown, < 400 linhas
- [ ] Componentes listados (Button, Input, Card, Modal, Navigation)
- [ ] Tailwind tokens com exemplo

**Checklist:**
- [ ] Arquivo criado em `{project}/DESIGN_SYSTEM.md.template`
- [ ] Markdown syntax válido
- [ ] Componentes: Button, Input, Card, Modal, Navigation presentes
- [ ] Tokens Tailwind: exemplo com colors/spacing/typography

**Output esperado:**
```
Arquivo: {project}/DESIGN_SYSTEM.md.template
Componentes: 5+ presentes ✓
Tokens: exemplificados ✓
Status: PASSED
```

**Passe para Passo 4.**

---

### Passo 4: Criar SPEC-DRIVEN-VALIDATION.md (Separado)

**Descrição:**  
Documento que será merged em GEMINI.md depois. Agora com **3 refs** em Protocol, Estrutura, Behavioral.

**Aceitação:**
- [ ] Contém 3 subseções: Protocol, Estrutura de Plano, Behavioral
- [ ] Protocol diz: "Leia PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md"
- [ ] Estrutura de Plano lista 8 componentes (inclui DESIGN_COMPLIANCE e DESIGN_SYSTEM_COMPLIANCE)
- [ ] Behavioral tem 3 motivos de parada (AC, Design, UI)

**Checklist:**
- [ ] Arquivo criado: `SPEC-DRIVEN-VALIDATION.md`
- [ ] Protocol: 3 refs mencionadas
- [ ] Estrutura: 8 componentes listados
- [ ] Behavioral: "pausa se AC falha", "pausa se Design falha", "pausa se UI falha"

**Output esperado:**
```
Arquivo: SPEC-DRIVEN-VALIDATION.md
Seções: 3/3 ✓
Refs: 3/3 ✓
Componentes: 8/8 ✓
Status: PASSED
```

**Passe para Passo 5.**

---

### Passo 5: Adaptar SESSION_LOG.md (com 3 Refs)

**Descrição:**  
Adicionar SPEC_REFERENCES (3 arquivos) e SPEC_VALIDATION (3 counts).

**Aceitação:**
- [ ] SPEC_REFERENCES tem 3 linhas (PRODUTO.md, DESIGN.md, DESIGN_SYSTEM.md com commit + versão)
- [ ] SPEC_VALIDATION tem 3 counts (AC count, patterns count, components count)

**Checklist:**
- [ ] SESSION_LOG.md atualizado
- [ ] Exemplo: `PRODUTO.md (commit: abc123, version: 1.0)` × 3
- [ ] SPEC_VALIDATION counts presentes

**Output esperado:**
```
FILE: SESSION_LOG.md
SPEC_REFERENCES: 3/3 ✓
SPEC_VALIDATION counts: 3/3 ✓
Status: PASSED
```

**Passe para Passo 6.**

---

### Passo 6: Adaptar GEMINI.md (com 3 Refs)

**Descrição:**  
Inserir SPEC-DRIVEN VALIDATION seção com **3 referências** em Protocol, Estrutura, Behavioral.

**Aceitação:**
- [ ] Seção está após "MONITORAMENTO"
- [ ] Protocol diz "Leia PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md"
- [ ] Estrutura tem 8 componentes (inclui DESIGN_COMPLIANCE + DESIGN_SYSTEM_COMPLIANCE)
- [ ] Behavioral tem 3 paradas

**Checklist:**
- [ ] GEMINI.md lido sem erro
- [ ] Seção no lugar certo
- [ ] 3 refs em Protocol
- [ ] 8 componentes em Estrutura
- [ ] 3 paradas em Behavioral

**Output esperado:**
```
FILE: GEMINI.md
SPEC-DRIVEN VALIDATION: inserida ✓
Refs: 3/3 ✓
Componentes: 8/8 ✓
Status: PASSED
```

**Passe para Passo 7.**

---

### Passo 7: Adaptar SKILLS_ORCHESTRATION.yaml (2 Skills Novas)

**Descrição:**  
Adicionar spec-driven-executor (L2) e specification-validator (L1) com descrição que menciona **3 specs**.

**Aceitação:**
- [ ] spec-driven-executor em L2 com "lê PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md"
- [ ] specification-validator em L1 com "valida contra AC + design + UI"

**Checklist:**
- [ ] SKILLS_ORCHESTRATION.yaml lido sem erro
- [ ] Ambas skills presentes
- [ ] Descrições mencionam 3 specs

**Output esperado:**
```
FILE: SKILLS_ORCHESTRATION.yaml
spec-driven-executor: adicionada em L2 ✓
specification-validator: adicionada em L1 ✓
Refs (3): presentes em ambas ✓
Status: PASSED
```

**Passe para Passo 8.**

---

### Passo 8: Adaptar SKILLS_ORCHESTRATION.yaml (10 Skills Existentes)

**Descrição:**  
Estender 10 skills com novos modos/flags. Onde relevante, mencionam "DESIGN.md" ou "DESIGN_SYSTEM.md".

**Skills a adaptar:**
1. session-log: `spec_aware: true`
2. diagnose: `--spec-compliance`
3. find-skills: `--infer-from-spec`
4. audit-integrity: `spec_compliance_score`
5. impeccable: `--mode spec-teach` (inclui DESIGN_SYSTEM)
6. breakdown-epic-pm: `--output producto.md`
7. breakdown-epic-arch: `--output design.md`
8. breakdown-feature-prd: `--update producto.md`
9. breakdown-feature-implementation: `--validate-against design.md design_system.md` (2 specs)
10. structured-autonomy-*: `--spec-source produto.md design.md design_system.md` (3 specs)

**Aceitação:**
- [ ] Todas 10 têm modos/flags novos
- [ ] Skills 5, 9, 10 explicitamente mencionam DESIGN_SYSTEM

**Checklist:**
- [ ] SKILLS_ORCHESTRATION.yaml lido sem erro
- [ ] 10 skills com 1+ novo modo/flag
- [ ] skill 5 (impeccable) menciona DESIGN_SYSTEM
- [ ] skill 9 menciona design.md + design_system.md
- [ ] skill 10 menciona 3 specs

**Output esperado:**
```
FILE: SKILLS_ORCHESTRATION.yaml
10 skills adaptadas: 10/10 ✓
DESIGN_SYSTEM refs: skills 5, 9, 10 ✓
Status: PASSED
```

**Passe para Passo 9.**

---

### Passo 9: Adaptar SKILLS_HIERARCHY.md

**Descrição:**  
Atualizar diagrama mermaid + tabela routing com 2 skills novas que mencionam **3 specs**.

**Aceitação:**
- [ ] spec-driven-executor em L2 no diagrama
- [ ] specification-validator em L1 no diagrama
- [ ] Tabela routing com contextos que mencionam 3 specs

**Checklist:**
- [ ] SKILLS_HIERARCHY.md lido sem erro
- [ ] Diagrama compila (mermaid válido)
- [ ] 2 skills novas presentes
- [ ] Tabela routing menciona "3 specs" para ambas

**Output esperado:**
```
FILE: SKILLS_HIERARCHY.md
spec-driven-executor: no diagrama ✓
specification-validator: no diagrama ✓
Tabela routing: 2 linhas novas (3 specs) ✓
Mermaid: válido ✓
Status: PASSED
```

**Passe para Passo 10.**

---

### Passo 10: Criar spec-driven-executor (com 3 Specs)

**Descrição:**  
Implementar skill que lê **3 specs**, valida conflitos, gera PLANO com **8 seções** (inclui DESIGN_COMPLIANCE + DESIGN_SYSTEM_COMPLIANCE).

**Aceitação:**
- [ ] Lê PRODUTO.md, DESIGN.md, DESIGN_SYSTEM.md (caminho relativo)
- [ ] Valida conflitos entre 3 specs
- [ ] Gera PLANO com 8 seções: SPEC_REFERENCES (3) → AC → DESIGN_COMPLIANCE → DESIGN_SYSTEM_COMPLIANCE → CHECKLIST → PLANO → VALIDAÇÃO → SIGNATURE

**Checklist:**
- [ ] Arquivo criado: `spec-driven-executor.{ext}`
- [ ] Lê 3 specs sem erro
- [ ] Valida conflitos
- [ ] PLANO tem 8 seções completas
- [ ] SPEC_REFERENCES mostra 3 commits

**Test (simular):**
```
Input: PRODUTO.md (3 AC), DESIGN.md (Python), DESIGN_SYSTEM.md (React)
Output PLANO:
  SPEC_REFERENCES: 3/3 ✓
  AC: 3/3 ✓
  DESIGN_COMPLIANCE: checklist ✓
  DESIGN_SYSTEM_COMPLIANCE: checklist ✓
  CHECKLIST: 7+ items ✓
  PLANO_ATÔMICO: ✓
  VALIDAÇÃO_AUTOMÁTICA: ✓
  SUCCESS_SIGNATURE: N/N ✓
Status: PASSED
```

**Passe para Passo 11.**

---

### Passo 11: Criar specification-validator (com Validação Ternária)

**Descrição:**  
Implementar skill que valida **3 dimensões** (AC, Design, UI) contra 3 specs. Output ternário: "2/3 AC, 1/2 Design, 3/4 UI".

**Aceitação:**
- [ ] Extrai AC de PRODUTO.md
- [ ] Extrai padrões de DESIGN.md
- [ ] Extrai componentes de DESIGN_SYSTEM.md
- [ ] Compara vs relatório
- [ ] Output: 3 scores (AC, Design, UI)

**Checklist:**
- [ ] Arquivo criado: `specification-validator.{ext}`
- [ ] Extrai 3 specs sem erro
- [ ] Compara vs relatório
- [ ] Output 3 scores

**Test (simular):**
```
Input:
  - PRODUTO.md (3 AC)
  - DESIGN.md (2 padrões)
  - DESIGN_SYSTEM.md (4 componentes)
  - Relatório: "AC 1 ✓, AC 2 ✓, AC 3 ✗. Pattern 1 ✓, Pattern 2 ✗. Button ✓, Input ✓, Card ✗, Modal ✓"

Output:
  AC Compliance: 2/3 ✓✓✗
  Design Compliance: 1/2 ✓✗
  UI Compliance: 3/4 ✓✓✗✓
  Overall: 6/9 ✓

Status: PASSED
```

**Passe para Passo 12.**

---

### Passo 12: Teste Unitário — spec-driven-executor com 3 Specs Reais

**Descrição:**  
Usar Agente Storyteller V5 (ou outro projeto). Criar 3 specs minimais. Executar spec-driven-executor. Validar 8 seções.

**Aceitação:**
- [ ] PRODUTO.md (commit XYZ): Visão + 3 AC
- [ ] DESIGN.md (commit XYZ): Stack + 2 padrões
- [ ] DESIGN_SYSTEM.md (commit XYZ): Cores + 4 componentes
- [ ] spec-driven-executor lê 3 sem erro
- [ ] PLANO tem 8 seções

**Checklist:**
- [ ] 3 specs presentes, commits válidos
- [ ] spec-driven-executor executa
- [ ] SPEC_REFERENCES: 3 commits ✓
- [ ] DESIGN_COMPLIANCE: presente ✓
- [ ] DESIGN_SYSTEM_COMPLIANCE: presente ✓

**Output esperado:**
```
Test: spec-driven-executor com 3 specs reais
PRODUTO.md (commit abc): ✓
DESIGN.md (commit abc): ✓
DESIGN_SYSTEM.md (commit abc): ✓
PLANO seções: 8/8 ✓
SPEC_REFERENCES: 3/3 ✓
Status: PASSED
```

**Passe para Passo 13.**

---

### Passo 13: Teste Unitário — specification-validator com Validação Ternária

**Descrição:**  
Relatório mock: 2/3 AC, 1/2 Design, 3/4 UI. Validar scores ternários corretos.

**Aceitação:**
- [ ] Relatório mock com implementação parcial de 3 dimensões
- [ ] specification-validator valida ternário
- [ ] Scores precisos: 2/3 AC, 1/2 Design, 3/4 UI

**Checklist:**
- [ ] Relatório realista
- [ ] 3 specs lidos corretamente
- [ ] Scores binários (não "aproximado")
- [ ] Output final: 6/9 overall

**Output esperado:**
```
Test: specification-validator com 3 specs
AC: 2/3 ✓✓✗
Design: 1/2 ✓✗
UI: 3/4 ✓✓✗✓
Overall: 6/9 ✓
Status: PASSED
```

**Passe para Passo 14.**

---

### Passo 14: Teste Integração — Fluxo Completo (Ternário)

**Descrição:**  
Prompt → spec-driven-executor (PLANO com 3 dims) → implementação mock → specification-validator (score ternário) → resultado acionável.

**Aceitação:**
- [ ] Prompt claro sobre 3 specs
- [ ] PLANO tem 3 dimensões de validação
- [ ] Implementação mock realista
- [ ] Scores ternários precisos
- [ ] Ação sugerida para cada falha

**Checklist:**
- [ ] Prompt menciona 3 specs
- [ ] PLANO: AC ✓, Design ✓, UI ✓
- [ ] Relatório: dimensão por dimensão
- [ ] Scores: N/M para AC, Design, UI
- [ ] Ações: "AC 3 requer X, Design Y requer Z, UI component W requer..."

**Output esperado:**
```
Test: Fluxo completo (ternário)
Prompt: claro (3 specs) ✓
PLANO dimensions: 3/3 ✓
Implementação: realista ✓
Scores ternários: precisos ✓
Ações: presentes ✓
Status: PASSED
```

**Passe para Passo 15.**

---

### Passo 15: Merge — SPEC-DRIVEN-VALIDATION em GEMINI.md

**Descrição:**  
Integrar SPEC-DRIVEN-VALIDATION.md (com 3 refs) em GEMINI.md seção 3. Deletar arquivo separado.

**Aceitação:**
- [ ] Conteúdo integrado (Protocol + Estrutura + Behavioral com 3 refs)
- [ ] Sem perda/duplicação
- [ ] SPEC-DRIVEN-VALIDATION.md deletado
- [ ] GEMINI.md lido sem erro

**Checklist:**
- [ ] GEMINI.md seção 3 completa
- [ ] 3 refs em todos os places (Protocol, Estrutura, Behavioral)
- [ ] Nenhuma seção anterior modificada
- [ ] Arquivo separado deletado

**Output esperado:**
```
FILE: GEMINI.md
SPEC-DRIVEN VALIDATION: merged ✓
3 refs: completas ✓
Compatibilidade: mantida ✓
Arquivo separado: deletado ✓
Status: PASSED
```

**Passe para Passo 16.**

---

### Passo 16: Relatório Final — Conformidade Completa (com DESIGN_SYSTEM)

**Descrição:**  
Validar todos 15 passos anteriores + DESIGN_SYSTEM.md.template. Marcar 16/16 completo.

**Aceitação (AC Globais):**
- [ ] PRODUTO.md.template criado
- [ ] DESIGN.md.template criado
- [ ] DESIGN_SYSTEM.md.template criado ← NOVO
- [ ] SPEC-DRIVEN VALIDATION em GEMINI.md (3 refs)
- [ ] SESSION_LOG (SPEC_REFERENCES + SPEC_VALIDATION com 3 refs)
- [ ] SKILLS_ORCHESTRATION: 2 novas (3 refs)
- [ ] SKILLS_ORCHESTRATION: 10 adaptadas (3 refs)
- [ ] SKILLS_HIERARCHY: atualizado (3 refs)
- [ ] spec-driven-executor (3 specs, 8 seções)
- [ ] specification-validator (ternário)
- [ ] Teste executor: PASSED
- [ ] Teste validator: PASSED
- [ ] Teste integração: PASSED
- [ ] Merge completo
- [ ] Branch rebuild-sdd-v2.0 pronto

**Checklist Final:**
- [ ] 16 passos: 16/16 ✓
- [ ] DESIGN_SYSTEM.md.template: presente ✓
- [ ] Nenhuma skill L3/L4 modificada: ✓
- [ ] Nenhuma skill deletada: ✓
- [ ] 3 testes PASSED: ✓
- [ ] 16 commits atômicos: ✓

**Output Final (Relatório):**
```
═══════════════════════════════════════════════════════════════
  REBUILD SDD v2.0 (COM DESIGN_SYSTEM) — CONFORMIDADE FINAL
═══════════════════════════════════════════════════════════════

Passos: 16/16 ✓
Templates: 3/3 ✓ (PRODUTO, DESIGN, DESIGN_SYSTEM)
Skills novas: 2/2 ✓ (executor + validator)
Skills adaptadas: 10/10 ✓
Testes: 3/3 PASSED ✓
Commits: 16/16 atômicos ✓

AC Globais: 16/16 COMPLETE ✓

Specs Versionadas (3):
  ✓ PRODUTO.md (negócio)
  ✓ DESIGN.md (arquitetura)
  ✓ DESIGN_SYSTEM.md (visual) ← NOVO

Validação: TERNÁRIA
  ✓ AC Compliance (de PRODUTO.md)
  ✓ Design Compliance (de DESIGN.md)
  ✓ UI Compliance (de DESIGN_SYSTEM.md)

═══════════════════════════════════════════════════════════════
STATUS: PRONTO PARA MERGE
═══════════════════════════════════════════════════════════════

Próximos passos:
  1. Review branch rebuild-sdd-v2.0
  2. Validar contra ARQUITETURA-SDD-v2.0.md
  3. Testar em projeto real
  4. Merge para main
  5. Comemorar 🎉

═══════════════════════════════════════════════════════════════
```

---

## RESTRIÇÕES DURANTE EXECUÇÃO

1. **Simplicidade Cirúrgica**: Sem boilerplate.
2. **Sem Breaking Changes**: L3/L4 intactas.
3. **Compatibilidade**: Skills estendidas, não deletadas.
4. **Versionamento**: 1 commit por passo.
5. **Validação**: AC = PASSED antes de próximo passo.
6. **Branch**: rebuild-sdd-v2.0 (não main).
7. **3 Specs = 1 Contract**: Não pense isoladamente. Negócio + Técnica + Visual = 1 pacote.

---

## IMPORTANTE

**Você está aplicando SDD v2.0 a SDD v2.0 mesmo.**

Objetivo: criar o sistema enquanto o usa. Se ficar confuso, relata para o humano refinar.

---

**Pronto?**  
Copie PLANO-EXECUÇÃO-REBUILD-V2.md + este prompt para uma sessão nova do Antigravity quando quiser executar.

Estruture assim:
- [Turno 1] Cole este prompt + ARQUITETURA atualizado
- [Turno 2-3] Execute passos conforme padrão "!execute passo X" ou "continue"
- [Final] Relatório com 16/16 ✓

---

**Fim do Prompt.**
