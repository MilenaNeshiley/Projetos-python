valor = int(input("Valor a sacar: R$"))
notas = [100, 50, 20, 10, 5, 2]
for nota in notas:
    qtd = valor // nota
    valor %= nota
    if qtd:
        print(f"{qtd} nota(s) de R${nota}")