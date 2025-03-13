# Entrada do usuário
quantidade = int(input("Digite a quantidade de maçãs compradas: "))

# Verifica o preço com base na quantidade comprada
if quantidade < 12:
    preco_por_maca = 1.30
else:
    preco_por_maca = 1.00

# Calcula o custo total
custo_total = quantidade * preco_por_maca

# Exibe o resultado
print(f"O custo total da compra é: R$ {custo_total:.2f}")
