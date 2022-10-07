def cria_prova(provas: list):
    prova = {
        "id_prova": int(input("Digite o ID da prova: ").strip()),
        "titulo_prova": input("Qual o título da prova? ").title().strip(),
        "num_quest": int(input("Qual o número de questões? ").strip()),
        "quests": []
    }

    while prova["id_prova"] < 1:
        print("⚠ Opção inválida! ⚠")
        prova["id_prova"] = int(input("Digite o ID da prova: ").strip())

    for prova_salva in provas:
        while prova["id_prova"] == prova_salva["id_prova"]:
            print("⚠ Opção inválida! Já existe uma prova com esse ID! ⚠")
            prova["id_prova"] = int(input("Digite o ID da prova: ").strip())

    while prova["num_quest"] < 1:
        print("⚠ Opção inválida! ⚠")
        prova["num_quest"] = int(input("Qual o número de questões: ").strip())

    for num_quest in range(prova["num_quest"]):
        quest = {
            "enunciado": input("Digite o enunciado: ").strip().capitalize(),
            "num_alt": int(input("Qual o número de alternativas? ").strip()),
            "alts": [],
            "resp_corr": ""
        }

        while quest["num_alt"] < 3 or quest["num_alt"] > 5:
            print("⚠ Opção inválida! A questão deve ter 3 ou 5 alternativas! ⚠")
            quest["num_alt"] = int(input("Qual o número de alternativas? ").strip())

        for num_alt in range(quest["num_alt"]):
            alt = input("Digite a alternativa: ".strip().capitalize())
            quest["alts"].append(alt)

        prova["quests"].append(quest)

    provas.append(prova)
