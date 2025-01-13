# Exercício: FizzBuzz
# Descrição: Escreva um programa que exiba os números de 1 a 100. Mas há duas condições especiais:

# Para múltiplos de 3, em vez do número, exiba "Fizz".
# Para múltiplos de 5, em vez do número, exiba "Buzz".
# Para números que são múltiplos de 3 e 5, exiba "FizzBuzz".

for numero in range (1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)