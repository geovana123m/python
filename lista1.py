def lista():
    lista = ["gente grande", "esposa de mentirinha", "mistério no mediterrâneo"]

    while True:
        print("1 - Inserir novo item")
        print("2 - Excluir item")
        print("3 - Mostrar lista atual")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            novo_item = input("Digite o novo item: ")
            lista.append(novo_item)
            print("Item adicionado à lista!")
        
        elif opcao == "2":
            if lista:
                print("Lista atual:", lista)
                item_excluir = input("Digite o número do item que deseja excluir: ")
                if item_excluir.isdigit() and int(item_excluir) <= len(lista):
                    del lista[int(item_excluir)-1]
                    print("Item excluído!")
                else:
                    print("Opção inválida!")
            else:
                print("A lista está vazia!")
        
        elif opcao == "3":
            print("Lista atual:", lista)
        
        elif opcao == "4":
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    lista()
