'''
Problema: beecrowd | 1019
Data: 2026.04.19
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: Ler uma duração em segundos, e converte-la para horas, minutos e segundos.
# --- ANÁLISE ---
#Entrada: um numero inteiro N representado segundos toais.
#Processamento: extrair horas, minutose e segundos restantes por divisão inteira e módulo.
#Saída: no formato h:m:s (sem zeros á esquerda 0:9:16, não 00:09:16).

N = int(input())
h = N // 3600
N = N % 3600
m = N // 60
s = N % 60 
print(f"{h}:{m}:{s}")
