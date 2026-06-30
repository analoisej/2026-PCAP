# ===============================
# Disciplina : Pensamento Computacional, Algortitmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Impar"
# Arquivo    : par_impar.py
# Autor      : Ana Loise Jovino Prado
#Data        : 25/06/2026
# ===============================

import random 


def resultado(jogador, soma):
    if soma % 2 == 0:
        soma = "par"
    else:
        soma = "impar"

    if jogador == "par" and soma == "par":
        return "jogador"
    if jogador == "impar" and soma == "impar":
        return "jogador"
    return "soma"

opcoes = ["par", "impar"]
pontos_jogador = 0
pontos_maquina = 0 

for rodada in range (0, 5):
    print(f"--- Rodada, {rodada} ---")

    jogada_maquina = random.randint(0, 5)
    numero_jogador = int(input("Sua jogada (0, 5): "))
    jogada_jogador = input("Sua jogada: ").lower().strip()
    soma = jogada_maquina + numero_jogador

    if jogada_jogador not in opcoes:
        print("Inválida! Você perde a rodada!")
        pontos_maquina = pontos_maquina + 1
    else:
        quem = resultado(jogada_jogador, soma)
        if quem == "jogador":
            print("Você ganhou a rodada!")
            pontos_jogador = pontos_jogador + 1
        else:
            print("A maquina venceu a rodada!")
            pontos_maquina = pontos_maquina + 1

int("Placar final -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)        