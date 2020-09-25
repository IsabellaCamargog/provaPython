Valor1 = float(input("Informe o primeiro valor"))
Valor2 = float(input("Informe o segundo valor"))
operacao = input("Qual a operação que deseja realizar (soma, subtração, multiplicação, divisão, resto divisão)").lower()
if operacao == "soma":
    print(Valor1 + Valor2)
elif operacao == "subtração":
    print(Valor1 - Valor2)
elif operacao == "multiplicação":
    print(Valor1 * Valor2)
elif operacao == "divisão":
    print(Valor1 / Valor2)
elif operacao == "resto divisão":
    print(Valor1 % Valor2)
else:
    print("Operação inválida, tente novamente")