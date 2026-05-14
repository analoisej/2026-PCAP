'''
Problema: beecrowd |1038
Data: 2026.05.13
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: escrever um programa que leia o código de um item e a quantidade deste item
#---ANALISE(LIAC)---
#Entrada: dois valores inteiros 
#Saida: "Total: R$" seguido do valor a ser pago
line = input().split()
cod = int(line[0])
qtd = int(line[1])
precos = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}
total = precos [cod] * qtd
print(f"Total: R$ {total:.2f}")
