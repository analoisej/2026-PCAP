'''
Problema: beecrowd |1012
Data: 2026.05.13
Estudante: Ana Loise Jovino Prado   
'''
#Objetivo: Escrever um programa que leia três valores com ponto flutuante de dupla precisão.
#---ANALISE(LIAC)---
#Entrada: tres valores com um digito após o ponto decimal
#Saída: deverá conter 5 linhas de dados.
valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
triangulo = (A * C) / 2
circulo = 3.14159 * (C ** 2)
trapezio = ((A + B) * C) / 2
quadrado = B ** 2
retangulo = A * B 
print(f"TRIANGULO: {triangulo:.3f}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")

