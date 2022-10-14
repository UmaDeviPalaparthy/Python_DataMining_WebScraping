Create a markdown file on your own GitHub repository (private, inviting me).
In this markdown, provide a short description of your approach to solve the problem.
List your source code, and the result of at least one example per approach, along with the contents of the files you used.
Discuss the the hurdles and benefits of developing each approach, and how did you handle them (I'd suggest to keep track of this in a diary-based approach).


Approach used to solve:
1. As asked I started by reading the input files provided, user inputs one file and I read the file, if I fail to read the file like file name is incorrect or file is not found then I catch the error and print a message accordingly. I read file by file and store the sequences in variables - "sequence_1", "sequence_2".
2. Since there are two parts to the algorithm and the user should be able to execute any part individually I ask the user to enter the choice on part of algorithm he wants to execute. input should either be number of matches or maximum chain. input is store in variable "choice"
3. in both parts of the algorithm the user is asked to enter the maximum number of shifts he wish to do. this nubmer should be between 0 and length of sequence, if not a value error is raised and is printed accordingly. user input is stored in variable "max_shifts".

Number of matches part of the algorithm: Method: "make_string_shifts" and "check_similarity" in main.py file
1. This part is to do the similarity checks, by inducing spaces and comparing string to get the best score possible.
2. Starts with inducing spaces, number of spaces to be induced is decided in a for loop - in ith iteration i number of spaces are induced and the for loop runs from 0 to till the maximum number of shifts. 
  2.i. First I induce spaces at the begining of sequence 1 and at the end of sequence 2, after iterating till the max_shifts, I write a for loop to induce space at the end of the first sequence and at the beginning of the second sequence.
3. In each iteration best score is calculated in "check_similarity" and is stored in "similarity_count" - a counter variable which will be incremented by 1 each time a character match is found in both the sequences.
5. initially a variable "prev_similarity_count" is defined with 0 value, this variable is used in order to store the best score from all the iterations. In each iteration when ever we encounter "similarity_count" greater than the "prev_similarity_count", then "prev_similarity_count" variable is updated with current best score from "similarity_count".
6. Along with storing the best score till now, we also store the sequences generated in that loop in prev_seq_1, prev_seq_2.
7. Since I have to output the best score from all the comparisions and the sequences in that comparision, I am returning multiple values (prev_similarity_count, prev_seq_1, prev_seq_2) from the method "make_string_shifts".
8. in the main method I storing these returned values in a list variable -"return_list" and then printing the outputs accordingly as need.
9. in order to get the indexes and characters that matched to result in the best score, I am processing the sequences stored in this return variable and printing the output.
10. in case if we get the best score possible as 0 with the number of shifts given by the user, the algorithm will decide the number of shifts to make - which is the length of the sequence - trying all the possibilities - and then getting the best score from all comparisions. 


Valiation errors:
File validaiton
part of the algorithm to choose should either be number of matches or maximum chain.
Maximum number of shifts should be between 0 to length of the string.
Length of sequence in both the files



hurdles faced are : understanding the part of maximum chain took a little bit of time and implementing this part.
and thinkg of execeptions in various scenarios, especially max shifts > str length then it took time to solve thinking its a syntax issue but its a logical issue.
As I read the problem statement it seemed like a big problem and also since there are two different parts of the algorithm to be implemented, I first though of using module in my solution like what ever I am gone write should be modularised and clearly use lot of funtions.
