# Functions Arguments

# You are given a program with two inputs one as password and the second one as password repeat
# complete and call the given function to output "Correct" if password and repeat are equal, and output "wrong"
# if they are not

# sample input
# nfs1598
# nfs1598

# sample output
# Correct

# Dont forget add arguments when you call the fuction

password = input()
repeat = input()
def validate(text1, text2):
    if text1 == text2:
        print("Correct")
    else:
        print("Wrong")
validate(password, repeat)