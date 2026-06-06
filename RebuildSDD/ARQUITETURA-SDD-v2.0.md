# ARQUITETURA — Especificação Dirigida por Desenvolvimento v2.0

**Data**: 2026-06-06  
**Versão**: 1.0  
**Objetivo**: Eliminar dependência de chat externo como "fonte de verdade". Especificação versionada no repo.

---

## 1. PROBLEMA IDENTIFICADO (Status Quo)

```
NotebookLM (base de conhecimento)
    ↓
Gemini Web (planejador, post-mortem, validador)
    ↓
Prompt ad-hoc → Antigravity (executor)
    ↓
Relatório → Gemini Web valida (opinião, não conformidade)
```

**Gargalos:**
- Verdade técnica fica em chat (volátil, sem versionamento)
- Validação é narrativa ("ficou bom?"), não binária
- Escalabilidade quebra com múltiplos projetos
- Ciclos de rework por falta de contrato claro

---

## 2. SOLUÇÃO PROPOSTA (SDD v2.0)

### 2.1 Camada Nova: Especificação Versionada no Repo (3 Fontes de Verdade)

```
PRODUTO.md (repo)        ← Visão, features, AC, constraints (negócio)
    ↓
DESIGN.md (repo)         ← Arquitetura, padrões code, stack, segurança (técnico)
    ↓
DESIGN_SYSTEM.md (repo)  ← UI padrões, componentes, tokens, Tailwind (visual/frontend)
    ↓
Prompt refino (você + Claude/aqui)
    ↓
Antigravity [lê PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md]
    ↓
Implementação com validação automática vs AC + padrões visuais
    ↓
Relatório binário: AC 1 ✓, AC 2 ✗, Design Compliance ✓, etc
    ↓
Você valida (não Gemini Web)
```

**Divisão de responsabilidades:**
- **PRODUTO.md**: O QUÊ (visão, features, aceitação)
- **DESIGN.md**: COMO (arquitetura, padrões técnicos, segurança, performance)
- **DESIGN_SYSTEM.md**: ESTILO (UI, componentes, tokens visuais, Tailwind patterns)

**Gemini Web novo papel:**
- ❌ Não é fonte de verdade técnica
- ✅ Consultor para análises pontuais
- ✅ Refinador de ideias novas (opcional)

### 2.2 Templates Obrigatórios

#### PRODUTO.md
```markdown
# PRODUTO.md — Especificação de Negócio

## Visão (1-2 parágrafos)
[Descrição clara do que é, por que existe]

## Escopo
### In
- Feature A
- Feature B
### Out
- Non-feature X (justificativa)

## Acceptance Criteria (por feature)
### Feature A
- [ ] AC 1: [verificável]
- [ ] AC 2: [verificável]
- [ ] AC 3: [verificável]

## Constraints
- Técnicas
- Negócio
- Segurança

## Decision Log
| Data | Decisão | Justificativa | Impacto |
|---|---|---|---|
```

#### DESIGN.md
```markdown
# DESIGN.md — Especificação Técnica (Backend/Infra)

## Arquitetura Alto Nível
[Diagrama + descrição]

## Stack & Rationale
- Backend: [Por quê]
- Database: [Por quê]
- Infrastructure: [Por quê]

## Padrões de Código
- Linguagem/Framework specific
- Estrutura de pastas
- Convenções de naming

## Testing Strategy
- Cobertura esperada
- Tipos de teste (unit/integration/e2e)
- Critérios de aceitação de teste

## Performance Targets
- Latência
- Throughput
- Recursos

## Security Constraints
- Autenticação/Autorização
- Data sensitivity
- Compliance
```

#### DESIGN_SYSTEM.md (NOVO)
```markdown
# DESIGN_SYSTEM.md — Especificação Visual (Frontend)

## Cor & Tipografia
- Paleta de cores (com hex/RGB)
- Tipografia (families, weights, sizes)
- Modo Dark/Light (se aplicável)

## Componentes UI Base
- Button variants (primary, secondary, danger, etc)
- Input types (text, email, password, etc)
- Card, Modal, Navigation, etc
- Cada componente: props, usage, accessibility

## Grid & Layout
- Breakpoints (mobile, tablet, desktop)
- Spacing scale (gap, padding, margin)
- Layout patterns (sidebar, hero, etc)

## Tokens Tailwind (se aplicável)
- Custom colors: `colors: { ... }`
- Custom sizing: `spacing: { ... }`
- Custom typography: `fontSize: { ... }`

## Icon System
- Icon library (Lucide, Feather, etc)
- Sizing conventions
- Usage patterns

## Accessibility & Semantics
- WCAG compliance level
- Semantic HTML patterns
- Focus states, ARIA labels
```

