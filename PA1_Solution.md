**Approach used to solve:**
1. As asked I started by reading the input files provided, user inputs one file and I read the file, if I fail to read the file like file name is incorrect or file is not found then I catch the error and print a message accordingly. I read file by file and store the sequences in variables - "sequence_1", "sequence_2".
2. Since there are two parts to the algorithm and the user should be able to execute any part individually I ask the user to enter the choice on part of algorithm he wants to execute. input should either be number of matches or maximum chain. input is store in variable "choice"
3. In both parts of the algorithm the user is asked to enter the maximum number of shifts he wish to do. this nubmer should be between 0 and length of sequence, if not a value error is raised and is printed accordingly. user input is stored in variable "max_shifts".

**Number of matches part of the algorithm: Methods used: "make_string_shifts" and "check_similarity" in main.py file**
1. This part is to do the similarity checks, by inducing spaces and comparing string to get the best score possible.
2. Starts with inducing spaces, number of spaces to be induced is decided in a for loop - in ith iteration i number of spaces are induced and the for loop runs from 0 to till the maximum number of shifts. 
 
    First I induce spaces at the begining of sequence 1 and at the end of sequence 2, after iterating till the max_shifts, I write a for loop to induce space at the end of the first sequence and at the beginning of the second sequence.
3. In each iteration best score is calculated in "check_similarity" and is stored in "similarity_count" - a counter variable which will be incremented by 1 each time a character match is found in both the sequences.
4. Initially a variable "prev_similarity_count" is defined with 0 value, this variable is used in order to store the best score from all the iterations. In each iteration when ever we encounter "similarity_count" greater than the "prev_similarity_count", then "prev_similarity_count" variable is updated with current best score from "similarity_count".
5. Along with storing the best score till now, we also store the sequences generated in that loop in prev_seq_1, prev_seq_2.
6. Since I have to output the best score from all the comparisions and the sequences in that comparision, I am returning multiple values (prev_similarity_count, prev_seq_1, prev_seq_2) from the method "make_string_shifts".
7. In the main method I storing these returned values in a list variable -"return_list" and then printing the outputs accordingly as need.
8. In order to get the indexes and characters that matched to result in the best score, I am processing the sequences stored in this return variable and printing the output.
9. In case if we get the best score possible as 0 with the number of shifts given by the user, the algorithm will decide the number of shifts to make - which is the length of the sequence - trying all the possibilities - and then getting the best score from all comparisions. 

**Maximum chain part of the algorithm: Methods used: "make_string_shifts" and "check_similarity" in maxchain.py file****
1. the logic of this part is written in maxchain.py file
2. This part is similar to the above part mentioned part of algorithm "Number of matches", with same variable names used in same scenarios.
3. An additional vaiable index is used here, which is to store the index at which the contiguious chain occurs. 
4. Here also we induce spaces into the string from 0 to maximum number of shifts provided by the user. by using for loop to do this process - ith iteration indicates i number of spaces to be induced and same as above written - first I induce spaces at the begining of sequence 1 and at the end of sequence 2, after iterating till the max_shifts, I write a for loop to induce space at the end of the first sequence and at the beginning of the second sequence.
5. In each iteration we do similarity check in function "check_similarity" to check the maximum chain matched. to do it, i used a for loop from 0 to length of the sequence, at any index we find a match we increment the counter variable - "similarity_count". 
6. In this for loop, an additional variable called "prev_count" is used to store the best score always, the maximum of "similarity_count" and "prev_count", "prev_count" is initialised to 0, as initially the maximum similairty count is 0. When updating the "prev_count" I am also updating the index variable to hold the current index, so that the index variable always shows the maximum contiguious chain. 
7. At any index in the for loop a mismatch is found then the "similarity_count" variable is set back to 0 so that the counter can start from 0 for the next matching character and can be increment if a subsequent character is also matching.
8. Since I need the index and best score from this method, I am returning both of them.
9. in the parent method "make_string_shifts" in maxchain.py file, I am receiving this best score for the current sequence and then checking it with the previous sequences best score - varaible used for previous sequence best score is "prev_similarity_count".
10. "prev_similarity_count" will always have the best score from all the sequences generated and compared till now.
11. after all the sequences are generated and compared, I will be returning the best score of all sequences, sequences generated in that iteration, index at which there is a maximum contiguious chain on both the sequences, variables returned are "prev_similarity_count, prev_seq_1, prev_seq_2, index" respectively.
12. if the best score possible with the shifts given by user is 0 then the algorithm decides to do all the shifts possible in the sequence, as in the maximum shifts would be the length of the sequence, which is the worst case scenario.
13. in the main method in main.py file, I will be printing the outputs as needed.


**Hurdles faced are :**
1. Understanding the part of maximum chain took a little bit of time and implementing this part also took some time, though the implementation part is similar, it took some time to figure it out.
2. Thinking of execeptions in various scenarios took some time, but its not a blocker, issue I faced is especially when I was checking maximum shifts given by user in within the sequence length, it took time to solve as I was thinking its a syntax issue but its a logical issue.
3. implementing the first part of the algorithm - number of matches - took some time, as its the first part of the PA being implemented, understanding logics on the whole and converting them into how to implement took some time.

**Benifits are:**
1. it made me understand python better. got abit more confident in it.
2. though both parts of the algorithm look similar but their work is different and is very interesting. one is checking character matching where as other can be used to get the sub-sequence matching. 
3. learnt modules and implementing more functions, exceptions, file handling.
4. made me think on what exception might occur, how better to implement a this solution like using string or list to store sequence, I later finalised to use string and wanted to avoid convertion to list and then parsing the list additionally.


**Source code links:**
1. main.py [https://github.com/UmaDeviPalaparthy/INF502/blob/main/code/main.py]
2. maxchain.py [https://github.com/UmaDeviPalaparthy/INF502/blob/main/code/maxchain.py]


**Execution of number of matches**
```
File contents: 
sequence1.txt : ACTGATCAC
sequence2.txt : TTAGCTCGA
```
**output for number of matches:**
```
Enter first file with DNA sequence which can have A,T,C,G chars in it : sequence1.txt
Enter second file with DNA sequence which can have A,T,C,G chars in it : sequence2.txt
Enter the approach you want to use : (number of matches or maximum chain) : number of matches
Enter maximum number of shifts you wish to do: 3
The best score is : 4
Both sequences have the following same chars :  ['T', 'A', 'C', 'C']
Both sequences have same characters at the following indexes :  [2, 4, 6, 8]
ACTGATCAC  
  TTAGCTCGA
```


**Execution of maximum chain:**
```
File contents: 
sequence1.txt : ACTGATCAC
sequence2.txt : TTAGCTCGA
```
**output for maximum chain:**
```
Enter first file with DNA sequence which can have A,T,C,G chars in it : sequence1.txt
Enter second file with DNA sequence which can have A,T,C,G chars in it : sequence2.txt
Enter the approach you want to use : (number of matches or maximum chain) : maximum chain
Enter maximum number of shifts you wish to do: 3
The best score is : 2
The start index at which the maximum contiguous chain occurs is :  5
ACTGATCAC
TTAGCTCGA
```
