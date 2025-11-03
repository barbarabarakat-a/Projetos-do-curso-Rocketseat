def adicionar_contato(lista_contatos, nome_contato, telefone_contato, email_contato):
    contatos = {
        "Nome": nome_contato,
        "Telefone": telefone_contato,
        "Email": email_contato,
        "Favorito": False
    }
    lista_contatos.append(contatos)
    print("Seu contato foi adicionado!")
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
    if opcao_favorito == "marcar":
        try:
            indice_ajustado = int(indice_contato) - 1
            if indice_ajustado >= 0 and indice_ajustado < len(lista_contatos):
                lista_contatos[indice_ajustado]["Favorito"] = True
                print(f"Contato de indice {indice_contato} marcardo como favorito.")

            else:
                print("Indice Invalido! Esse indice nao existe na sua lista de contatos.")
        except ValueError:
            print("indice Invalido! Por favor, digite um numero valido: ")


    elif opcao_favorito == "desmarcar":
        try:
            indice_ajustado = int(indice_contato) - 1
            if indice_ajustado >= 0 and indice_ajustado < len(lista_contatos):
                lista_contatos[indice_ajustado]["Favorito"] = False
                print(f"Contato de indice {indice_contato} desmarcado como favorito.")

            else:
                print("Indice Invalido! Esse indice nao existe na sua lista de contatos.")
        except ValueError:
            print("indice Invalido! Por favor, digite um numero valido: ")

        return
    
def visualizar_favoritos(lista_contatos):
    print("Agenda de contatos favoritos:")

    favoritos = [c for c in lista_contatos if c.get("Favorito")]

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

def deletar_contato(indice_contato, lista_contatos):
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(lista_contatos):
        del lista_contatos[indice_ajustado]
        print(f"Contato de indice {indice_contato} foi removido da sua agenda de contatos.")
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
        opcao_favorito = input("Voce deseja marcar ou desmarcar um contato como favorito: ")
        
        if opcao_favorito == "marcar":
            visualizar_lista(lista_contatos)
            indice_contato = input("Digite o indice do contato que deseja favoritar: ")
            contato_favorito(indice_contato, lista_contatos)

        elif opcao_favorito == "desmarcar":
            visualizar_lista(lista_contatos)
            indice_contato = input("Digite o indice do contato que desejar remover dos contatos favoritos: ")
            contato_favorito(indice_contato, lista_contatos)

    elif opcao == "5":
        visualizar_favoritos(lista_contatos)

    elif opcao == "6":
        visualizar_lista(lista_contatos)
        indice_contato = int(input("Digite o indice do contato que deseja remover da sua agenda de contatos: "))
        deletar_contato(indice_contato, lista_contatos)

    elif opcao == "7":
        print("Ate breve!")
        break
