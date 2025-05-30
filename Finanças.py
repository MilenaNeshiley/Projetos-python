saldo = 0
while True:
    print(f"Saldo: R${saldo}")
    acao = input("Digite (add/gastar/sair): ")

    if acao == "add":
        valor = float(input("Valor a adicionar: "))
        saldo += valor
    elif acao == "gastar":
        valor = float(input("Valor a gastar: "))
        saldo -= valor
    elif acao == "sair":
        break