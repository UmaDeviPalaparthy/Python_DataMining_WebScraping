Create a markdown file on your own GitHub repository (private, inviting me).
In this markdown, provide a short description of your approach to solve the problem.
List your source code, and the result of at least one example per approach, along with the contents of the files you used.
Discuss the the hurdles and benefits of developing each approach, and how did you handle them (I'd suggest to keep track of this in a diary-based approach).


Approach used to solve:
As I read the problem statement it seemed like a big problem and also since there are two different parts of the algorithm to be implemented, I first though of using module in my solution like what ever I am gone write should be modularised and clearly use lot of funtions.

1. As asked I started by reading the input files provided, user inputs one file and I read the file, if I fail to read the file like file name is incorrect or file is not found then I catch the error and print a message accordingly. I read file by file and store the sequences in variables - "sequence_1", "sequence_2".
2. Since there are two parts to the algorithm and the user should be able to execute any part individually I ask the user to enter the choice on part of algorithm he wants to execute. input should either be number of matches or maximum chain.
3. in both parts of the algorithm the user is asked to enter the maximum number of shifts he wish to do. this nubmer should be between 0 and length of sequence, if not a value error is raised and is printed accordingly.

Number of matches part of the algorithm:
1. Next starts the similarity checks, first with 0 spaces induced in both the strings we check for the best score possible.
2. next I started with for loop to induce spaces in from 1 to number of shifts, and in each iteration checking for the best score,  at the begining of the first sequence and the end of the second sequence, since length should be same. 
3. storing the previous best score and comparing the current best score (variable - similarity_count ) to get the maximum of both and store it in variable used for previous best score ("prev_similarity_count"), which will be the final best score. I am also storing the sequences as well when ever I encounter a revision to the bestscore.
4. while calculating the current best score, using a counter variable to increment by 1 each time a character match is found in both the sequences.
5. Since I have to output the best score from all the comparisions and the sequences in that comparision and returning multiple values from this method "make_string_shifts"
6. in the main method I storing these returned values in a list variable (variable - "return_list") and then printing the outputs accordingly as need.
7. in order to get the indexes and characters that matched to result in the best score, I am processing the sequences stored in this return variable and printing the output.
8. in case if we get the best score possible as 0 with the number of shifts given by the user, the algorithm will decide the number of shifts to make - which is the length of the sequence - trying all the possibilities - and then getting the best score from all comparisions. 


Valiation errors:
File validaiton
part of the algorithm to choose should either be number of matches or maximum chain.
Maximum number of shifts should be between 0 to length of the string.
Length of sequence in both the files



hurdles faced are : understanding the part of maximum chain took a little bit of time and implementing this part.
and thinkg of execeptions in various scenarios, especially max shifts > str length then it took time to solve thinking its a syntax issue but its a logical issue.
