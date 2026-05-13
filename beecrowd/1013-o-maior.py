'''
Problema: beecrowd |1013
Data: 2026.05.13
Estudante: Ana Loise Jovino Prado   
'''

#Objetivo:Fazer um programa que leia três valores e apresente o maior dos três valores lidos.
#---ANALISE(liac)---
#Entrada: três valores inteiros 
#Saida: imprimir o maior dos três valores seguido da mensagem "eh o maior"

a, b, c = map(int, input().split())
maiorAB = (a + b + abs(a - b)) // 2
maiorABC = (maiorAB + c + abs(maiorAB - c)) // 2
print(f"{maiorABC} eh o maior")