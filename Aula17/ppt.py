#============================
# Disciplina : Pensamento Computaciona, Algoritmos e Programação (PCAP)
# Projeto : Jogo "Pedra-Papel-Tesoura"
# Arquivo : ppt.py
# Autor : Ana Loise Jovino Prado 
# Data : 2026.06.18
#============================

import random 
def resultado(jogador, maquina):
    if jogador == maquina:
        return "empate"
    if jogador == "pedra" and maquina == "tesoura":
        return "jogador"
    if jogador == "pedra" and maquina == "lagarto":
        return "jogador"
    if jogador == "papel" and maquina == "pedra":
        return "jogador"
    if jogador == "papel" and maquina == "spock":
        return "jogador"
    if jogador == "tesoura" and maquina == "papel":
        return "jogador"
    if jogador == "tesoura" and maquina == "lagarto":
        return "jogador"
    if jogador == "pe" and maquina == "te":
        return "jogador"
    if jogador == "pe" and maquina ==  "la":
        return "jogador"
    if jogador == "pa" and maquina == "pe":
        return "jogador"
    if jogador == "pa" and maquina == "spo":
        return "jogador"
    if jogador == "te" and maquina == "pa":
        return "jogador"
    if jogador == "te" and maquina == "la":
        return "jogador"

    return "maquina"

opcoes = ["pedra", "papel", "tesoura", "pe", "pa", "te", "la", "spo"]
pontos_jogador = 0 
pontos_maquina = 0 
for rodada in range (1, 6):
    print("--- Rodada", rodada, "---")
    jogada_maquina = random.choice(opcoes)
    jogada_jogador = input("Sua jogada: ").lower().strip()
    if jogada_jogador not in opcoes:
        print("❌ Inválida! Você perde a rodada.")
        pontos_maquina = pontos_maquina + 1
    else:
        quem = resultado(jogada_jogador, jogada_maquina)
        if quem == "empate":
            print("🤝 Empate!")
        elif quem == "jogador":
            print("🎉 Você ganhou a rodada!")
            pontos_jogador = pontos_jogador + 1
        else:
            print("💀 A máquina ganhou a rodada!")
            pontos_maquina = pontos_maquina + 1

print("Placar final -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)
