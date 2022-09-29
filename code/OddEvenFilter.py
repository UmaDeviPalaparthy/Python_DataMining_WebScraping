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
