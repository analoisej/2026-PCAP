# ===================================
# Arquivo:      parimpar.py
# Disciplina:   2026-PCAP
# Aula :        20
# Autor:        Ana Loise Jovino Prado
# Data:         2026.09.01
# Conceitos:    
# ===================================
from random import randint
from telas import titulo, linha
from modulos import ler_opcao, ler_numero
import random

JOGADAS1 = ("Par", "Impar")
JOGADAS2 = ("0, 1, 2, 3, 4, 5")

def opcoes():
    print("Veja as opçes e escolha uma delas: ")
    print("(1) Par")
    print("(2) Impar")

def opcoes1():
    print("Escolha um valor de 0 a 5")

def somapar(numero_maquina, numero_jogador):
    soma = (numero_maquina + numero_jogador) % 2 
    if soma == 0:
        return "par"
    else:
        return "impar"

def placar(pontos_maquina, pontos_jogador):
    print("Quem fizer 2 pontos primeiro ganha")
    print("O placar está asssim:")
    print(f"Você tem {pontos_jogador} pontos")
    print(f"A máquina tem {pontos_maquina} pontos")

def jogarpar_impar():
    titulo("Par ou Ímpar")
    pontos_jogador = 0 
    pontos_maquina = 0

    while pontos_jogador < 2 and pontos_maquina < 2:
        opcoes()
        jogadores1 = int(ler_opcao("Sua jogada: ", ["1", "2"]))
        if jogadores1 == 1:
            maquina1 = 0 
        else: 
            maquina1 = 1

        opcoes1()
        jogadores2 = int(ler_opcao("Sua jogada: ", ["0", "1", "2", "3", "4", "5"]))
        maquina2 = randint(0, 5)
        solucao1 = somapar(jogadores2, maquina2)
        if solucao1 == "par" and jogadores1 == 0:
            pontos_jogador += 1
            placar(pontos_maquina, pontos_jogador)
        elif solucao1 == "impar" and jogadores1 == 1:
            pontos_jogador += 1
            placar(pontos_maquina, pontos_jogador)
        else:
            pontos_maquina += 1
            placar(pontos_maquina, pontos_jogador)
        
        linha()
    if pontos_jogador == 2:
        print("Você ganhou o jogo!")
    else:
        print("A maquina ganhou o jogo")


