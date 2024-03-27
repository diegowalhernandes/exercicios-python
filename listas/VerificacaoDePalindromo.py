# Verificação de Palíndromo:
# Escreva uma função que verifica se uma palavra fornecida pelo usuário é um palíndromo (ou seja, se pode ser lida da mesma forma da esquerda para a direita e vice-versa).


def verifica_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    
    palavra_invertida = palavra[::-1]

    if palavra == palavra_invertida:
        return True
    else:
        return False
    
palavra = input("Digite uma palavra: ")

if verifica_palindromo(palavra):
    print(f'A  palavra {palavra} é um palindromo')
else:
    print(f'A palavra {palavra} não é um palindromo.')