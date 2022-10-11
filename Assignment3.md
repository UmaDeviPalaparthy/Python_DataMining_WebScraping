# Assignment 3: Python Basics

* **INDIVIDUAL ASSIGNMENT**
* **Deadline**: Oct-11th 11:59PM
* **Value**: 100 points counted towards Homework category

**How to submit**: In your GitHub repository called *INF502* (same used for the HW assignments 1 and 2), create a file called *"Assignment3.md"* with the following content:
  1. The problem's specification (as provided below in this file);
  2. A brief textual explanation of you approach to solve the problem. Use the tag ```code``` if you need to show snippets of code along with the explanation (not required though).
  3. A link to the file with the solution. Add the `.py` file to the `code` folder (create one if you don't have it already!).
  
  Please remember to check if you invited me to see your repository (do so if you did not do for previous assignments). I will evaluate the latest commit before 11:59PM (Oct-11th)

## Problem 1: Wallets

Write a Python program that request a user to provide numbers representing the value in cash for different wallets. Your program should store these values in a list. The user should be able to add as many values as they want. One example of a filled `wallets` list (in this example, with 5 wallets) would be:

```
print(wallets)

Output: [1023, 984, 192, 1842, 12]
```

After the user adds the values for the wallets, your application should provide the following information:
* The fattest wallet has `$value` in it.
* The skinniest wallet has `$value` in it.
* All together, these wallets have `$value` in them.
* All together, the total value of these wallets is worth `$value` dimes.

Please try to think about different functions to complete your work.

```python
# Calculates total of a given input values
def calculate_sum(input_list):
    total = 0
    for i in input_list:
        total += i
    return total


# wallet function - prints the outputs accordingly
# gets the fattest and skinniest value from the list
# invokes nested methods to calculate sum
def wallets(input_list):
    # sorts list
    input_list.sort()
    # last is unknown hence using -1 as to get the last element
    # in sorted list last element is largest
    fattest = input_list[-1]
    # first element is smallest
    skinniest = input_list[0]
    # invokes method to calculate total of all the values in the list
    total = calculate_sum(input_list)

    # prints the calculated outputs
    print("The fattest wallet has " + str(fattest) + " in it.")
    print("The skinniest wallet has " + str(skinniest) + " in it.")
    print("All together, these wallets have " + str(total) + " in them.")
    print("All together, the total value of these wallets is worth " + str(total/10) + " dimes.")


# method to convert the input string to list of integers
def str_to_int_list(str_input):
    # empty list to hold values
    input_list = list()
    # for loop to iterate on the input string
    for i in str_input.split(" "):
        # converting int before appending to list
        input_list.append(int(i))
    return input_list


def main():
    print("Enter the values in different wallets, Enter space separated values : ")
    # input is read as a string variable
    str_input = input()
    # invokes method to make the conversion from string to int list
    input_list = str_to_int_list(str_input)
    # invokes method to calculate various outputs values of wallet functionality
    wallets(input_list)


# invokes main method
main()

```

```
output 1:
      Enter the values in different wallets, Enter space separated values : 
        10 20 30 40 50
        The fattest wallet has 50 in it.
        The skinniest wallet has 10 in it.
        All together, these wallets have 150 in them.
        All together, the total value of these wallets is worth 15.0 dimes.
output 2:
output 3:
output 4:

```
## Problem 2: Periodic Table 

The Periodic Table of the Elements was developed to organize information about the elements that make up the Universe.
Write a terminal application that lets you enter information about each element in the periodic table.
Make sure you include the following information:
* symbol, name, atomic number, row, and column

You must save the elements in a dictionary where the `symbol` is the key and the other attributes are nested inside `symbol`. The nested keys are `name`, `number`, `row`, `column`.

To populate your dictionary with data, provide a menu of options to the users:

1. Search the element by symbol (see all the details).
2. Search by a property (`name`, `number`, `row`, `column`) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program

Make sure you do the appropriate communication with the user to get the necessary information to complete each step.

```python
def search_element_property_name(dict, name):
    list_elements = list()
    for x, y in dict.items():
        if y[0] == name:
            list_elements.append(x + ": " + str(y))
    return list_elements


def search_element_property_number(dict, number):
    list_elements = list()
    for x, y in dict.items():
        if y[1] == number:
            list_elements.append(x)
    return list_elements


def search_element_property_row(dict, row):
    list_elements = list()
    for x, y in dict.items():
        if y[2] == row:
            list_elements.append(x)
    return list_elements


def search_element_property_column(dict, column):
    list_elements = list()
    for x, y in dict.items():
        if y[3] == column:
            list_elements.append(x)
    return list_elements


def search_element_symbol(dict, symbol):
    return dict.get(symbol, -1)


def add_element(dict, symbol, name, number, row, column):
    dict[symbol] = [name, int(number), int(row), int(column)]


# 4th option to change the name of the element by symbol
def name_change(dict, symbol, name):
    dict[symbol][0] = name


# 4th option to change the number of the element by symbol
def number_change(dict, symbol, number):
    dict[symbol][1] = int(number)


# 4th option to change the row of the element by symbol
def row_change(dict, symbol, row):
    dict[symbol][2] = int(row)


# 4th option to change the column of the element by symbol
def column_change(dict, symbol, column):
    dict[symbol][3] = int(column)


def export_JSON_file(dict):
    file_handler = open('periodic_table.txt', 'w')
    file_handler.write('{')
    file_handler.write('\n')
    for x, y in dict.items():
        file_handler.write('\t')
        file_handler.write(str(x))
        file_handler.write(': ')
        file_handler.write(str(y))
        file_handler.write('\n')
    file_handler.write('}')
    file_handler.close()


def load_JSON_file():
    file_handler = open('periodic_table.txt', 'r')
    dict = file_handler.read()
    # for x, y in dict(input_str).items():
    #   print(x)
    #  print(y)
    print(dict)
    return dict


def menu_user_input():
    print("1. Search the element by symbol (see all the details).")
    print("2. Search by a property (name, number, row, column) and see "
          "the values for that property for all the elements in the table.")
    print("3. Enter a new element manually (type the information for each property)")
    print("4. Change the properties of an element (by symbol)")
    print("5. Export periodic table as a JSON file")
    print("6. Load periodic table from JSON file")
    print("7. Exit the program")


def main():
    menu_user_input()
    option = int(input("Enter the operation of you choice from menu : "))
    dict = {"iron": ["iron", 123, 12, 12]}
    if 1 > option > 7:
        print("Enter a valid option with in 1 - 7")
        option = int(input("Enter the operation of you choice from menu : "))
    while option != 7:
        if option == 1:
            print(search_element_symbol(dict, input("Enter symbol to search : ")))

        elif option == 2:
            choice = input("Enter if you want to search by name / number / row "
                           "/ column of the element you want to search: ")
            if choice == 'name':
                name = input("Enter name : ")
                print(search_element_property_name(dict, name))
            elif choice == 'number':
                number = int(input("Enter number : "))
                print(search_element_property_number(dict, number))
            elif choice == 'row':
                row = int(input("Enter row : "))
                print(search_element_property_row(dict, row))
            elif choice == 'column':
                column = int(input("Enter column : "))
                print(search_element_property_column(dict, column))
        # print(search_element_property_name(input("Enter name or number or row "
        #                                         "or column of the element you want to search: ")))
        elif option == 3:
            symbol = input("Enter symbol : ")
            name = input("Enter name : ")
            number = input("Enter number : ")
            row = input("Enter row : ")
            column = input("Enter column : ")
            add_element(dict, symbol, name, number, row, column)

        elif option == 4:
            symbol = input("Enter the symbol for which you want to update the properties: ")
            choice = input("Enter the property you want to modify (name, number, row, column) : ")
            if choice == 'name':
                name = input("Enter name : ")
                name_change(dict, symbol, name)
            elif choice == 'number':
                number = input("Enter number : ")
                number_change(dict, symbol, number)
            elif choice == 'row':
                row = input("Enter row : ")
                row_change(dict, symbol, row)
            elif choice == 'column':
                column = input("Enter column : ")
                column_change(dict, symbol, column)

        elif option == 5:
            export_JSON_file(dict)
        elif option == 6:
            load_JSON_file()
        option = int(input("Enter the operation of you choice from main menu : "))


main()

```
```
output 1:
```
