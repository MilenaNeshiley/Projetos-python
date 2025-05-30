def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    return cpf != cpf[0] * 11

cpf_input = input("Digite o CPF: ")
print("Válido" if validar_cpf(cpf_input) else "Inválido")