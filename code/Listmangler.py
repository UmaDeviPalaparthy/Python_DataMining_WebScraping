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
