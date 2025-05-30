def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcao = input("Converter (1) Celsius para Fahrenheit ou (2) Fahrenheit para Celsius? ")

if opcao == '1':
    c = float(input("Digite a temperatura em Celsius: "))
    print(f"{c}°C = {celsius_para_fahrenheit(c):.2f}°F")
elif opcao == '2':
    f = float(input("Digite a temperatura em Fahrenheit: "))
    print(f"{f}°F = {fahrenheit_para_celsius(f):.2f}°C")
else:
    print("Opção inválida.")