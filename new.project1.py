def adicionar_tarefas(lista_tarefa, nome_tarefa):
    tarefa = {"Tarefa": nome_tarefa,  "Completada": False}  #Criamos um dicionario para pegar as chaves e valores
    lista_tarefa.append(tarefa)
    print(f"A tarefa '{nome_tarefa}' foi adicionada.")
    return


def visualizar_lista(lista_tarefa):
    print("Lista de tarefas")
    if not lista_tarefa:
        print("Nenhuma tarefa adicionada ainda.")
    else:
        for indice, tarefa in enumerate(lista_tarefa, start=1):
            status = "x" if tarefa["Completada"] else " "
            nome_tarefa = tarefa["Tarefa"]
            print(f"{indice}. [{status}] {nome_tarefa}")
    return


def atualizar_tarefa(indice_tarefa, lista_tarefa, novo_nome_tarefa):
    indice_ajustado = int(indice_tarefa) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(lista_tarefa):
        lista_tarefa[indice_ajustado]["Tarefa"] = novo_nome_tarefa
        print(f"A tarefa de indice {indice_tarefa} foi atualizado para '{novo_nome_tarefa}'")
    else:
        print("Indice invalido!")
    return

def completar_tarefa(indice_tafera, lista_tarefa):
    indice_ajustado = int(indice_tarefa) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(lista_tarefa):
        lista_tarefa[indice_ajustado]["Completada"] = True
        print(f"Tarefa {indice_tafera} marcada como completada")
    else:
        print("Indice invalido!")
    return

def deletar_tarefas_completadas(lista_tarefa):
    for tarefa in lista_tarefa:
        if tarefa ["Completada"] == True:
            lista_tarefa.remove(tarefa)
    print("Tarefas completadas foram deletadas")
    return

lista_tarefa = []  # If its inside of the looping, always will be erased

while True:
    print("\n Bem-vindo ao nosso Gerenciador de Tarefas")

    print("""
    1. Adicionar tarefas à lista
    2. Visualizar a lista de tarefas
    3. Atualizar o nome das tarefas
    4. Marcar tarefas como completas
    5. Deletar tarefas completadas
    6. Sair
    """)

    opcao = int(input("Digite o número da sua opção: "))

    
    if opcao == 1:
        nome_tarefa = input("Qual tarefa você deseja adicionar? ")
        adicionar_tarefas(lista_tarefa, nome_tarefa)

    elif opcao == 2:
        visualizar_lista(lista_tarefa)

    elif opcao == 3:
        visualizar_lista(lista_tarefa)

        indice_tarefa = input("Digite o indice da tarefa que deseja atualizar: ")
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(indice_tarefa, lista_tarefa, novo_nome_tarefa)

    elif opcao == 4:
        visualizar_lista(lista_tarefa)
        indice_tarefa = input("Digite o indice da tarefa que seja marcar como completada: ")
        completar_tarefa(indice_tarefa, lista_tarefa)

    elif opcao == 5:
        deletar_tarefas_completadas(lista_tarefa)
        visualizar_lista(lista_tarefa)

    elif opcao == 6:
        print("Até breve!")
        break  # This stops the loop

    else:
        print("Opção inválida! Digite um número de 1 a 6.")









#############   EXEMPLO DA AGENDA DE TAREFAS ###########
def adicionar_contato(lista_contatos, nome_contato, telefone_contato, email_contato):
    contatos = {
        "Nome": nome_contato,
        "Telefone": telefone_contato,
        "Email": email_contato,
        "Favorito": False
    }
    lista_contatos.append(contatos)
    print("Seu contato foi adionado!")
    return

def visualizar_lista(lista_contatos):
    print("Agenda de contatos:")
    if not lista_contatos:
        print("Sua agenda nao possui contatos.")
    else:
        for indice, contato in enumerate(lista_contatos, start=1):
            status = "★" if contato["Favorito"] else " "
            nome_contato = contato["Nome"]
            print(f"""{indice}. [ {status} ]   
        Nome: {nome_contato}
        Telefone: {telefone_contato}
        Email: {email_contato}
""")
    return
    
