itens = ["Notebook", "Picanha", "Item3", "Item4", "Item5"]

def mostrar():
    print(f"Itens na lista: {itens}\n")

def cadastrar():
    resposta = input("Digite o item a se cadastrar: ")
    itens.append(resposta)
    print("Item adicionado.")

def excluir():
    mostrar()
    resposta = input("Fale o item que deseja deletar: ")
    itens.remove(resposta)
    print("Item deletado.")

def modificar():
    mostrar()
    resposta = input("Qual item deseja modificar?(maiusculo e minusculo conta.)")
    indice = itens.index(resposta)
    item_modificado = input("Qual o nome a ser dado ao item? ")
    itens[indice] = item_modificado
    print("Item modificado com sucesso.")

while True:
    print("Lista_compras")
    print("1 - Mostrar lista")
    print("2 - Cadastrar item na lista")
    print("3 - Excluir item da lista")
    print("4 - Modificar item da lista")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        mostrar()
    elif opcao == 2:
        cadastrar()
    elif opcao == 3:
        excluir()
    elif opcao == 4:
        modificar()
    elif opcao == 5:
        print("Saindo do sistema...")
        exit()
    else:
        print("Opção inválida, tente novamente...")