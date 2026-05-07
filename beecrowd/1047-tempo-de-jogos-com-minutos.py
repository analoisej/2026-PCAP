'''
Problema: beecrowd | 1047
Data: 2026.05.07
Estudante: Ana Loise Jovino Prado
'''
 #---ANALISE(LIAC)---
 #Entrada: 4 inteiros na mesma linha, representando a hora de início e a hora de término de um jogo.
 #Saída: Imprimir a duração do jogo, considerando o cenário de que o jogo pode iniciar em um dia e terminar no outro.

hi, mi, hf, mf = map(int, input().split())
tim = (hi * 60) + mi
tfm = (hf * 60) + mf
if tim > tfm:
    ttm = (tfm - tim) + (24 * 60)
else:
    ttm = tfm - tim
if ttm == 0:
    ttm = 24 * 60
print(f"O JOGO DUROU {ttm // 60} HORA(S) E {ttm % 60} MINUTO(S)")
