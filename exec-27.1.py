# Entrada de dados
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Inicializa o maior valor como o primeiro
maior = valor1

# Comparações encadeadas
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3

# Saída
print(f"O maior valor é: {maior}")
