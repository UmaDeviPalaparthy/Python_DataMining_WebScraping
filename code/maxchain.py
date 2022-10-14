# Method to shift strings by number shifts provided and invoke method to compare these modified strings
def make_string_shifts(sequence_1, sequence_2, shifts):

    # variable to store prev similarity count to compare with current count and decide the large score
    prev_similarity_count = 0
    prev_seq_1 = sequence_1
    prev_seq_2 = sequence_2
    index = -1   # to hold the index at which maximum contiguous chain occurs

    # adding spaces at the beginning of sequence 1
    for i in range(shifts):
        spaces = ""
        for j in range(i):
            spaces += " "
        seq_1 = spaces + sequence_1
        seq_2 = sequence_2 + spaces
        #print(seq_1)
        # default value 0, as the worst similarity can be is 0

        similarity = check_similarity(seq_1, seq_2)
        if similarity[0] > prev_similarity_count:
            # prev_similarity_count always has the largest value
            prev_similarity_count = similarity[0]
            prev_seq_1 = seq_1
            prev_seq_2 = seq_2
            index = similarity[1]

    # adding spaces at the beginning of sequence 2
    for i in range(shifts):
        spaces = ""
        for j in range(i):
            spaces += " "
        seq_2 = spaces + sequence_2
        seq_1 = sequence_1 + spaces
        #print(seq_1)
        # default value 0, as the worst similarity can be is 0
        similarity = 0
        similarity = check_similarity(seq_1, seq_2)
        if similarity[0] > prev_similarity_count:
            # prev_similarity_count always has the largest value
            prev_similarity_count = similarity[0]
            prev_seq_1 = seq_1
            prev_seq_2 = seq_2
            index = similarity[1]

    return prev_similarity_count, prev_seq_1, prev_seq_2, index


# function to check the similarity in given two strings
def check_similarity(seq_1, seq_2):
    # if the length of sequences is not same raise error
    if len(seq_1) != len(seq_2):
        raise ValueError("Length of both the sequences should be equal")

    # initializing the count to default value 0, since if no match are found - the worst case is always 0
    similarity_count = 0
    prev_count = 0
    index = -1  # to hold the index at which maximum contiguous chain occurs
    # for loop iterate from 0 to length of the sequence 1, since both the strings are of equal length
    for i in range(len(seq_1)):
        # if at any index chars in both the sequences are equal increment the similarity count variable
        if seq_1[i] == seq_2[i]:
            similarity_count += 1
            if similarity_count > prev_count:
                prev_count = similarity_count
                index = i  # contains the last index where the maximum contiguous chain occurs
        else:
            similarity_count = 0

    return prev_count, index

