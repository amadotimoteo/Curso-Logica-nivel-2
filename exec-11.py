# Entrada de dados: Usuário insere a temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Cálculo da conversão para Celsius
celsius = (fahrenheit - 32) / 1.8

# Exibe o resultado formatado
print(f"\nA temperatura em graus Celsius é: {celsius:.2f}°C")