---

## 3. MUDANÇAS ESTRUTURAIS

### 3.1 GEMINI.md — Nova Seção

Adicionar após "MONITORAMENTO":

```yaml
# 3. SPEC-DRIVEN VALIDATION (NOVO)

Protocol:
  - Antes de QUALQUER execução, leia:
    - PRODUTO.md (se existe no repo) — fonte de verdade: negócio
    - DESIGN.md (se existe no repo) — fonte de verdade: arquitetura técnica
    - DESIGN_SYSTEM.md (se existe no repo) — fonte de verdade: padrões visuais/frontend
  - Valide o plano proposto contra os 3 arquivos
  - Se houver conflito: PAUSA e relata antes de executar
  - Acceptance Criteria = SEMPRE de PRODUTO.md, nunca de prompt do turno
  - Design patterns = SEMPRE de DESIGN.md, nunca inferir
  - UI patterns = SEMPRE de DESIGN_SYSTEM.md, nunca criar ad-hoc
  
Estrutura de Plano Obrigatória:
  - SPEC_REFERENCES (commit + versão de PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md)
  - ACCEPTANCE_CRITERIA (cópia de PRODUTO.md, com checkboxes)
  - DESIGN_COMPLIANCE (validação contra DESIGN.md patterns — se houver)
  - DESIGN_SYSTEM_COMPLIANCE (validação contra DESIGN_SYSTEM.md padrões visuais — se houver)
  - CONFORMANCE_CHECKLIST (validação antes de impl)
  - PLANO_ATÔMICO (steps técnicos)
  - VALIDAÇÃO_AUTOMÁTICA (AC após impl + design checks)
  - SUCCESS_SIGNATURE (N/N items complete)

Behavioral:
  - Se AC falhar durante impl, PAUSA
  - Se padrão DESIGN.md não for seguido, PAUSA
  - Se componente UI não segue DESIGN_SYSTEM.md, PAUSA
  - Não continue "salvando" com workarounds
  - Relata incompletude, não silencia
```

### 3.2 SESSION_LOG — Nova Seção

Adicionar após "FILE_STATUS":

```markdown
SPEC_REFERENCES:
  - PRODUTO.md (commit: XYZ, version: 1.0)
  - DESIGN.md (commit: XYZ, version: 1.0)
  - DESIGN_SYSTEM.md (commit: XYZ, version: 1.0)
  
SPEC_VALIDATION:
  - PRODUTO.md AC count: N
  - DESIGN.md patterns count: N
  - DESIGN_SYSTEM.md components count: N
  - Conflicts with current impl: [lista ou "none"]
```

Se spec mudar mid-session, SESSION_LOG avisa.

---

## 4. SKILLS — MUDANÇAS

### 4.1 Skills Compatíveis (Sem Mudança)
- vibe-coding
- karpathy-guidelines
- doublecheck
- skill-creator
- quality-playbook
- security-review
- threat-model-analyst
- secret-scanning
- breakdown-plan
- breakdown-test
- commit-message-storyteller
- github-* (issues, release)
- humanizer-pt-br

### 4.2 Skills com Adaptação (Novo Modo/Flag)

#### session-log
- **Novo**: Seção `SPEC_REFERENCES`
- **Novo**: Seção `SPEC_VALIDATION`
- **Comportamento**: Avisa se spec mudou desde SESSION anterior

#### diagnose
- **Novo modo**: `diagnose --spec-compliance`
- **Output**: AC matrix vs current state (✓/✗/⚠️)

#### find-skills
- **Novo modo**: `find-skills --infer-from-spec`
- **Input**: Lê PRODUTO.md + DESIGN.md
- **Output**: Sugere skills baseado em requirements

#### audit-integrity
- **Novo check**: "Relatório valida AC de PRODUTO.md?"
- **Score**: Inclui spec-compliance score

#### impeccable
- **Novo modo**: `impeccable --mode spec-teach`
- **Função**: Lê DESIGN.md, ensina padrões ao executor

#### breakdown-epic-pm
- **Novo modo**: `breakdown-epic-pm --output producto.md`
- **Output**: Arquivo PRODUTO.md estruturado (não relatório)

