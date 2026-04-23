'''
Problema: beecrowd | 1050
Data: 2026.04.23
Estudante: Ana Loise Jovino Prado
'''
#Objetivo: Ler um codigo DDD e informar a qual cidade ele pertence 

#--- ANALISE ---
#Entrada: um numero ineitro representando o codigo DDD
#Saida: nome da cidade correspondente, u "DDD nao cadastrado" se nao encontrado
DDD = int(input())
if DDD == 61:
    print("Brasilia")
elif DDD == 71:
    print("Salvador")
elif DDD == 11:
    print("Sao Paulo")
elif DDD == 21:
    print("Rio de Janeiro")
elif DDD == 32:
    print("Juiz de Fora")
elif DDD == 19:
    print("Campinas")
elif DDD == 27:
    print("Vitoria")
elif DDD == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")