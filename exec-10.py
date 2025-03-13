# Entrada de dados (removendo pontos para evitar erro)
salario_fixo = float(input("Digite o salário fixo do vendedor: ").replace(".", ""))
num_carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_total_vendas = float(input("Digite o valor total das vendas: ").replace(".", ""))

# Definição dos valores fixos
comissao_por_carro = 700.00  # Comissão fixa por carro vendido
percentual_sobre_vendas = 5 / 100  # 5% sobre o valor total das vendas

# Cálculo do salário final
comissao_fixa = num_carros_vendidos * comissao_por_carro  # Comissão fixa total
comissao_vendas = valor_total_vendas * percentual_sobre_vendas  # Comissão sobre vendas

salario_final = salario_fixo + comissao_fixa + comissao_vendas  # Salário total

# Exibe o resultado formatado com separador de milhar e duas casas decimais
print(f"\nO salário final do vendedor será: R$ {salario_final:,.2f}")

# replace(".", "") → Remove os pontos digitados pelo usuário antes da conversão para float, permitindo que ele escreva 2.000 sem erro.
Exibe o salário final com separador de milhar usando :,.2f.
# Isso permite com que o usuario possa digitar usando o "." exemplo "2.000 inves de 2000) 
