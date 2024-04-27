# Exercício: Verificação de Palíndromo

# Escreva um programa em Python que verifique se uma palavra é um palíndromo. Um palíndromo é uma palavra, frase, número ou outra sequência de caracteres que se lê da mesma forma para frente e para trás, desconsiderando os espaços em branco e diferenciação entre maiúsculas e minúsculas.

# Por exemplo:

# "ovo" é um palíndromo.
# "arara" é um palíndromo.
# "Ame a ema" é um palíndromo (desconsiderando espaços e diferenciação de maiúsculas/minúsculas).
# Seu programa deve solicitar ao usuário que entre com uma palavra e depois verificar se essa palavra é um palíndromo ou não. Em seguida, deve exibir uma mensagem indicando o resultado.

palavra = input("Escreva uma palavra: ").upper().replace(" ", "")
letras = []
for letra in palavra:
    letras.append(letra)
    
letras.reverse()
letras = ''.join(letras)

print(letras)

if palavra == letras:
    print("é palindromo")
else:
    print("não é palindromo")