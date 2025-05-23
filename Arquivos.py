import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa(tarefas):
    nome = input("Digite o nome da tarefa: ")
    tarefas.append({"nome": nome, "concluida": False})
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(tarefas):
        status = "✔️" if tarefa["concluida"] else "❌"
        print(f"{i+1}. {tarefa['nome']} [{status}]")

def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    indice = int(input("Digite o número da tarefa concluída: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Índice inválido!")

def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    indice = int(input("Digite o número da tarefa a excluir: ")) - 1
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        print("Tarefa excluída!")
    else:
        print("Índice inválido!")

def menu():
    tarefas = carregar_tarefas()
    while True:
        print("==== MENU DE TAREFAS ====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Excluir tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            excluir_tarefa(tarefas)
        elif opcao == "5":
            salvar_tarefas(tarefas)
            print("Saindo e salvando... Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__== "__main__":
    menu()