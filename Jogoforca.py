palavra = "python"
letras_certas = []
tentativas = 6

while tentativas > 0:
    display = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
    print(f"Palavra: {display}")
    if '_' not in display:
        print("Você venceu!")
        break

    letra = input("Chute uma letra: ").lower()
    if letra in palavra:
        letras_certas.append(letra)
    else:
        tentativas -= 1
        print(f"Errou! Tentativas restantes: {tentativas}")