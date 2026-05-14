'''
Problema: beecrowd |1035
Data: 2026.05.13
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: ler 4 valores inteiros A,B,C e D
#---ANALISE(LIAC)---
#Entrada: quatro números inteiros
#Saida: mostre a respectiva mensagem após a validação dos valores 

A, B, C, D = map(int, input().split())
if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
    
