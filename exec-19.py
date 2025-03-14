# Ler dois valores distintos
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Verificar e exibir em ordem crescente
if valor1 < valor2:
    print(f"Valores em ordem crescente: {valor1}, {valor2}")
else:
    print(f"Valores em ordem crescente: {valor2}, {valor1}")
