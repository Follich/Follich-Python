import random
import time

print("=+" * 20)
print("         Pedra - Papel - Tesoura")
print("=+" * 20)

arms = ["Pedra", "Papel", "Tesoura"]
pc = random.randint(1, 3)

print("Escolha um deles \nPedra[1]\nPapel[2]\nTesoura[3]")
user = int(input("User: "))

time.sleep(1)
print("Jo")
time.sleep(1)
print("Ken")
time.sleep(1)
print("Po")
time.sleep(1)

print("=+" * 20)
print(f"O jogador jogou {arms[user - 1]}")
print(f"O computador jogou {arms[pc - 1]}")
print("=+" * 20)

if user == 1:
    if pc == 2:
        print("Jogador perdeu")
        print("Fim de jogo")
    elif pc == 3:
        print("O jogador ganhou")
        print("Fim de jogo")
    else:
        print("Empate")
        print("Fim de jogo")

if user == 2:
    if pc == 3:
        print("Jogador perdeu")
        print("Fim de jogo")
    elif pc == 1:
        print("O jogador ganhou")
        print("Fim de jogo")
    else:
        print("Empate")
        print("Fim de jogo")

if user == 3:
    if pc == 1:
        print("Jogador perdeu")
        print("Fim de jogo")
    elif pc == 2:
        print("O jogador ganhou")
        print("Fim de jogo")
    else:
        print("Empate")
        print("Fim de jogo")
