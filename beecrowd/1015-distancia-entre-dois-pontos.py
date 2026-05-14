'''
Problema: beecrowd | 1015
Data: 2026-05-14
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: ler os valores correspondentes aos eixos x e y de dois pontos quaisquer no plano.
#---ANALISE(LIAC)---
#Entrada: duas linhas de dados 
#Saída: imprimir o valor da distância segundo a fórmula fornecida.
import math
line1 = input().split()
x1 = float(line1[0])
y1 = float(line1[1])
line2 = input().split()
x2 = float(line2[0])
y2 = float(line2[1])
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("{:.4f}" .format(distancia))
