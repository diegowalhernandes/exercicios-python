import random

# Número secreto
numero = random.randint(1, 100)
cont = 0

print("Bem-vindo ao Jogo da Adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 100.")

while True:
    try:
        # Entrada do jogador
        seu_num = int(input("Escolha um número de 1 a 100: "))
        cont += 1

        # Dicas
        if seu_num < 1 or seu_num > 100:
            print("Por favor, escolha um número dentro do intervalo!")
        elif seu_num < numero:
            print("Muito baixo!")
        elif seu_num > numero:
            print("Muito alto!")
        else:
            print(f"Parabéns! O número escolhido foi {numero}. Você acertou em {cont} tentativas.")
            break  # Sai do loop ao acertar
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
