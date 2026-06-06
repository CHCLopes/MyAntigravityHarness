import os
import sys
import subprocess

def run_integration_test():
    print("[*] Iniciando Teste de Integração: Fluxo Completo SDD v2.0")
    
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SandBox", "AgenteStoryteller"))
    plano_path = os.path.join(project_dir, "PLANO_GERADO.md")
    
    # Passo 1: Limpar plano gerado anterior
    if os.path.exists(plano_path):
        os.remove(plano_path)
        print("[+] Plano anterior limpo.")
        
    # Passo 2: Executar o spec-driven-executor
    print("[*] Executando spec-driven-executor...")
    executor_script = os.path.join(os.path.dirname(__file__), "spec-driven-executor.py")
    res = subprocess.run([sys.executable, executor_script, project_dir], 
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(res.stdout)
    
    if not os.path.exists(plano_path):
        print("[-] Falha: PLANO_GERADO.md não foi criado pelo executor.")
        return False
        
    # Passo 3: Mockar implementação de forma parcial (2/3 AC, 1/2 Design, 3/4 UI)
    print("[*] Simulando implementação parcial (Mock)...")
    with open(plano_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Aplica as marcações simuladas
    content = content.replace("- [ ] AC 1:", "- [x] AC 1:")
    content = content.replace("- [ ] AC 2:", "- [x] AC 2:")
    content = content.replace("- [ ] Validar padrão técnico: Backend: Python 3.11 + FastAPI", "- [x] Validar padrão técnico: Backend: Python 3.11 + FastAPI")
    content = content.replace("- [ ] Validar padrão de UI/Componente: Button", "- [x] Validar padrão de UI/Componente: Button")
    content = content.replace("- [ ] Validar padrão de UI/Componente: Card", "- [x] Validar padrão de UI/Componente: Card")
    content = content.replace("- [ ] Validar padrão de UI/Componente: Input", "- [x] Validar padrão de UI/Componente: Input")
    
    # Adiciona um quarto elemento UI que falhou para fechar 3/4
    content = content.replace(
        "## 4. DESIGN_SYSTEM_COMPLIANCE\n- [x] Validar padrão de UI/Componente: Button\n- [x] Validar padrão de UI/Componente: Card\n- [x] Validar padrão de UI/Componente: Input",
        "## 4. DESIGN_SYSTEM_COMPLIANCE\n- [x] Validar padrão de UI/Componente: Button\n- [x] Validar padrão de UI/Componente: Card\n- [x] Validar padrão de UI/Componente: Input\n- [ ] Validar padrão de UI/Componente: Modal"
    )
    
    # Modifica a seção de Design Compliance para fechar 1/2
    content = content.replace(
        "## 3. DESIGN_COMPLIANCE\n- [x] Validar padrão técnico: Backend: Python 3.11 + FastAPI\n- [ ] Validar padrão técnico: Comunicação: WebSockets para baixa latência\n- [ ] Validar padrão técnico: LLM: Ollama rodando localmente\n- [ ] Validar padrão técnico: Padrão Singleton para gerenciar conexão do banco.\n- [ ] Validar padrão técnico: Tratamento de exceções centralizado em middleware.",
        "## 3. DESIGN_COMPLIANCE\n- [x] Validar padrão técnico: Backend: Python 3.11 + FastAPI\n- [ ] Validar padrão técnico: Comunicação: WebSockets para baixa latência"
    )
    
    with open(plano_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    # Passo 4: Executar o specification-validator
    print("[*] Executando specification-validator...")
    validator_script = os.path.join(os.path.dirname(__file__), "specification-validator.py")
    res = subprocess.run([sys.executable, validator_script, project_dir], 
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(res.stdout)
    
    # Passo 5: Analisar e sugerir ações corretivas claras e acionáveis
    print("[*] Analisando itens pendentes para ação corretiva...")
    with open(plano_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    lines = content.splitlines()
    pendentes_ac = []
    pendentes_design = []
    pendentes_ui = []
    current_sec = None
    
    for line in lines:
        if "## 2. ACCEPTANCE_CRITERIA" in line:
            current_sec = "AC"
        elif "## 3. DESIGN_COMPLIANCE" in line:
            current_sec = "DESIGN"
        elif "## 4. DESIGN_SYSTEM_COMPLIANCE" in line:
            current_sec = "UI"
        elif line.startswith("## "):
            current_sec = None
            
        if line.strip().startswith("- [ ]") and current_sec:
            item = line.replace("- [ ]", "").strip()
            if current_sec == "AC":
                pendentes_ac.append(item)
            elif current_sec == "DESIGN":
                pendentes_design.append(item)
            elif current_sec == "UI":
                pendentes_ui.append(item)
                
    print("\n" + "="*50)
    print("        AÇÕES CORRETIVAS E ITENS FALTANTES")
    print("="*50)
    if pendentes_ac:
        for it in pendentes_ac:
            print(f"[AÇÃO AC]: Implementar pendência de negócio -> {it}")
    if pendentes_design:
        for it in pendentes_design:
            print(f"[AÇÃO DESIGN]: Implementar pendência técnica -> {it}")
    if pendentes_ui:
        for it in pendentes_ui:
            print(f"[AÇÃO UI]: Implementar pendência de design system -> {it}")
    print("="*50)
    
    print("\n[+] Teste de Integração concluído com sucesso.")
    return True

if __name__ == "__main__":
    run_integration_test()
