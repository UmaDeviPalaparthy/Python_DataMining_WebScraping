# Assignment 2: Python Basics

* **INDIVIDUAL ASSIGNMENT**
* **Deadline**: Sept-27th 11:59PM
* **Value**: 100 points counted towards Homework category
* 
* **How to submit**: In your GitHub repository called *INF502* (same used for the Assignment 1) create a file called *"Assignment2.md"* with the following content:
  1. The problem's specification (as provided below in this file);
  2. A solution for each problem (in Python). Use the tag ```code``` to write the code along with the explanation.
  3. Explanation about the code (comments on variables and their meanings, explanation on why you used one or another approach, logical reasoning). The explanation can be either comments inside the code or text as a response to the problem in the markdown file.
  4. Create a folder called `code` and add the Python files (.py) with the solution. Link these files in your answer for each problem.
  Please remember to check if you invited me to see your repository (do so if you did not do for Assignment 1). I will evaluate the latest commit before 11:59PM (Sept-27th)

## Problems

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`.

The function returns the length of the hypotenuse assuming that `length_a` and `length_b` are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the `math` module might have useful functions to use.

For example:
```python
print(pythagoreanTheorem(2, 2))
2.8284271247461903
```
```python
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


```
```
Output 1:
Enter the length of one side - a : 4
Enter the length of another side - b : 4
Hypotenuse is :  5.656854249492381

Output 2:
Enter the length of one side - a : 10
Enter the length of another side - b : 10
Hypotenuse is :  14.142135623730951

Output 3:
Enter the length of one side - a : 2
Enter the length of another side - b : 2
Hypotenuse is :  2.8284271247461903

Output 4:
Enter the length of one side - a : 3
Enter the length of another side - b : 3
Hypotenuse is :  4.242640687119285
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.

For example:

```python
print(list_mangler([1, 2, 3, 4]))
[3, 4, 9, 8]
```
```python
# Custom method to  calculate and return list
def list_mangler(list_in):
    # new_list_in list variable to hold new values of the list
    new_list_in = list()
    for i in list_in:
        if i % 2 == 0:
            # if even - double the value in the list
            new_list_in.append(i ** 2)
        else:
            # if odd - triple the value in the list
            new_list_in.append(i ** 3)
    return new_list_in


# main method definition.
# input List values are hardcoded in this method
def main():
    list_in =[1,2,3,4,5]
    new_list_in = list_mangler(list_in)
    print(new_list_in)


# main method invocation
main()
```
```
input = [1,2,3,4,5]
output 1:
[1, 4, 27, 16, 125]

input = [6,7,8,9,10]
output 2:
[36, 343, 64, 729, 100]

input = [11,12,13,14,15]
output 3:
[1331, 144, 2197, 196, 3375]

input = [16,17,18,19,20]
output 4:
[256, 4913, 324, 6859, 400]

```

In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for `to_drop` equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

For example:

```
print(grade_calc([100, 90, 80, 95], 2)) # drops the 2 lowest grades (80 and 90)
'A'
```
```python
# Custom method to drop lowest two grades and calculate letter grade
def grade_calc(grades_in, to_drop):
    # For loop to iterate from 0 to to_drop value
    for x in range(to_drop):
        # variable to get the last lowest grade in the list
        # worst case scenario assigning the highest grade or a grade outside the scope
        low_grade = 10000
        for grade in grades_in:
            if grade < low_grade:
                # low_grade has the lowest grade in the list
                low_grade = grade
        # line to remove the lowest grade in the list
        grades_in.remove(low_grade)
    # print(grades_in)
    # avg variable to hold average of values from the list
    avg = 0
    # calculate average
    for grade in grades_in:
        avg += grade
    # if conditions to return the letter grade
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    elif avg >= 50:
        return 'F'


# main method to invoke the grade_calc method
# grade list and number of grades to drop are hardcoded
# prints the letter grade
def main():
    grades_in = [100, 90, 80, 95]
    to_drop = 2
    print(grade_calc(grades_in, to_drop))


# invocation of main method
main()

```
```
input:
grades_in = [100, 90, 80, 95]
to_drop = 2
output 1: A

input:
grades_in = [90, 80, 95, 85]
to_drop = 2
output 2: A


output 3:
output 4:

```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).


**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

For example:
```
print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))
[[2, 4, 6, 8], [1, 3, 5, 7, 9]]
print(odd_even_filter([3, 9, 43, 7]))
[[], [3, 9, 43, 7]]
print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56]))
[[98, 50, 90, 2, 56], [71, 39, 79, 5, 89]]
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).
