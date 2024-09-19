def input_dados_contato():
    print("Por favor, insira as informações para o registro do novo contato.")
    nome     = input("Nome: ")
    telefone = input("Telefone: ")
    email    = input("Email: ")
    favorito = int(input("Marcar como favorito? [1- Sim] - [0 - Não]: "))
    print("Salvando os dados do contato...")

    return nome, telefone, email, favorito


def exibir_contatos(contatos: list, apenas_favoritos = False):
    print("Listando os contatos salvos: ")
    for contato in range(0, len(contatos)):
        if apenas_favoritos:
            if contatos[contato]['favorito']:
                print(f"{contato + 1} - Nome: {contatos[contato]['nome']}, Telefone: {contatos[contato]['telefone']}, Email: {contatos[contato]['email']}, Favorito: {contatos[contato]['favorito']}")

        else:
            print(f"{contato + 1} - Nome: {contatos[contato]['nome']}, Telefone: {contatos[contato]['telefone']}, Email: {contatos[contato]['email']}, Favorito: {contatos[contato]['favorito']}")


def editar_contato(indice: int, contatos: list):
    indice = indice - 1

    if indice < 0 or indice > len(contatos):
        raise Exception("Indice inválido para a edição.")

    nome, telefone, email, favorito = input_dados_contato()

    contatos[indice]["nome"]     = nome
    contatos[indice]["telefone"] = telefone
    contatos[indice]["email"]    = email
    contatos[indice]["favorito"] = favorito

    return contatos


def marcar_desmarcar_como_favorito(indice: int, contatos: list):
    indice = indice - 1

    if indice < 0 or indice > len(contatos):
        raise Exception("Indice inválido.")
    
    contatos[indice]["favorito"] = not contatos[indice]["favorito"]

    return contatos


def remover_contato(indice: int, contatos: list):
    indice = indice - 1

    if indice < 0 or indice > len(contatos):
        raise Exception("Indice inválido.")
    
    contatos.pop(indice)

    return contatos


if __name__ == "__main__":

    contatos = [
        {
            "nome":     "Rodrigo Santiago", 
            "telefone": "19 9 9999-9999", 
            "email":    "email@email.com", 
            "favorito": False
        }
    ]


    print("1 - Adicionar novo contato")
    print("2 - Listar contatos cadastrados")
    print("3 - Editar um contato")
    print("4 - Marcar/Desmarcar um contato como favorito")
    print("5 - Listar contatos marcados como favoritos")
    print("6 - Apagar um contato")
    print("7 - Sair")

    while True:
        try:
            match int(input("\nEscolha uma ação: ")):
                case 1:
                    nome, telefone, email, favorito = input_dados_contato()

                    contatos.append({
                        "nome":     nome, 
                        "telefone": telefone, 
                        "email":    email, 
                        "favorito": True if favorito else False
                    })

                case 2:
                    exibir_contatos(contatos=contatos)

                case 3:
                    while True:
                        try:
                            indice = int(input("Qual contato deseja editar? "))
                        
                        except ValueError:
                            print("valor inválido, por favor tente novamente.")
                        
                        except Exception:
                            print("Houve um erro inesperado na rotina de atualização.")
                            break

                        else:
                            contatos = editar_contato(indice=indice, contatos=contatos)
                            break

                case 4:                    
                    while True:
                        try:
                            indice = int(input("Qual contato deseja editar? "))
                        
                        except ValueError:
                            print("valor inválido, por favor tente novamente.")
                        
                        except Exception:
                            print("Houve um erro inesperado na rotina de atualização.")
                            break

                        else:
                            contatos = marcar_desmarcar_como_favorito(indice=indice, contatos=contatos)
                            break

                case 5:
                    exibir_contatos(contatos=contatos, apenas_favoritos=True)

                case 6:
                    while True:
                        try:
                            indice = int(input("Qual contato deseja remover? "))
                        
                        except ValueError:
                            print("valor inválido, por favor tente novamente.")
                        
                        except Exception:
                            print("Houve um erro inesperado na rotina de atualização.")
                            break

                        else:
                            contatos = remover_contato(indice=indice, contatos=contatos)
                            break

                case 7:
                    print("Encerrando a aplicação!")
                    break

        except ValueError as e:
            print("Operação inválida!")

        except Exception as e:
            print(str(e))
