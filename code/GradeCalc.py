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
