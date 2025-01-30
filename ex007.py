# Given a list of numbers, output "bingo" if it contains the input number.

items = [42, 88, 721, 12, 43, 45, 908]
num = int(input("Enter a number: "))

if num in items:
    print("bingo")
else:
    print("try another number")