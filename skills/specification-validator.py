import os
import sys
import re

def parse_checkboxes(content):
    # Retorna o número de checkboxes marcados e o total
    marked = len(re.findall(r'-\s*\[[xX]\]', content))
    unmarked = len(re.findall(r'-\s*\[\s*\]', content))
    total = marked + unmarked
    return marked, total

def run_validator(project_dir, plano_path=None):
    print(f"[*] Inicializando specification-validator para: {project_dir}")
    
    if not plano_path:
        plano_path = os.path.join(project_dir, "PLANO_GERADO.md")
        
    if not os.path.exists(plano_path):
        print(f"[-] Erro: Plano de implementação {plano_path} não encontrado.")
        return False
        
    with open(plano_path, "r", encoding="utf-8") as f:
        plano_content = f.read()
        
    # Extrai cada seção do plano de implementação
    sections = {}
    current_section = None
    current_lines = []
    
    for line in plano_content.splitlines():
        if line.startswith("## "):
            if current_section:
                sections[current_section] = "\n".join(current_lines)
            current_section = line.strip().lstrip("#").strip()
            current_lines = []
        elif current_section:
            current_lines.append(line)
            
    if current_section:
        sections[current_section] = "\n".join(current_lines)
        
    # Realiza a validação ternária nas seções correspondentes
    ac_marked, ac_total = parse_checkboxes(sections.get("2. ACCEPTANCE_CRITERIA", ""))
    design_marked, design_total = parse_checkboxes(sections.get("3. DESIGN_COMPLIANCE", ""))
    ui_marked, ui_total = parse_checkboxes(sections.get("4. DESIGN_SYSTEM_COMPLIANCE", ""))
    
    overall_marked = ac_marked + design_marked + ui_marked
    overall_total = ac_total + design_total + ui_total
    
    print("\n" + "="*50)
    print("        RELATÓRIO DE VALIDAÇÃO TERNÁRIA (SDD v2.0)")
    print("="*50)
    print(f"1. AC Compliance (Negócio)    : {ac_marked}/{ac_total} passed")
    print(f"2. Design Compliance (Técnico) : {design_marked}/{design_total} passed")
    print(f"3. UI Compliance (Visual)      : {ui_marked}/{ui_total} passed")
    print("-"*50)
    print(f"Overall Result                 : {overall_marked}/{overall_total} passed")
    print("="*50)
    
    if overall_marked < overall_total:
        print("\n[✗] STATUS: FALHA NA CONFORMIDADE.")
        print("[!] Correções pendentes necessárias antes do commit final.")
        return False
    else:
        print("\n[✓] STATUS: PASSED.")
        print("[+] Implementação em conformidade estrita com as especificações.")
        return True

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    run_validator(os.path.abspath(target_dir))
