

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

code for [Pythagorean.py](code/Pythagorean.py)

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
            new_list_in.append(i * 2)
        else:
            # if odd - triple the value in the list
            new_list_in.append(i * 3)
    return new_list_in


# main method definition.
# input List values are hardcoded in this method
def main():
    print("Enter the list values as space separated values")
    # read input from user as space separated values
    list_str = input()
    # split the input by space
    list1 = list_str.split(" ")
    # empty list to hold the values
    list_in = list()
    # for loop to convert the string values in list to int values
    for i in list1:
        list_in.append(int(i))
    # list_in =[1,2,3,4,5]
    new_list_in = list_mangler(list_in)
    print(new_list_in)


# main method invocation
main()
```
```

output 1:
Enter the list values as space separated values
1 2 3 4 5
[3, 4, 9, 8, 15]

output 2:
Enter the list values as space separated values
6 7 8 9 10
[12, 21, 16, 27, 20]

output 3:
Enter the list values as space separated values
11 12 13 14 15
[33, 24, 39, 28, 45]

output 4:
Enter the list values as space separated values
16 17 18 19 20
[32, 51, 36, 57, 40]

```

In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

code for [Listmangler.py](code/Listmangler.py)

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

    avg = avg/len(grades_in)
    # print(avg)
    # if conditions to return the letter grade
    if avg >= 90.0:
        return 'A'
    elif avg >= 80.0:
        return 'B'
    elif avg >= 70.0:
        return 'C'
    elif avg >= 60.0:
        return 'D'
    elif avg < 60.0:
        return 'F'


# main method to invoke the grade_calc method
# grade list and number of grades to drop are hardcoded
# prints the letter grade
def main():
    print("Enter the list values as space separated values")
    # read input from user as space separated values
    list_str = input()
    # split the input by space
    list1 = list_str.split(" ")
    # empty list to hold the values
    grades_in = list()
    # for loop to convert the string values in list to int values
    for i in list1:
        grades_in.append(int(i))
    # grades_in = [80, 60, 70, 75]
    to_drop = int(input("Enter number of grades to be dropped: "))
    # to_drop = 2
    print(grade_calc(grades_in, to_drop))


# invocation of main method
main()

```
```
output 1: 
Enter the list values as space separated values
100 90 95 80
Enter number of grades to be dropped: 2
A

output 2: 
Enter the list values as space separated values
90 80 85 75
Enter number of grades to be dropped: 2
B


output 3:
Enter the list values as space separated values
80 75 70 65
Enter number of grades to be dropped: 2
C

output 4:
Enter the list values as space separated values
70 65 60 50
Enter number of grades to be dropped: 2
D

```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

code for [GradeCalc.py](code/GradeCalc.py)

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
```python
# custom method to filter the list into two
def odd_even_filter(numbers):
    # empty list to hold even values 
    list_even = list()
    # empty list to hold odd values 
    list_odd = list()
    # empty list to hold both even and odd values 
    list_full = list()
    # for loop to iterate over the values in list - numbers
    for x in numbers:
        # if the value is even append to even list else append to odd list
        if x % 2 == 0:
            list_even.append(x)
        else:
            list_odd.append(x)
    # append both even and odd list
    list_full.append(list_even)
    list_full.append(list_odd)
    # return full list with both the values separated
    return list_full


def main():
    print("Enter the list values as space separated values")
    # read input from user as space separated values
    list_str = input()
    # split the input by space
    list1 = list_str.split(" ")
    # empty list to hold the values
    odd_even_list = list()
    # for loop to convert the string values in list to int values
    for i in list1:
        odd_even_list.append(int(i))
    # print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(odd_even_filter(odd_even_list))


main()

```
```
output 1:
Enter the list values as space separated values
1 2 3 4 5 6 7 8 9
[[2, 4, 6, 8], [1, 3, 5, 7, 9]]

output 2:
Enter the list values as space separated values
11 12 13 14 15 16 17 18
[[12, 14, 16, 18], [11, 13, 15, 17]]

output 3:
Enter the list values as space separated values
21 13 34 35 87 98
[[34, 98], [21, 13, 35, 87]]

output 4:
Enter the list values as space separated values
413 345 12 35 15 26 20 40
[[12, 26, 20, 40], [413, 345, 35, 15]]
```
In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

code for [OddEvenFilter.py](code/OddEvenFilter.py)
