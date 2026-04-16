'''
Problema: beecrowd | 1008
Data: 2026.04.16
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: Ler número do funcionário, horas trabalhadas e valor por hora

#--- ANÁLISE (LIAC) ---
#Entrada: número do funcionário (inteiro), horas trabalhadas (inteiro), valor por hora (float)
#Processamento: calcular o salário (horas trabalhadas * valor por hora)
#Saída: imprimir o número do funcionário e o salário com 2 casas decimais

N = int(input())
H = int(input())
V = float(input())
SAL = H * V 
print(f"NUMBER = {N}")
print(f"SALARY = U$ {SAL:.2f}")