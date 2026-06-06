import os
import sys
import re
import subprocess

def get_git_commit(filepath):
    try:
        # Tenta obter o commit do git para o arquivo específico
        res = subprocess.run(['git', 'log', '-n', '1', '--pretty=format:%h', '--', filepath], 
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    except Exception:
        pass
    return "unknown_commit"

def run_executor(project_dir):
    print(f"[*] Inicializando spec-driven-executor para: {project_dir}")
    
    produto_path = os.path.join(project_dir, "PRODUTO.md")
    design_path = os.path.join(project_dir, "DESIGN.md")
    design_system_path = os.path.join(project_dir, "DESIGN_SYSTEM.md")
    
    # 1. Leitura das especificações
    specs = {"PRODUTO.md": produto_path, "DESIGN.md": design_path, "DESIGN_SYSTEM.md": design_system_path}
    found_specs = {}
    
    for name, path in specs.items():
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                found_specs[name] = f.read()
            print(f"[+] Encontrado: {name}")
        else:
            print(f"[!] Ausente: {name}")
            
    # 2. Validação de Conflitos Lógicos
    conflitos = []
    if "DESIGN.md" in found_specs and "DESIGN_SYSTEM.md" in found_specs:
        design_content = found_specs["DESIGN.md"].lower()
        ds_content = found_specs["DESIGN_SYSTEM.md"].lower()
        
        # Exemplo simples de verificação de stack técnica cruzada
        if "python" in design_content and "react" in ds_content and "tailwind" in ds_content:
            # Não é necessariamente um conflito se for backend Python e frontend React, 
            # mas vamos alertar se houver inconsistências nítidas de tecnologia.
            pass
            
    # 3. Extração de Conteúdo
    ac_list = []
    if "PRODUTO.md" in found_specs:
        # Encontra seções de AC e extrai checkboxes
        content = found_specs["PRODUTO.md"]
        # Encontra todas as linhas que têm checkboxes
        for line in content.splitlines():
            if "- [ ]" in line or "- [x]" in line:
                # Limpa a marcação e guarda a descrição
                ac_desc = re.sub(r'^.*?-\s*\[[ xX]\]\s*', '', line).strip()
                # Remove duplicação de prefixo se já houver
                ac_desc = re.sub(r'^AC\s*\d+\s*:\s*', '', ac_desc).strip()
                ac_list.append(ac_desc)
                
    design_patterns = []
    if "DESIGN.md" in found_specs:
        # Extrai os sub-tópicos ou listas de padrões de código
        content = found_specs["DESIGN.md"]
        lines = content.splitlines()
        for line in lines:
            if line.strip().startswith("-") and not line.strip().startswith("- ["):
                design_patterns.append(line.strip().lstrip("-").strip())
                
    ui_components = []
    if "DESIGN_SYSTEM.md" in found_specs:
        content = found_specs["DESIGN_SYSTEM.md"]
        # Tenta achar componentes UI base
        lines = content.splitlines()
        for line in lines:
            if line.strip().startswith("###"):
                ui_components.append(line.strip().lstrip("#").strip())

    # 4. Geração do Plano
    commit_prod = get_git_commit(produto_path) if "PRODUTO.md" in found_specs else "local"
    commit_design = get_git_commit(design_path) if "DESIGN.md" in found_specs else "local"
    commit_ds = get_git_commit(design_system_path) if "DESIGN_SYSTEM.md" in found_specs else "local"
    
    plano_content = f"""# PLANO DE IMPLEMENTAÇÃO E EXECUÇÃO

## 1. SPEC_REFERENCES
- PRODUTO.md (commit: {commit_prod}, version: 1.0)
- DESIGN.md (commit: {commit_design}, version: 1.0)
- DESIGN_SYSTEM.md (commit: {commit_ds}, version: 1.0)

## 2. ACCEPTANCE_CRITERIA
"""
    if ac_list:
        for i, ac in enumerate(ac_list, 1):
            plano_content += f"- [ ] AC {i}: {ac}\n"
    else:
        plano_content += "- [ ] AC 1: [Critério de aceitação padrão para validação]\n"
        
    plano_content += "\n## 3. DESIGN_COMPLIANCE\n"
    if design_patterns:
        for pat in design_patterns[:5]:
            plano_content += f"- [ ] Validar padrão técnico: {pat}\n"
    else:
        plano_content += "- [ ] Validar conformidade com as diretrizes do DESIGN.md\n"
        
    plano_content += "\n## 4. DESIGN_SYSTEM_COMPLIANCE\n"
    if ui_components:
        for comp in ui_components[:5]:
            plano_content += f"- [ ] Validar padrão de UI/Componente: {comp}\n"
    else:
        plano_content += "- [ ] Validar conformidade com os tokens e componentes de DESIGN_SYSTEM.md\n"
        
    plano_content += """
## 5. CONFORMANCE_CHECKLIST
- [ ] Setup do ambiente e validação das especificações (PRODUTO, DESIGN, DESIGN_SYSTEM).
- [ ] Confirmação de que não existem conflitos de tecnologia entre as especificações.
- [ ] Validação do escopo com as restrições arquiteturais definidas.

## 6. PLANO_ATÔMICO
- [ ] Passo 1: Implementar as estruturas básicas de backend conforme o DESIGN.md.
- [ ] Passo 2: Construir e estilizar a interface de acordo com o DESIGN_SYSTEM.md.
- [ ] Passo 3: Integrar a lógica e rodar testes de critérios de aceitação (AC).

## 7. VALIDAÇÃO_AUTOMÁTICA
- [ ] Rodar testes unitários e de integração para validar cada critério de aceitação de negócio.
- [ ] Executar auditoria de design visual para verificar a correta aplicação dos componentes de UI.

## 8. SUCCESS_SIGNATURE
Status: 0 de __TOTAL_AC__ critérios completados.
"""
    total_ac = len(ac_list) if ac_list else 1
    plano_content = plano_content.replace("__TOTAL_AC__", str(total_ac))

    plano_output_path = os.path.join(project_dir, "PLANO_GERADO.md")
    with open(plano_output_path, "w", encoding="utf-8") as f:
        f.write(plano_content)
        
    print(f"[+] PLANO_GERADO.md gerado com sucesso em: {plano_output_path}")
    return True

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    run_executor(os.path.abspath(target_dir))
