### Tanya Kadiyala
### CMSY-257-300
### Lab 1
### Problem 1: Sphere Calculations

# Imports the math library so Pi and square can be used #
import math

# Prints introduction statement and the user prompt for sphere radius #
print("Hello! Welcome to the Sphere Properties Calculator!")
user_input = input("Please Enter Your Sphere Radius: ")

# Since a user input is always a string, we have to convert it into a float #
radius = float(user_input)

# Store Pi in a variable for easy use #
PI = math.pi

# Calculates diameter, circumference, surface area, and volume #
diameter = radius * 2
circumference = (2 * PI)* radius
surface_area = 4 * PI * (radius ** 2)
volume = (4/3) * PI * (radius ** 2)

# Prints all the calculated values. The number values have to be converted
  
print("\nSphere Diamater: " + str(diameter))
print("Sphere Circumference: " + str(circumference))
print("Sphere Surface Area: " + str(surface_area))
print("Sphere Volume: " + str(volume))
