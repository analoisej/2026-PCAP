'''
Problema: beecrowd | 1044
Data: 2026.05.10
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: verificar se dois inteiros são multiplos entre si  
#--- ANALISE (LIAC) ---
#Entrada: dois numeros inteiros
#Saída: "Sao Multiplos" ou "Nao sao Multiplos"

A, B = input().split()
A = int(A)
B = int(B)
if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A
if maior % menor == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")