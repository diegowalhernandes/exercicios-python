# Exercício: Jogo da Adivinhação
# Crie um programa em Python que faça o seguinte:

# O programa escolhe aleatoriamente um número entre 1 e 100.
# O jogador tem que adivinhar o número.
# O programa deve dar dicas como "Muito alto!" ou "Muito baixo!" até o jogador acertar.
# Ao final, exiba o número de tentativas que o jogador usou.

import random

numero = random.randint(1, 100)
seu_num = []


while seu_num != numero:
    seu_num = int(input("Escolha um numero de 1 a 100: "))
    if numero < seu_num:
        print("Muito alto")
    elif numero > seu_num:
        print("Muito baixo")
    else:
        print(f"O numero escolhido foi {numero}, você acertou")