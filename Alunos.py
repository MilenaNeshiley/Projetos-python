import json
import os

ARQUIVO = "alunos.json"

def carregar_alunos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_alunos(alunos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)

def adicionar_aluno(alunos):
    nome = input("Nome do aluno: ")
    idade = input("Idade: ")
    curso = input("Curso: ")
    aluno = {"nome": nome, "idade": idade, "curso": curso}
    alunos.append(aluno)
    print("Aluno adicionado com sucesso!")

def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for i, aluno in enumerate(alunos, 1):
        print(f"{i}. {aluno['nome']} - {aluno['idade']} anos - Curso: {aluno['curso']}")

def buscar_aluno(alunos):
    nome_busca = input("Digite o nome do aluno para buscar: ").lower()
    encontrados = [a for a in alunos if nome_busca in a['nome'].lower()]
    
    if encontrados:
        for aluno in encontrados:
            print(f"{aluno['nome']} - {aluno['idade']} anos - Curso: {aluno['curso']}")
    else:
        print("Nenhum aluno encontrado com esse nome.")

def menu():
    alunos = carregar_alunos()
    while True:
        print("=== MENU DE ALUNOS ===")
        print("1. Adicionar aluno")
        print("2. Listar alunos")
        print("3. Buscar aluno")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            buscar_aluno(alunos)
        elif opcao == "4":
            salvar_alunos(alunos)
            print("Saindo e salvando... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
        