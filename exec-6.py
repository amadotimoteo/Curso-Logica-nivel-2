# Solicita ao usuário que insira sua idade em anos, meses e dias
anos = int(input("Digite sua idade em anos: "))  # Converte o valor inserido para inteiro
meses = int(input("Digite a quantidade de meses: "))  # Converte o valor inserido para inteiro
dias = int(input("Digite a quantidade de dias: "))  # Converte o valor inserido para inteiro

# Cálculo da idade total em dias
idade_em_dias = (anos * 365) + (meses * 30) + dias  # Converte anos e meses para dias e soma tudo

# Exibe o resultado final
print(f"Sua idade em dias é: {idade_em_dias}")  # Mostra a idade total em dias para o usuário
