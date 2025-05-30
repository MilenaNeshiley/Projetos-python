agenda = {}

def adicionar_contato(nome, telefone):
    agenda[nome] = telefone

def mostrar_contatos():
    for nome, telefone in agenda.items():
        print(f"{nome}: {telefone}")

while True:
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        adicionar_contato(nome, telefone)
    elif opcao == '2':
        mostrar_contatos()
    elif opcao == '3':
        break
    else:
        print("Opção inválida")