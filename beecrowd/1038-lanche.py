'''
Problema: beecrowd |1038
Data: 2026.05.13
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: escrever um programa que leia o código de um item e a quantidade deste item
#---ANALISE(LIAC)---
#Entrada: dois valores inteiros 
#Saida: "Total: R$" seguido do valor a ser pago
linha = input().split()
codigo = int(linha[0])
quantidade = int(linha[1])
if codigo ==1:
    total = quantidade * 4.00
elif codigo == 2:
    total = quantidade * 4.50
elif codigo == 3: 
    total = quantidade * 5.00
elif codigo == 4:
    total = quantidade * 2.00
elif codigo == 5:
    total = quantidade * 1.50
print (f"Total: R$ {total:.2f}")
