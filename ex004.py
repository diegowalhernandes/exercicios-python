# else Statement
# Write a program to control entrance to a club.
# Only people who are 18 or older are allowed to enter the club.
# The given program takes the age and the name of the person who tries to enter. Complete the program to output "Welcome" followed by the name of the person if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age.
try:
    age = int(input("Qual a sua idade? "))
    if age < 0:
        print("Idade inválida. Por favor, insira um número positivo.")
    else:
        name = input("Qual o seu nome? ")
        if age >= 18:
            print(f"Welcome {name} você tem {age} de idade e pode entrar")
        else:
            print(f"Sorry, {name}, você tem apenas {age} e não pode entrar")
except ValueError:
    print("Por favor, insira um número válido para a idade.")
