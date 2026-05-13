'''
Problema: beecrowd |1037
Data: 2026.05.13
Estudante: Ana Loise Jovino Prado   
'''
#Objetivo: Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
#Entrada: O programa deve ler um valor de ponto flutuante com duas casas decimais.
#Saida: O programa deve mostrar a mensagem "NOTAS:" 
valor = float(input())
if 0 <= valor <= 25:
    print("Intervalo [0,25]")
elif 25 < valor <= 50:
    print("Intervalo (25,50]")
elif 50 < valor <= 75:
    print("Intervalo (50,75]")
elif 75 < valor <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
