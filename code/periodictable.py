# method to search the dictionary and get all the names
# input json_dict has nested dictionary with details
def search_element_property_name(json_dict):
    # for loop to get all the parent level keys
    for key in json_dict.keys():
        # prints the names in the nested dictionary
        print(json_dict[key]["name"])


# method to search the dictionary and get all the numbers
# input json_dict has nested dictionary with details
def search_element_property_number(json_dict):
    # for loop to get all the parent level keys
    for key in json_dict.keys():
        # prints the numbers in the nested dictionary
        print(json_dict[key]["number"])


# method to search the dictionary and get all the rows
# input json_dict has nested dictionary with details
def search_element_property_row(json_dict):
    # for loop to get all the parent level keys
    for key in json_dict.keys():
        # prints the row in the nested dictionary
        print(json_dict[key]["row"])


# method to search the dictionary and get all the columns
# input json_dict has nested dictionary with details
def search_element_property_column(json_dict):
    # for loop to get all the parent level keys
    for key in json_dict.keys():
        # prints the column in the nested dictionary
        print(json_dict[key]["column"])


# method to search the dictionary (json_dict) using symbol which is at parent key level
def search_element_symbol(json_dict, symbol):
    # if present returns the value, if not present returns -1
    return json_dict.get(symbol, -1)


# method to ass elements into dictionary, it adds nested dictionary as well
# json_dict is the dictionary
def add_element(json_dict, symbol, name, number, row, column):
    # sub_json variable holds the nested dictionary in json format.
    sub_json = {"name": name, "number": number, "row": row, "column": column}
    # assigning nested json to the parent dictionary
    json_dict[symbol] = sub_json


# 4th option, method to change the name of the element by symbol
def name_change(json_dict, symbol, name):
    # symbol is the key for which the property name is being edited
    json_dict[symbol]["name"] = name


# 4th option, method  to change the number of the element by symbol
def number_change(json_dict, symbol, number):
    # symbol is the key for which the property number is being edited
    json_dict[symbol]["number"] = int(number)


# 4th option, method  to change the row of the element by symbol
def row_change(json_dict, symbol, row):
    # symbol is the key for which the property row is being edited
    json_dict[symbol]["row"] = int(row)


# 4th option, method  to change the column of the element by symbol
def column_change(json_dict, symbol, column):
    # symbol is the key for which the property column is being edited
    json_dict[symbol]["column"] = int(column)


# 5th option, to export the existing dictionary object into a json file in json format.
def export_json_file(json_dict):
    # opening the file "periodic_table.json" in write mode, file path is in same location as the current file
    file_handler = open('periodic_table.json', 'w')
    # write the dictionary object to file, converting it to string as we can write data in string formats.
    file_handler.write(str(json_dict))
    # closing the opened file.
    file_handler.close()


# 6th option, method to load the json in file into dictionary
def load_json_file():
    # opening the file "periodic_table.json" in read mode, file path is in same location as the current file
    file_handler = open('periodic_table.json', 'r')
    # read all the lines from the file at once as a string.
    json_string = file_handler.read()
    # converting the read json string into dictionary object.
    json_dictionary = eval(json_string)
    print(json_dictionary)


# Method to print the main menu to the user.
def menu_user_input():
    print("1. Search the element by symbol (see all the details).")
    print("2. Search by a property (name, number, row, column) and see "
          "the values for that property for all the elements in the table.")
    print("3. Enter a new element manually (type the information for each property)")
    print("4. Change the properties of an element (by symbol)")
    print("5. Export periodic table as a JSON file")
    print("6. Load periodic table from JSON file")
    print("7. Exit the program")


# main method to indicate the start of the flow
def main():
    # first printing menu to let the users read and choose from options.
    menu_user_input()
    # reading user input on menu number selected
    option = int(input("Enter the operation of you choice from menu : "))
    # sample Json with hardcoded data initialized, contains 2 elements with their properties in nested json
    json_dict = {'iron': {'name': 'iron', 'number': 123, 'row': 12, 'column': 12},
                 'nickel': {'name': 'nickel', 'number': 231, 'row': 121, 'column': 12}}

    # if user input a menu other than given, ask the user to enter an appropriate number
    if 1 > option > 7:
        print("Enter a valid option with in 1 - 7")
        option = int(input("Enter the operation of you choice from menu : "))

    # iterating on the entire menu and respective operations until user inputs 7 to exit
    while option != 7:
        # option 1 to search the element by symbol
        if option == 1:
            print(search_element_symbol(json_dict, input("Enter symbol to search : ")))

        # option 2 to search the element by its properties name / number / row / column
        elif option == 2:
            # choice - holds the input on what property to be searched
            choice = input("Enter if you want to search by name / number / row "
                           "/ column of the element you want to search: ")
            # if user wants to search by name
            if choice == 'name':
                search_element_property_name(json_dict)

            # if user wants to search by number
            elif choice == 'number':
                search_element_property_number(json_dict)

            # if user wants to search by row
            elif choice == 'row':
                search_element_property_row(json_dict)

            # if user wants to search by column
            elif choice == 'column':
                search_element_property_column(json_dict)
        # option 3 to insert a new element to the dictionary, asks user input for all the properties and symbol
        elif option == 3:
            symbol = input("Enter symbol : ")
            name = input("Enter name : ")
            number = input("Enter number : ")
            row = input("Enter row : ")
            column = input("Enter column : ")
            # method invocation to add the new element
            add_element(json_dict, symbol, name, number, row, column)

        # option 4, update the property of the element by using any of the property
        elif option == 4:
            # asks user input on symbol for which user want to update the property
            symbol = input("Enter the symbol for which you want to update the properties: ")
            # asks the user to provide the property that he wants to update
            choice = input("Enter the property you want to modify (name, number, row, column) : ")

            # update name of the symbol
            if choice == 'name':
                name = input("Enter name : ")
                name_change(json_dict, symbol, name)
            # update number of the symbol
            elif choice == 'number':
                number = input("Enter number : ")
                number_change(json_dict, symbol, number)
            # update row of the symbol
            elif choice == 'row':
                row = input("Enter row : ")
                row_change(json_dict, symbol, row)
            # update column of the symbol
            elif choice == 'column':
                column = input("Enter column : ")
                column_change(json_dict, symbol, column)

        # option 5, write the dictionary to file in json format
        elif option == 5:
            export_json_file(json_dict)
        # option 6, read the json from a file into dictionary.
        elif option == 6:
            load_json_file()
        # repeat to ask the user to provide option form the main menu
        option = int(input("Enter the operation of you choice from main menu : "))


# Main method invocation.
main()
