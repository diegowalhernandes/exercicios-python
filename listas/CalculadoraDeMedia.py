# Calculadora de Média:
# Escreva um programa que recebe uma lista de números do usuário e calcula a média desses números.

numeros = []

while len(numeros) < 5:    
    numero = int(input("Escreva um numero: "))
    numeros.append(numero)
media = sum(numeros) / len(numeros)

print("A media dos números é: ", media)