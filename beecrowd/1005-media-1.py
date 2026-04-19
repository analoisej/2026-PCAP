'''
Problema: beecrowd | 1008
Data:2026.04.16
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: Ler duas notas com pesos diferentes, e calcular a média ponderada.
#Entrada: A entrada contém dois números de ponto flutuante, representando as notas e
#Processamento: média ponderada = (A * 3.5 + B * 7.5) / 11
#Saida: exibir no formato exato "MEDIA = valor" com 5 casas decimais
A = float(input())
B = float(input())
media = (A * 3.5 + B * 7.5) /11
print(f"MEDIA = {media:.5f}")

