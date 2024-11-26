"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

x = float(input("Enter a side "))
y = float(input("enter another side "))

n = input("Is one of your numbers the hypotneuse (yes or no) ")

X = x**2
Y = y**2

if "no" in n:
    Z = X + Y
elif "yes" in n:
    if x > y:
        Z = X - Y
    elif y > x:
        Z = Y - X
    elif y == X:
        Z = Y - X
else:
    print("yes or no please")

import math

z = math.sqrt(Z)

print(f"your missing side has the value {z}")