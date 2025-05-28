# Two friends want to play backgammon, but have lost the dice.
# Create a program to replace the dice. When the program is run, it should roll the dice and output the result of each die.

# Hint
# Use random.randint() function to generate random values in the range of 1 to 6 for each dice.

import random
random.seed(int(input()))

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print(dice1)
print(dice2)