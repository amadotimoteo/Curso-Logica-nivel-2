# Solicita os dados do usuário
salario_fixo = float(input("Digite o salário fixo do vendedor: ").replace(",", "."))
vendas = float(input("Digite o valor total das vendas efetuadas: ").replace(",", "."))

# Inicializa a comissão
comissao = 0

# Calcula a comissão corretamente
if vendas <= 1500:
    comissao = vendas * 0.03  # 3% sobre o total das vendas até R$ 1.500,00
else:
    comissao = (1500 * 0.03) + ((vendas - 1500) * 0.05)  # 3% sobre 1500 + 5% sobre o restante

# Calcula o salário total
salario_total = salario_fixo + comissao

# Exibe o resultado formatado corretamente
print(f"Salário total do vendedor: R$ {salario_total:.2f}")
