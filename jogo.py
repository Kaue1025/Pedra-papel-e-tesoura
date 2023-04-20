import random
from getpass import getpass
import time

pedra=1
papel=2
tesoura=3

def player_vs_player():
    
    while True:
        p1 = getpass("Jogador 1, escolha  1 pedra,  2 papel ou  3 tesoura: ")
        p2 = getpass("Jogador 2, escolha pedra, papel ou tesoura: ")
        print (p1)
        print(p2)
        if p1 == p2:
            print("Empate!")
        elif (p1 == "1" and p2 == "3") or (p1 == "2" and p2 == "1") or (p1 == "3" and p2 == "2"):
            print("Jogador 1 venceu!")
        else:
            print("Jogador 2 venceu!")
        play_again = input("Desejam jogar novamente? (s/n) ")
        if play_again.lower() != "s":
            break

def player_vs_cpu():
    
    while True:
        p1 = input("Jogador 1, escolha  1 pedra,  2 papel ou  3 tesoura: ")
        p2 = random.choice(["pedra", "papel", "tesoura"])
        print(f"A CPU escolheu: {p2}")
        if p1 == p2:
            print("Empate!")
        elif (p1 == "1" and p2 == "3") or (p1 == "2" and p2 == "1") or (p1 == "3" and p2 == "2"):
            print("Jogador 1 venceu!")
        else:
            print("A CPU venceu!")
        play_again = input("Desejam jogar novamente? (s/n) ")
        if play_again.lower() != "s":
            break

def cpu_vs_cpu():
   
    while True:
        p1 = random.choice(["pedra", "papel", "tesoura"])
        p2 = random.choice(["pedra", "papel", "tesoura"])
        print(f"A CPU 1 escolheu: {p1}")
        print(f"A CPU 2 escolheu: {p2}")
        if p1 == p2:
            print("Empate!")
        elif (p1 == "pedra" and p2 == "tesoura") or (p1 == "papel" and p2 == "pedra") or (p1 == "tesoura" and p2 == "papel"):
            print("A CPU 1 venceu!")
        else:
            print("A CPU 2 venceu!")
        play_again = input("Desejam jogar novamente? (s/n) ")
        if play_again.lower() != "s":
            break


    







print(" ")
print("******************************")
print("* Bem vindo ao PPT           *")
print("* Modos de jogo:             *")
print("* 1 -> Player vs CPU         *")
print("* 2 -> Player vs Player      *")
print("* 3 -> CPU vs CPU            *")
print("* 4 -> Sair                  *")
print("******************************")

while True:
        mode = input("Escolha o modo de jogo: ")
        if mode == "1":
            player_vs_cpu()
            break
        elif mode == "2":
            player_vs_player()
            break
        elif mode == "3":
            cpu_vs_cpu()
            break
        elif mode == "4":
            break
        else:
            print("Modo inválido, tente novamente!")
