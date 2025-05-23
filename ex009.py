# while Loops
# You have a magic box that doubles the count of items you put, in every day.
# The given program takes the initial count of the items and the number of days as input.

# Task
# Write a program to calculate and output items' count on the last day.

# Sample Input
# 3
# 2

# Sample Output
# 12

# Explanation
# Day 1: 6 (3*2)
# Day 2: 12 (6*2)

items = int(input("Quantos items tem na caixa? "))
days = int(input("Quantos dias terão? "))
#your code goes here
counter = 0

while counter < days:
    items *= 2
    counter += 1
print(items)

