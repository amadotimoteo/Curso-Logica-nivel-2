# Solicita a entrada do custo de fábrica ao usuário e trata o separador de milhar
custo_fabrica = float(input("Digite o custo de fábrica do carro: ").replace(".", ""))

# Definição das porcentagens
percentual_distribuidor = 28 / 100  # 28%
percentual_impostos = 45 / 100  # 45%

# Calcula os valores do distribuidor e dos impostos
valor_distribuidor = custo_fabrica * percentual_distribuidor
valor_impostos = custo_fabrica * percentual_impostos

# Calcula o custo final ao consumidor
custo_final = custo_fabrica + valor_distribuidor + valor_impostos

# Exibe o resultado formatado
print(f"\nO custo final do carro ao consumidor será: R$ {custo_final:,.2f}")

# replace(".", "") → Remove os pontos digitados pelo usuário antes da conversão, permitindo que ele escreva 250.000 sem erro.
Formatação na saída :,.2f → Agora o valor final será exibido com vírgula como separador de milhar e duas casas decimais.
