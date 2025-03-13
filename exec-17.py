# Ler o ano atual e o ano de nascimento
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcular a idade
idade = ano_atual - ano_nascimento

# Verificar se pode votar
if idade >= 16:
    print("Você PODE votar este ano.")
else:
    print("Você NÃO PODE votar este ano.")
