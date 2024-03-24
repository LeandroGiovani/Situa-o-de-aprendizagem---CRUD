from database import *


def menu():
    indiceMenu = int(input("""
-----------------------
O que deseja gerenciar?
[1] Times
[2] Jogadores
[3] Sair    
-----------------------
"""))
    if indiceMenu == 1:
        menuTimes()
    elif indiceMenu == 2:
        menuJogadores()
    elif indiceMenu == 3:
        print("\nSaindo...")
    else:
        print("Valor inserido inválio.")
        menu()


def menuTimes():
    indiceMenuTimes = int(input("""
-----------------------
[1] 
[2] 
[3] 
-----------------------
"""))
    # if indiceMenuTimes == 1:
    # elif indiceMenuTimes == 2:
    # elif indiceMenuTimes == 3:
    #     print("\nSaindo...")
    # else:
    #     print("Valor inserido inválio.")
    #     menuTimes()


def menuJogadores():
    indiceMenuJogadores = int(input("""
-----------------------
[1] 
[2] 
[3] 
-----------------------
"""))
    # if indiceMenuJogadores == 1:
    # elif indiceMenuJogadores == 2:
    # elif indiceMenuJogadores == 3:
    #     print("\nSaindo...")
    # else:
    #     print("Valor inserido inválio.")
    #     menuJogadores()