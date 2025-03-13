# Solicita a entrada de dados ao usuário
salario_atual = float(input("Digite o salário atual do funcionário: "))
percentual_reajuste = float(input("Digite o percentual de reajuste (%): "))

# Calcula o novo salário
novo_salario = salario_atual + (salario_atual * (percentual_reajuste / 100))

# Exibe o resultado formatado
print(f"\nO novo salário após o reajuste será: R$ {novo_salario:.2f}")
