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
from modulos import ler_opcao

NOME_DO_DONO = "ANA LOISE"
OPCOES = ["0", "1"]

while True:
    titulo("FLIPERAMA DO " + NOME_DO_DONO)
    print("1 - Jogo Advinhe o Número")
    print("0 - Sair do FLiperama")
    linha()
    opcao = ler_opcao("Escolha uma opção", OPCOES)

    if opcao == "0":
        print("Até a Próxima!")
        break
    elif opcao == "1":
        jogar_adivinhe()
