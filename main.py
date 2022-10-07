from subalgoritmos import *

admins = []
alunos = []
provas = []

opc_acesso = int(input("""Portal 🚪

1 - Admin;
2 - Aluno;
3 - Sair.

Escolha o acesso: """))

while opc_acesso != 3:
    while opc_acesso > 3 or opc_acesso < 0:
        print("⚠ Opção inválida! ⚠")
        opc_acesso = int(input("""Portal 🚪

1 - Admin;
2 - Aluno;
3 - Sair.

Escolha o acesso: """))

    if opc_acesso == 1:
        pass
    if opc_acesso == 2:
        pass