def editar_contato(indice_contato, lista_contatos, novo_nome_contato, novo_telefone_contato, novo_email_contato):
    try:
        indice_ajustado = int(indice_contato) - 1
        if indice_ajustado >= 0 and indice_ajustado < len(lista_contatos):
            lista_contatos[indice_ajustado]["Nome"] = novo_nome_contato
            lista_contatos[indice_ajustado]["Telefone"] = novo_telefone_contato
            lista_contatos[indice_ajustado]["Email"] = novo_email_contato
            print(f"""
                O contato de indice {indice_contato} foi atualizado:
                Nome: {novo_nome_contato}
                Telefone: {novo_telefone_contato}
                Email: {novo_email_contato}
              """)
        else:
            print("Indice Invalido! Esse indice nao existe na sua lista de contatos.")
    except ValueError:
        print("indice Invalido! Por favor, digite um numero valido: ")
        return

def contato_favorito(indice_contato, lista_contatos):
    try:
        indice_ajustado = int(indice_contato) - 1
        if indice_ajustado >= 0 and indice_ajustado < len(lista_contatos):
            lista_contatos[indice_ajustado]["Favorito"] = True
            print(f"Contato de indice {indice_contato} marcardo como favorito.")

        else:
            print("Indice Invalido! Esse indice nao existe na sua lista de contatos.")
    except ValueError:
        print("indice Invalido! Por favor, digite um numero valido: ")
        return

def visualizar_favoritos(lista_contatos):
    print("Agenda de contatos favoritos:")

    favoritos = [contato for contatos in lista_contatos if contatos.get("Favorito")]
    
    if not lista_contatos:
        print("Sua agenda nao possui nenhum contato favorito.")
    else:
        for indice, contato in enumerate(favoritos, start=1):
                nome_contato = contato.get("Nome", "Sem nome")   
                telefone_contato = contato.get("Telefone", "Sem telefone")   
                email_contato = contato.get("Email", "Sem email")   
                print(f"""{indice}. [ { "★" } ]   
        Nome: {nome_contato}
        Telefone: {telefone_contato}
        Email: {email_contato}
""")
    return 

lista_contatos = []

while True:
    print("\n Agenda de Contatos")
    print("""
1. Adicionar um contato (Nome, Telefone, Email)
2. Visualizar a lista de contados cadastrados
3. Editar um contato existente
4. Marcar/Desmarcar um contato como favorito
5. Visualizar a lista de contatos favoritos
6. Apagar um contato
7. Sair
""")

    opcao = input("Digite a opcao que deseja: ")

    if opcao == "1":
        nome_contato = input("Digite o nome do contato que voce deseja cadastrar: ")
        telefone_contato = input(f"Digite o numero de telefone do {nome_contato}: ")
        email_contato = input(f"Digite o email do {nome_contato}: ")

        adicionar_contato(lista_contatos, nome_contato, telefone_contato, email_contato)
        
    elif opcao == "2":
        visualizar_lista(lista_contatos)

    elif opcao == "3":
        visualizar_lista(lista_contatos)
        indice_contato = input("Digite o indice do contato que deseja alterar: ")
        novo_nome_contato = input("Digite o novo nome do contato: ")
        novo_telefone_contato = input("Digite o novo telefone do contato: ")
        novo_email_contato = input("Digite o novo email do contato: ")
        editar_contato(indice_contato, lista_contatos, novo_nome_contato, novo_telefone_contato, novo_email_contato)

    elif opcao == "4":
        visualizar_lista(lista_contatos)
        indice_contato = input("Digite o indice do contato que deseja favoritar: ")
        contato_favorito(indice_contato, lista_contatos)

    elif opcao == "5":
                visualizar_favoritos(lista_contatos)


    elif opcao == "7":
        print("Ate breve!")
        break
