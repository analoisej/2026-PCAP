'''
Problema: beecrowd |1017
Data: 2026.05.13
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: descobrir a quantidade de litros de combustivel gastos em uma viagem
#---ANALISE(LIAC)---
#Entrada: dois inteiros
#Saída: imprimir a quantidade de litros necessaria para realizar a vaiagem 
tempo = int(input())
velocidade = int(input())
litros = (tempo * velocidade) / 12
print(f"{litros:.3f}")
