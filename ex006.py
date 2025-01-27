# Lists
# Imagine a vending machine that sells fruits. Each fruit has its own number, starting from 0.
# Write a program for the vending machine, which will take n numeber as input from the customer and return the fruit with that index.IndexError
# if n< 0 or n>7 (the index of last fruit), the program outputs "Wrong number".PendingDeprecationWarning

# Sample Input:
# 2
# Sample Output:
# Banana

fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"]
num = int(input())
if num < 0 or num > 7:
    print("Wrong number")
if num == 0:
    print("apple")
if num == 1:
    print("cherry")
if num == 2:
    print("banana")
if num == 3:
    print("kiwi")
if num == 4:
    print("lemon")
if num == 5:
    print("pear")
if num == 6:
    print("peach")
if num == 7:
    print("avocado")