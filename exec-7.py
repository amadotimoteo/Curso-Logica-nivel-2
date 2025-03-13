# Solicita a entrada de dados ao usuário
total_eleitores = int(input("Digite o número total de eleitores: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

# Verifica se os votos são compatíveis com o total de eleitores
if votos_brancos + votos_nulos + votos_validos > total_eleitores:
    print("Erro: A soma dos votos excede o número total de eleitores.")
else:
    # Calcula os percentuais
    percentual_brancos = (votos_brancos / total_eleitores) * 100
    percentual_nulos = (votos_nulos / total_eleitores) * 100
    percentual_validos = (votos_validos / total_eleitores) * 100

    # Exibe os resultados formatados
    print(f"\nPercentual de votos brancos: {percentual_brancos:.2f}%")
    print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
    print(f"Percentual de votos válidos: {percentual_validos:.2f}%")
