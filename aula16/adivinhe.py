# ===================================================
#Disciplina : Pensamento Computacioanal, Algortimos e Programação(PCAP)
#Projeto: Jogo "Adivinhe o Número"
#Arquivo: adivinhe.py
#Autor: Ana Loise Jovino Prado
#Data: 2026.05.18
#=====================================================
import random 
def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo) 
    acertou = False 
    
    while chances > 0 and not acertou:
        palpite = int(input("Seu palpite (1 a " + str(maximo) + "): "))

        if palpite == numero_secreto:
            print("Acertou!")
            