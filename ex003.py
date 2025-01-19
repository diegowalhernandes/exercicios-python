# if Statements

# Write a programa that checks if the water is boiling.
# Take the integer temperature in Celsius as input and output "Boiling" if the temperature is above or equal to 100

# Sample input
# 105
# Sample Output
# Boiling

temp = int(input("Qual a temperatura? "))
if temp >= 100:
    print("Boiling")
else:
    print("No Boiling")