# importing math library
import math


# Method to calculate hypotenuse, length_a, length_b are the other two sides of the triangle
# returns hypotenuse
def pythagoreanTheorem(length_a, length_b):
    length_c = math.sqrt(length_a ** 2 + length_b ** 2)
    return length_c


# main method to read user input for the two sides of the triangle.
def main():
    length_a = int(input("Enter the length of one side - a : "))
    length_b = int(input("Enter the length of another side - b : "))
    # length_c representing the hypotenuse
    length_c = pythagoreanTheorem(length_a, length_b)
    print("Hypotenuse is : ", length_c)


# invocation of main method.
main()
