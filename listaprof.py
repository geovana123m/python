def mostrar_lista(lista):
    print("Lista:")
    for item in lista:
        print(item)
    print()

def adicionar_item(lista):
    novo_item = input("Digite uma fruta: ")
    lista.append(novo_item)
    print("Fruta adicionada com sucesso!")
    mostrar_lista(lista)

def excluir_item(lista):
    item_excluir = input("Digite a fruta você que deseja excluir: ")
    if item_excluir in lista:
        lista.remove(item_excluir)
        print("Fruta excluída com sucesso!")
    else:
        print("O item não está na lista.")
    mostrar_lista(lista)

def gravar_lista(lista):
    nome_arq = input("Digite o nome do arquivo")
    with open(nome_arq, "w") as arquivo:
        for item in lista:
            arquivo.write(item + "\n")
    print("Aquivo gravado com sucesso", nome_arq)

def carregar_arquivo(lista):
    nome_arq = input("digite o nome do arquivo para carregar a lista")
    try:
        with open(nome_arq, "r") as arquivo:
            lista.clear()
            for linha in arquivo:
                lista.append(linha.strip())
        print("Lista carregada com sucesso", nome_arq)
    except FileNotFoundError:
        print("Não encontrado")
    except Exception as e:
        print("Ocorreu um erro", e)

def ordenar_lista(lista):
    lista.sort(reverse = True)    
    print("Lista ordenada com sucesso")


def main():
    lista = []
    continuar = True

    while continuar:
        print("Escolha uma opção:")
        print("1. Adicionar uma fruta à lista")
        print("2. Excluir uma fruta da lista")
        print("3. Mostrar lista atual")
        print("4. Gravar lista")
        print("5. Carregar lista")
        print("6. Sair do programa")

        opcao = input("Opção: ")

        if opcao == '1':
            adicionar_item(lista)
        elif opcao == '2':
            excluir_item(lista)
        elif opcao == '3':
            mostrar_lista(lista)
        elif opcao == '4':
            gravar_lista(lista)
        elif opcao == '5':
            carregar_arquivo(lista)
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
