# Exercício: Contagem de Vogais
# Escreva um programa em Python que conte o número de vogais em uma palavra fornecida pelo usuário.
# Considere que as vogais são as letras 'a', 'e', 'i', 'o' e 'u', tanto em maiúsculas quanto em minúsculas.
# Seu programa deve solicitar ao usuário que insira uma palavra e, em seguida, contar quantas vogais estão presentes nessa palavra.
# Por fim, deve exibir o número total de vogais encontradas.

frase = input("Escreva uma frase: ").upper().replace(" ", "")
vogais = ['A', 'E', 'I', 'O', 'U']
letras_vogais = []

for letra in frase:
    if letra in vogais:
        letras_vogais.append(letra)


print("Frase original: ", frase)
print("Vogais encontradas: ",len(letras_vogais))

