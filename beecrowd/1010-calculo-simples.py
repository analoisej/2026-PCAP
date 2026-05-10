'''
Problema: beecrowd | 1010
Data: 2026.05.10
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: Ler o código de um produto, a quantidade de produtos e o valor unitário de cada produto.
#---ANALISE(LIAC)---
#Entrada: O programa deve ler o código de um produto, a quantidade de produtos e o valor unitário de cada produto.
#Saida: O programa deve calcular e mostrar o valor a ser pago, com duas casas decimais.
cod1, qtd1, val1 = input().split()
qtd1 = int(qtd1)
val1 = float(val1)
cod2, qtd2, val2 = input().split()
qtd2 = int(qtd2)
val2 = float(val2)
total = (qtd1 * val1) + (qtd2 * val2)
print(f"VALOR A PAGAR: R$ {total:.2f}")