# Entrada de dados
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_hora = float(input("Digite o salário por hora: "))

# Definições
horas_semanais = 40
semanas_no_mes = 4
horas_mensais = horas_semanais * semanas_no_mes  # Total de horas regulares no mês
salario_total = 0

# Cálculo do salário
if horas_trabalhadas > horas_mensais:
    horas_extras = horas_trabalhadas - horas_mensais
    valor_hora_extra = salario_hora * 1.5  # Acréscimo de 50%
    salario_total = (horas_mensais * salario_hora) + (horas_extras * valor_hora_extra)
else:
    salario_total = horas_trabalhadas * salario_hora

# Saída do resultado
print(f"O salário total do funcionário é: R$ {salario_total:.2f}")
