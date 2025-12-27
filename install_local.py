import subprocess
import sys
import os

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print("Instalando pacote cpf_utils em modo editable...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", "."])
        print("\nInstalação concluída com sucesso!")
        print("Use: from cpf_utils import validar_cpf, formatar_cpf")
    except subprocess.CalledProcessError as e:
        print("Falha ao instalar o pacote.")
        print(e)

if __name__ == "__main__":
    main()

