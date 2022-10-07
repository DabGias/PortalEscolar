def criar_prova(provas: list):
    prova = {
        "id_prova": int(input("Digite o ID da prova: ").strip()),
        "titulo_prova": input("Qual o título da prova? ").title().strip(),
        "num_quest": int(input("Qual o número de questões? ").strip()),
        "quests": [],
        "completou": []
    }

    while prova["id_prova"] < 1:
        print("⚠ Opção inválida! ⚠")
        prova["id_prova"] = int(input("Digite o ID da prova: ").strip())

    for prova_salva in provas:
        if prova["id_prova"] == prova_salva["id_prova"]:
            print("⚠ Opção inválida! Já existe uma prova com esse ID! ⚠")
            prova["id_prova"] = int(input("Digite o ID da prova: ").strip())

    while prova["num_quest"] < 1:
        print("⚠ Opção inválida! ⚠")
        prova["num_quest"] = int(input("Qual o número de questões: ").strip())

    for num_quest in range(prova["num_quest"]):
        quest = {
            "enunciado": input("Digite o enunciado da questão {}: ".format(num_quest + 1)).strip().capitalize(),
            "num_alt": int(input("Qual o número de alternativas? ").strip()),
            "alts": [],
            "resp_corr": ""
        }

        while quest["num_alt"] < 3 or quest["num_alt"] > 5:
            print("⚠ Opção inválida! A questão deve ter 3 ou 5 alternativas! ⚠")
            quest["num_alt"] = int(input("Qual o número de alternativas? ").strip())

        for num_alt in range(quest["num_alt"]):
            alt = input("Digite a alternativa: ").strip().upper()
            quest["alts"].append(alt)

        quest["resp_corr"] = input("Qual a alternativa correta? ").strip().upper()

        prova["quests"].append(quest)

    provas.append(prova)


def listar_tudo(provas: list):
    if len(provas) > 0:
        for index_p, prova in enumerate(provas):
            print("-" * 20)
            print("{}. {}: ".format(index_p + 1, prova["titulo_prova"]))
            for index_a, aluno in enumerate(prova["completou"]):
                print("    {}. Nome: {} Nota: {}/{}".format(index_a + 1, aluno["nome_aluno"], aluno["nota_aluno"],
                                                            prova["num_quest"]))
        print("-" * 20)
    else:
        print("⚠ Não há provas registradas! ⚠")


def iniciar_prova(provas: list):
    if len(provas) > 0:
        aluno = {
            "nome_aluno": input("Digite seu nome: "),
            "nota_aluno": 0
        }

        id_prova = int(input("Digite o ID da prova: "))

        while id_prova < 0:
            print("⚠ Opção inválida! ⚠")
            id_prova = int(input("Digite o ID da prova: "))

        for prova in provas:
            if prova["id_prova"] == id_prova:
                for quest in prova["quests"]:
                    print("-" * 20)
                    print(quest["enunciado"])
                    for alt in quest["alts"]:
                        print(alt)
                    resp_aluno = input("Digite a alternativa: ").strip().upper()

                    if quest["resp_corr"] == resp_aluno:
                        aluno["nota_aluno"] += 1

                print("-" * 20)
                print("Nota: {}".format(aluno["nota_aluno"]))
                print("-" * 20)
                prova["completou"].append(aluno)
    else:
        print("⚠ Não há provas cadastradas! ⚠")
