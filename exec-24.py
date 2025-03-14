# Solicita os dados do cliente
numero_conta = input("Digite o número da conta do cliente: ")
saldo = float(input("Digite o saldo atual: ").replace(",", "."))
debito = float(input("Digite o valor do débito: ").replace(",", "."))
credito = float(input("Digite o valor do crédito: ").replace(",", "."))

# Calcula o saldo atual
saldo_atual = saldo - debito + credito

# Exibe o saldo atualizado
print(f"\nNúmero da Conta: {numero_conta}")
print(f"Saldo Atual: R$ {saldo_atual:.2f}")

# Verifica se o saldo é positivo ou negativo
if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