#### breakdown-epic-arch
- **Novo modo**: `breakdown-epic-arch --output design.md`
- **Output**: Arquivo DESIGN.md estruturado (não relatório)

#### breakdown-feature-prd
- **Novo modo**: `breakdown-feature-prd --update producto.md`
- **Comportamento**: Adiciona feature ao PRODUTO.md existente

#### breakdown-feature-implementation
- **Novo flag**: `--validate-against design.md`
- **Comportamento**: Valida plano contra DESIGN.md antes de gerar

#### structured-autonomy-plan, generate, implement (trio)
- **Novo flag**: `--spec-source producto.md design.md`
- **Comportamento**: 
  - Plan: AC derivadas de PRODUTO.md
  - Generate: referencia spec em implementation.md
  - Implement: valida próprio output vs AC, pausa se falhar

### 4.3 Skills Novas (CRÍTICAS)

#### spec-driven-executor (L0/L2)
```
Função: Orquestra fluxo spec-driven
- Lê PRODUTO.md e DESIGN.md no início
- Estrutura PLANO com AC + CHECKLIST + CONFORMANCE
- Força relatório binário (N/N items ✓)
- Pausa se AC falhar, não continua silenciosamente
```

#### specification-validator (L1)
```
Função: Gate de conformidade automático
- Input: Relatório de implementação + PRODUTO.md AC
- Output: "5/7 AC passed, 2 failed/incomplete"
- Ação: Se < 100%, bloqueia entrega ou sugere rework
```

---

## 5. FLUXO NOVO (End-to-End)

```
1. Ideia
   ↓
2. [Você ou Gemini Web] → Cria/atualiza PRODUTO.md + DESIGN.md
   ↓
3. [Você] → Cria prompt refino (Claude/aqui) com:
   - Referência a PRODUTO.md + DESIGN.md
   - Feature específica para implementar
   - Context vindo de SESSION_LOG
   ↓
4. [Você] → Traz prompt para Antigravity
   ↓
5. [Antigravity via spec-driven-executor]:
   - Lê PRODUTO.md + DESIGN.md
   - Valida conflitos
   - Gera PLANO com AC cópia de PRODUTO.md
   - Implementa
   - Valida próprio output vs AC
   - Relatório: "AC 1: ✓, AC 2: ✗, etc"
   ↓
6. [specification-validator]:
   - Valida conformidade automática
   - Score: N/N items
   ↓
7. [Você] → Lê relatório binário
   - Se 100% ✓: Comita em main
   - Se < 100%: Pede ajuste ou refaz spec
   ↓
8. [Gemini Web] → (Opcional) Análise de por quê AC X falhou
```

---

## 6. IMPACTO

| Aspecto | Antes | Depois |
|---|---|---|
| Fonte de verdade | Chat (Gemini Web) | Repo (PRODUTO.md + DESIGN.md + DESIGN_SYSTEM.md) |
| Versionamento | Nenhum (chat é volátil) | Git (auditável, rastreável) |
| Validação | Narrativa ("ficou bom?") | Binária (N/N AC ✓) + Design ✓ |
| Gemini Web role | Fonte de verdade técnica | Consultor ocasional |
| Escalabilidade | Quebra com 3+ projetos | Suporta N projetos |
| Ciclos de rework | Frequentes (falta contrato) | Raros (contrato é spec) |
| Automação | Planejamento manual + Antigravity | Planejamento automatizado + Validação automática |

---

## 7. IMPLEMENTAÇÃO (Visão Geral)

**Fase 1 — Preparação (aqui, agora):**
- Gerar ARQUITETURA-SDD-v2.0.md ✓
- Gerar PLANO-EXECUÇÃO-REBUILD.md
- Gerar PROMPT-ANTIGRAVITY-REBUILD.md

**Fase 2 — Delegação (Antigravity executa):**
- Você traz PLANO para Antigravity
- Antigravity executa conforme plano
- Traz relatório com conformância

**Fase 3 — Validação (Você):**
- Lê relatório
- Testa resultado
- Comita ou refaz

---

## 8. ROLLBACK (Se Necessário)

Tudo em branch novo. Se não gostar:
```bash
git checkout main
git branch -D rebuild-sdd-v2.0
```

Volta ao status quo em segundos.

---

**Próximo passo**: PLANO-EXECUÇÃO-REBUILD.md com 12-15 passos atômicos, AC, Checklist, Conformance.
