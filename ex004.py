## Exercícios 

### Casdatro de CPF

# Crie um programa para cadastro de CPF de clientes que receb o CPF em um input box apenas com numeros.
#Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"

cpf = input('Insira seu CPf:')
cpf = cpf.strip()
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Digite seu CPF corretamente e digite apenas números')