# Solicita os dados do usuário
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura (em metros): "))
sexo = input("Digite seu sexo (M para masculino, F para feminino): ").strip().upper()

# Verifica o sexo e calcula o peso ideal
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")
    exit()

# Exibe o resultado
print(f"{nome}, seu peso ideal é: {peso_ideal:.2f} kg")

