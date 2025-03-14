# Solicita os dados do usuário
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura (em metros): ").replace(",", "."))  # Substitui vírgula por ponto
sexo = input("Digite seu sexo (M para masculino, F para feminino): ").strip().upper()

# Verifica se a altura está num intervalo realista (entre 0.5m e 2.5m)
if altura < 0.5 or altura > 2.5:
    print("Altura inválida! Digite a altura corretamente em metros (ex: 1.83).")
    exit()

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
