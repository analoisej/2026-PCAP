'''
Problema: beecrowd |1046
Data: 2026.05.13
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: Ler a hora inicial e a hora final de um jogo.
#---ANALISE(LIAC)---
#Entrada: dois valores inteiros
#Saída: apresente a duração do jogo conforme exemplo abaixo
a, b = map(int, input().split())
duracao = b - a
if duracao <= 0:
    duracao +=24
print(f"O JOGO DUROU {duracao} HORA(S)")