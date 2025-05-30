tab = [" "]*9

def print_tab():
    for i in range(0, 9, 3):
        print(tab[i:i+3])

def ganhou(jogador):
    for i in [0, 3, 6]:
        if tab[i] == tab[i+1] == tab[i+2] == jogador: return True
    for i in [0, 1, 2]:
        if tab[i] == tab[i+3] == tab[i+6] == jogador: return True
    if tab[0] == tab[4] == tab[8] == jogador: return True
    if tab[2] == tab[4] == tab[6] == jogador: return True
    return False

jogador = "X"
for _ in range(9):
    print_tab()
    pos = int(input(f"{jogador}, escolha posição (0-8): "))
    if tab[pos] == " ":
        tab[pos] = jogador
        if ganhou(jogador):
            print_tab()
            print(f"{jogador} venceu!")
            break
        jogador = "O" if jogador == "X" else "X"