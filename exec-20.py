# Ler a hora de início e a hora de fim do jogo
hora_inicio = int(input("Digite a hora de início do jogo (0-23): "))
hora_fim = int(input("Digite a hora de fim do jogo (0-23): "))

# Calcular a duração do jogo
if hora_fim > hora_inicio:
    duracao = hora_fim - hora_inicio
else:
    duracao = (24 - hora_inicio) + hora_fim  # Caso o jogo ultrapasse a meia-noite

# Exibir o resultado
print(f"A duração do jogo foi de {duracao} hora(s).")
