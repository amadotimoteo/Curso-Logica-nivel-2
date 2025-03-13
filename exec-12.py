# Entrada de dados: Usuário insere as três notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

# Pesos das notas
peso1 = 2
peso2 = 3
peso3 = 5

# Cálculo da média ponderada
media_final = (n1 * peso1 + n2 * peso2 + n3 * peso3) / (peso1 + peso2 + peso3)

# Exibe o resultado formatado
print(f"\nA média final do aluno é: {media_final:.2f}")
