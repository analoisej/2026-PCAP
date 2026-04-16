'''
Problema: beecrowd | 1009 
Data: 2026.04.16
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: Ler nome, salario fixo e total de veendas

#--- ANÁLISE (LIAC) ---
#Entrada: nome (texto), salario fixo (float), vendas (float)
#Processamento: calcular o salário total (salário fixo + 15% das vendas)
#Saída: imprimir o salário total com 2 casas decimais

n = input()
s = float(input())
v = float(input())
c = v * 0.15
t = s + c
print(f"TOTAL = R$ {t:.2f}")