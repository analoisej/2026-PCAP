# ===================================
# Arquivo:      main.py
# Disciplina:   2026-PCAP
# Aula :        20
# Autor:        Ana Loise Jovino Prado
# Data:         2026.08.04
# Conceitos:    
# ===================================

# Importat funções de arquivos
from telas import titulo, linha 
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores
from parimpar import jogarpar_impar

NOME_DOS_JOGOS = ["Advinhe o Numero", "Pedra-Papel-Tesoura", "Par ou Impar"]
vezes_jogado =  carregar_placar()
jogadores = carregar_jogadores()

def mostrar_placar():
    titulo("PLACAR")
    for i in range(3):
        print(NOME_DOS_JOGOS[i] + ": " + str(vezes_jogado[i]) + "x")


NOME_DO_DONO = "ANA LOISE"
OPCOES = ["0", "1", "2", "3", "4"]

while True:
    titulo("FLIPERAMA DA " + NOME_DO_DONO)
    print("[1]  Advinhe o Número")
    print("[2] Pedra-Papel-Tesoura")
    print("[3] Par ou Impar")
    print("[4] Jogadores")
    print("[0] Sair do Fliperama")
    linha()
    opcao = ler_opcao("Escolha uma opção", OPCOES)

    if opcao == "0":
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        titulo("Até a Próxima!")
        break

    if opcao == "4":
        menu_jogadores(jogadores)
    else:
        indice = int(opcao) - 1 
        vezes_jogado[indice] = vezes_jogado[indice] + 1

        if opcao == "1":
            jogar_adivinhe()
        elif opcao == "2":
            jogar_ppt()
        elif opcao == "3":
            jogarpar_impar()


input("Pressione Enter para volar ao menu... ")
    