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
    print("All together, the total value of these wallets is worth " + str(total * 10) + " dimes.")


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
