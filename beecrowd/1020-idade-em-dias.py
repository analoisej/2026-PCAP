'''
Problema: beecowd | 1020 - Idade em Dias
Data 2026.04.23
Estudante: Ana Loise Jovino 
'''
#Objetivo: Leia um valor inteiro correspondente á idade de uma pessoa e informe-a em anos, meses e dias.
#--- ANALISE (LIAC) ---
#Entrada: um valor inteiro correspondente á idade de uma pessoa
#Saida: imprimir a idade em anos, meses e dias

idade_em_dias = int(input())
anos = idade_em_dias // 365
resto_anos = idade_em_dias % 365
meses = resto_anos // 30
dias = resto_anos % 30
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
