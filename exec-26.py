# Entrada de dados usando Seleção Aninhada
numero = float(input("Digite um número: "))

# Verificação utilizando seleção aninhada
if numero > 0:
    print("O número é positivo")
elif numero < 0:
    print("O número é negativo")
else:
    print("O número é zero")

# Entrada de dados usando Seleção Concatenada
numero = float(input("Digite um número: "))

# Verificação utilizando seleção concatenada
if numero >= 0:
    if numero == 0:
        print("O número é zero")
    else:
        print("O número é positivo")
else:
    print("O número é negativo")
