   # ===============================
# Arquivo      : jogadores.py
# Disciplina   : 2026-PCAP
# Aula         : 22 
# Autor        : Ana Loise Jovino Prado
# Conceitos    : Registro como lista de campos, cadastro como lista de listas, cadastrar, listar, bucar, alterar, excluir, persistencia em arquivo .csv
# ===============================
from os.path import exists
from telas import titulo, linha 
from modulos import ler_opcao

ARQUIVO = "jogadores.csv"

def cadastrar(jogadores):
    titulo("NOVO JOGADOR")


    apelido = input("Apelido (sem espacos): ").strip().lower()
    nome = input("Nome completo: ").strip()


    novo = [apelido, nome, "0"]
    jogadores.append(novo)


    print("Jogador " + apelido + " cadastrado.")
    linha()

def listar(jogadores):
    titulo("JOGADORES CADASTRADOS")

    if len(jogadores) == 0:
        print("Nenhum jogador cadastrado ainda.")
    else:
        for jogador in jogadores:
            print(jogador[0] + " | " + jogador[1] + " | " + jogador[2] + " partidas")

    linha ()

def buscar(jogadores, apelido):
    for i in range(len(jogadores)):
        if jogadores[i] [0] == apelido:
            return i

    return -1

def alterar(jogadores):
    listar(jogadores)

    apelido = input("Apelido de quem vai mudar de nome: ").strip().lower()
    i = buscar(jogadores, apelido)

    if i == -1:
        print("Nao achei ninguem com esse apelido.")
    else:
        print("Nome attual: " + jogadores[i][1])
        jogadores[i][1] = input("Nome novo: ").strip()
        print("Pronto. Agora e " + jogadores[i][1] + ".")

    linha()

def excluir(jogadores):
    listar(jogadores)

    apelido = input("Apelido de quem vai ser excluido: ").strip().lower()
    i = buscar(jogadores, apelido)

    linha()

    if i == -1:
        print("Nao achei ninguem com esse apelido.")
        linha()
    else:
        print("Vou apagar o cadastro de " + jogadores[i][1] + ".")
        print("[1] Confirmar")
        print("[2] Deixar como esta")
        certeza = ler_opcao("Sua escolha", ["1", "2"])

        if certeza == "1":
            jogadores.pop(i)
            print("Cadastro apagado.")
        else:
            print("Nada foi apagado.")

linha()

def salvar_jogadores(jogadores):
    arquivo = open(ARQUIVO, "w")

    for jogador in jogadores:
        arquivo.write(jogador[0] + "," + jogador[1] + "," + jogador[2] + "\n")

        arquivo.close()

def carregar_jogadores():
    if not exists(ARQUIVO):
        return []

    arquivo = open(ARQUIVO, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    lido = []
    for linha_lida in linhas:
        pedacos = linha_lida.strip().split(",")
        lido.append(pedacos)

    return lido

def menu_jogadores(jogadores):
    while True:
        titulo("CADASTRO DE JOGADORES")
        print("[1] Cadastrar jogador")
        print("[2] Listar jogadores")
        print("[3] Alterar nome")
        print("[4] Excluir jogador")
        print("[0] Voltar ao fliperama")
        linha()

        opcao = ler_opcao("Sua escolha", ["0", "1", "2", "3", "4"])

        if opcao == "0":
            break 
        elif opcao == "1":
            cadastrar(jogadores)
        elif opcao == "2":
            listar(jogadores)
        elif opcao == "3":
            alterar(jogadores)
        else:
            excluir(jogadores)

jogadores = carregar_jogadores()
listar(jogadores)
menu_jogadores(jogadores)