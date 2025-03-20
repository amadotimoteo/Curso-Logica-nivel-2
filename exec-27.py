# Entrada de dados
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Verificação do maior valor
if valor1 > valor2 and valor1 > valor3:
    maior = valor1
elif valor2 > valor1 and valor2 > valor3:
    maior = valor2
else:
    maior = valor3

# Saída
print(f"O maior valor é: {maior}")
