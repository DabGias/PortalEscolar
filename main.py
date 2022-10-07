from subalgoritmos import *

if __name__ == "__main__":
    provas = []
    senha = "aDmin@2022"

    opc_acesso = int(input("""Portal 🚪
    
1 - Admin;
2 - Aluno;
3 - Sair.

Escolha o acesso: """).strip())

    while opc_acesso > 3 or opc_acesso < 1:
        print("⚠ Opção inválida! ⚠")
        opc_acesso = int(input("""Portal 🚪

1 - Admin;
2 - Aluno;
3 - Sair.

Escolha o acesso: """).strip())

    while opc_acesso != 3:
        if opc_acesso == 1:
            senha_adm = input("Digite a senha: ").strip()

            while senha_adm != senha:
                print("⚠ Senha inválida! ⚠")
                senha_adm = input("Digite a senha: ").strip()

            opc_adm = int(input("""Bem-vindo(a) ADM 🤵
            
1 - Criar prova;
2 - Listar alunos e provas;
3 - Sair.

Escolha sua opção: """).strip())

            while opc_adm > 3 or opc_adm < 1:
                print("⚠ Opção inválida! ⚠")
                opc_adm = int(input("""Bem-vindo(a) ADM 🤵

1 - Criar prova;
2 - Listar alunos e provas;
3 - Sair.

Escolha sua opção: """).strip())

            while opc_adm != 3:
                if opc_adm == 1:
                    criar_prova(provas)
                if opc_adm == 2:
                    listar_tudo(provas)

                opc_adm = int(input("""Bem-vindo(a) ADM 🤵
        
1 - Criar prova;
2 - Listar alunos e provas;
3 - Sair.

Escolha sua opção: """).strip())

        if opc_acesso == 2:
            iniciar_prova(provas)

        opc_acesso = int(input("""Portal 🚪
    
1 - Admin;
2 - Aluno;
3 - Sair.

Escolha o acesso: """).strip())

    print("Você saiu! 👋")
