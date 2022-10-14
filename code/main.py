# importing module with functionality to get the maximum number of chains match
import maxchain


# Method to shift strings by number shifts provided and invoke method to compare these modified strings
def make_string_shifts(sequence_1, sequence_2, shifts):

    # variable to store prev similarity count to compare with current count and decide the large score
    prev_similarity_count = 0
    prev_seq_1 = sequence_1
    prev_seq_2 = sequence_2

    # adding spaces at the beginning of sequence 1
    for i in range(shifts):
        spaces = ""
        for j in range(i):
            spaces += " "
        seq_1 = spaces + sequence_1
        seq_2 = sequence_2 + spaces

        # default value 0, as the worst similarity can be is 0
        similarity_count = check_similarity(seq_1, seq_2)
        if similarity_count > prev_similarity_count:
            # prev_similarity_count always has the largest value
            prev_similarity_count = similarity_count
            prev_seq_1 = seq_1
            prev_seq_2 = seq_2

    # adding spaces at the beginning of sequence 2
    for i in range(shifts):
        spaces = ""
        for j in range(i):
            spaces += " "
        seq_2 = spaces + sequence_2
        seq_1 = sequence_1 + spaces

        # default value 0, as the worst similarity can be is 0
        similarity_count = check_similarity(seq_1, seq_2)
        if similarity_count > prev_similarity_count:
            # prev_similarity_count always has the largest value
            prev_similarity_count = similarity_count
            prev_seq_1 = seq_1
            prev_seq_2 = seq_2

    return prev_similarity_count, prev_seq_1, prev_seq_2


# function to check the similarity in given two strings
def check_similarity(seq_1, seq_2):
    # if the length of sequences is not same raise error
    if len(seq_1) != len(seq_2):
        raise ValueError("Length of both the sequences should be equal")

    # initializing the count to default value 0, since if no match are found - the worst case is always 0
    similarity_count = 0
    # for loop iterate from 0 to length of the sequence 1, since both the strings are of equal length
    for i in range(len(seq_1)):
        # if at any index chars in both the sequences are equal increment the similarity count variable
        if seq_1[i] == seq_2[i]:
            similarity_count += 1

    return similarity_count


# method to read sequence from file
def readfile(file_path):
    # opening file in read mode.
    file_handler = open(file_path, 'r')
    # read all the content in the file as string
    file_content = file_handler.read()
    # closing file after finishing its use
    file_handler.close()
    return file_content


# main method definition, reads sequences from files
def main():
    # try to check and catch if error if file is not found
    try:
        # read first sequence from file "sequence1.txt" which is in the same path as the current file
        sequence_1 = readfile(input("Enter first file with DNA sequence which can have A,T,C,G chars in it : "))  # sequence1.txt
        # read second sequence from file "sequence2.txt" which is in the same path as the current file
        sequence_2 = readfile(input("Enter second file with DNA sequence which can have A,T,C,G chars in it : "))  # "sequence2.txt"
    except FileNotFoundError:
        print("one or both the sequence files are not found, check for file names and file paths")
        exit()

    # asks user to give input on choice of which part algorithm to be executed
    choice = input("Enter the approach you want to use : (number of matches or maximum chain) : ")
    if choice == "number of matches":
        # max_shifts - variable to do maximum number of shifts,
        # worst case maximum number of shifts to do is shift till the length of sequence
        max_shifts = len(sequence_1)
        try:
            max_shifts = int(input("Enter maximum number of shifts you wish to do: "))
            # print(max_shifts)
            if 0 > max_shifts or max_shifts > len(sequence_1):
                raise ValueError("Enter a numerical value from 0 to length of the string")
        except ValueError:
            # if the user input a value other than integer then value error is thrown by int()
            # after printing the error, exit the program
            print("Enter a numerical value from 0 to length of the string")
            exit()

        # try block to catch errors thrown while comparing strings for similarity check
        try:
            # invoke method to check for similarity
            # similarity_count = check_similarity(sequence_1, sequence_2)
            return_list = make_string_shifts(sequence_1, sequence_2, max_shifts)

            # if possible best score is 0, worst case when the maximum number of shifts given by the
            # user is not enough to decide the best score
            if return_list[0] == 0:
                # worst case maximum number  of shifts to do is shift till the length of sequence
                max_shifts = len(sequence_1)
                # re-invoke the function to check the similarity once again
                return_list = maxchain.make_string_shifts(sequence_1, sequence_2, max_shifts)

            # printing the outputs for number of matches scenario
            print("The best score is : " + str(return_list[0]))  # similarity_count
            same_chars = list()
            same_char_indx = list()
            for i in range(len(return_list[1])):
                if return_list[1][i] == return_list[2][i]:
                    same_chars.append(return_list[1][i])
                    same_char_indx.append(i)
            print("Both sequences have the following same chars : ", same_chars)
            print("Both sequences have same characters at the following indexes : ", same_char_indx)
            print(return_list[1])  # sequence_1
            print(return_list[2])  # sequence_2
        except ValueError as ve:
            # if any exception raises log it in console and exit the application
            print(ve)
            exit()
    # below will get execute if the user wants to run the other part of the algorithm for maximum chain
    elif choice == "maximum chain":
        # max_shifts - variable to do maximum number of shifts,
        # worst case maximum number  of shifts to do is shift till the length of sequence
        max_shifts = len(sequence_1)
        try:
            max_shifts = int(input("Enter maximum number of shifts you wish to do: "))
            if 0 > max_shifts or max_shifts > len(sequence_1):
                raise ValueError("Enter a numerical value from 0 to length of the string")
        except ValueError:
            # if the user input a value other than integer then value error is thrown by int()
            # after printing the error, exit the program
            print("Enter a numerical value from 0 to length of the string")
            exit()

        # try block to catch errors thrown while comparing strings for similarity check
        try:
            # invoke method to check for similarity
            # similarity_count = check_similarity(sequence_1, sequence_2)
            return_list = maxchain.make_string_shifts(sequence_1, sequence_2, max_shifts)

            # if possible best score is 0, worst case when the maximum number of shifts given by the
            # user is not enough to decide the best score
            if return_list[0] == 0:
                # worst case maximum number  of shifts to do is shift till the length of sequence
                max_shifts = len(sequence_1)
                # re-invoke the function to check the similarity once again
                return_list = maxchain.make_string_shifts(sequence_1, sequence_2, max_shifts)

            # printing the outputs for number of matches scenario
            print("The best score is : " + str(return_list[0]))  # similarity_count
            print("The start index at which the maximum contiguous chain occurs is : ",
                  (return_list[3] - return_list[0] + 1))
            print(return_list[1])  # sequence_1
            print(return_list[2])  # sequence_2

        except ValueError as ve:
            # if any exception raises log it in console and exit the application
            print(ve)
            exit()
    else:
        print("The approach you want to use should either be \"number of matches\" or \"maximum chain\" ")


main()
