Par ou impar (aula 18)
# Variáveis
Linha 43 - pontos_jogador = pontos jogador + 1
Nas linhas acima tem o código para saber quem ganhou, e se o jogador ganhou a rodada é adicionado um ponto para o jogador 

Linha 46 - pontos_maquina = pontos_maquina + 1
É a mesma coisa dos pontos do jogador, se a maquina ganhar é adicionado pontos para a maquina 

Linha 49 - jogada_maquina = random.randint(0, 5)
Ele guarda a informação que seria o numero de jogadas (5).

# Operadores 
Linha 14 - if soma % 2 == 0:
Pega o valor que a pessoa coloca e divide por 2, porem esse sinal de divisao é usado quando queremos guardar o resto da divisão.

Linha 35 - pontos_maquina + 1 
ele pega a variavel "pontos_maquina" e adiciona 1 ponto pra essa variavel se a maquina vencer a rodada.

Linha 44 - pontos_jogador + 1 
Mesma ideia da linha 44, ele adiciona 1 ponto na variavel "pontos_jogador", se o jogador vencer a rodada.

# Estruturas de Repetição
Linha 29 - for rodada in range (0, 5):
Ele roda todos os códigos toda vez que alguem inicia o jogo.

# Estrutura de Condição 
Linha 43 - if quem == "jogador"
Se o jogador fizer um ponto, mostra no terminal que ele ganhou a rodada 

Linha 46 - else: 
Se não for nenhuma das opçoes acima, ou seja se o jodador nao pontuar é exibido no terminal que a maquina venceu a rodada.

Linha 20 - if jogador == "par" and soma == "par":
Se o jogador jogar par e a soma for par o jogador ganha a rodada.

# Sub-rotinas
Linha 14 - def resultado(jogador, soma):
eu estou definindo as jogadas possiveis para que o jogador possa vencer.

# Entrada
Linha 34 - numero_jogador = int(input("Sua jogada (0, 5): "))
Ele mostra o texto na tela e o jogador coloca sua jogada de 1 a 5, e o jogador pode colocar somente numero por conta do int.

Linha 35 - jogada_jogador = input("Sua jogada: ").lower().strip()
Mesma coisa da linha 34, o texto é mostrado no terminal e o jogador coloca seu palpite porem em texto.

# Saida
Linha 31 - print("Inválida! Você perde a rodada!")
Ele mostra somente o texto na tela e você não pode interagir.

Linha 43 - print("Você ganhou a rodada!")
Ele mostra somente o texto na tela e você não pode interagir.

linha 46 - print("A maquina venceu a rodada!")
Ele mostra somente o texto na tela e você não pode interagir.

Autor: Ana Loise Jovino Prado 