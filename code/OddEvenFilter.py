def odd_even_filter(numbers):
    list_even = list()
    list_odd = list()
    list_full = list()
    # print(numbers)
    for x in numbers:
        if x % 2 == 0:
            list_even.append(x)
        else:
            list_odd.append(x)
    # print(list_even)
    # print(list_odd)
    list_full.append(list_even)
    list_full.append(list_odd)
    # print(list_full)
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
