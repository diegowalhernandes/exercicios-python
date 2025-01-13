
# Aqui vai um exercício divertido e desafiador para praticar lógica de programação em Python!

# Exercício: Número Palíndromo
# Descrição:
# Escreva um programa que solicite ao usuário um número inteiro e verifique se ele é um número palíndromo. Um número é considerado palíndromo se ele é o mesmo quando lido de trás para frente.

numero = input("Digite um número inteiro positivo: ")

if not numero.isdigit():
    print("Erro: o número deve ser positivo.")
else:
    if numero == numero[::-1]:
        print(f"O número {numero} é um palíndromo.")
    else:
        print(f"O número {numero} não é um palíndromo.")

