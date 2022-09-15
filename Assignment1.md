# Git/GitHub Assignment

* **INDIVIDUAL ASSIGNMENT**
* **Due date**: Sept-13th 11:59PM
* **Value**: 100 points counted towards Homework category.

## Description
This assignment is composed of two parts. 
- [Part 1](#Part-1-Dealing-with-git) consists of executing a sequence of commands and giving explanations about the commands you have to run. For each question, please provide appropriate explanation and/or the details requested.

- [Part 2](#Part-2-Using-GitHub) consists of creating a Markdown file on a fork of this course and creating a pull request towards this repo.

### Part 1: Dealing with git

To conduct this, you will have to download [handson.zip](handson.zip) and unzip it in your local machine. **Note:** handson folder is a git repository.

Then, follow these steps:

**On GitHub:**
1. Create a new repository under your GitHub account called *INF502*;
2. Create a file called *"Assignment1.md"*;
3. Copy the questions from this section and paste in your *"Assignment1.md"* file (tip: to copy the questions, click on *"Raw"* at the right-top of this file; this will show you the markdown source);
4. For each empty grey box, please provide an answer to the questions below.
5. Invite me to see your new repository. This will allow you to keep a private repository that only you and me will be able to see.

Your submission is complete when you complete the *Assigment1.md* file with your answers and invite me to your repo.

**On your local machine:** Using the command line, find and access the "handson/" directory (if you didn't download and unzip the file, go back to the beginning of Part 1's instructions). Then, answer the following questions (on your *Assigment1.md* file):

1. List all the branches in this repository and, for each branch, list the commits.

    - Use `git branch` to list the branches in this repository.
    - Use `git checkout` to explore each branch.
    - Use `git log --decorate` to explore the structure of commits.

```
There are two branches : master and math
$ git branch
* master
  math

$ git checkout master
Already on 'master'

$ git log --decorate
                commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
                Author: Igor Steinmacher <igorsteinmacher@gmail.com>
                Date:   Wed Aug 14 23:15:28 2019 -0700

                    Making a small change here

                commit 654b490a181dedf82dd6deda5f9848d6cca05918
                Author: Igor Steinmacher <igorsteinmacher@gmail.com>
                Date:   Wed Aug 14 23:12:14 2019 -0700

                    Added a draft of A.py

                commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
                Author: Igor Steinmacher <igorsteinmacher@gmail.com>
                Date:   Wed Aug 14 23:08:47 2019 -0700

                     Creating all files (all empty)


$ git checkout math
Switched to branch 'math'

$ git log --decorate
                    commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
                    Author: Igor Steinmacher <igorsteinmacher@gmail.com>
                    Date:   Wed Aug 14 23:13:48 2019 -0700

                        Adding some more knowledge to the function

                    commit 654b490a181dedf82dd6deda5f9848d6cca05918
                    Author: Igor Steinmacher <igorsteinmacher@gmail.com>
                    Date:   Wed Aug 14 23:12:14 2019 -0700

                        Added a draft of A.py

                    commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
                    Author: Igor Steinmacher <igorsteinmacher@gmail.com>
                    Date:   Wed Aug 14 23:08:47 2019 -0700

                         Creating all files (all empty)

```

2. Try `git log --graph --all` to see the commit tree. Paste the result here and write a paragraph to provide an interpretation of what you found.
```
* commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
|
|     Making a small change here
|
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (math)
|/  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
|   Date:   Wed Aug 14 23:13:48 2019 -0700
|
|       Adding some more knowledge to the function
|
* commit 654b490a181dedf82dd6deda5f9848d6cca05918
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:12:14 2019 -0700
|
|     Added a draft of A.py
|
* commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700

       Creating all files (all empty)


Understanding :
This command shows the activity performed in the repository from bottom to top (most recent activity is on top). for each commit 
it shows the commit hash value, author, data of commit and comments given by developer during commit. HEAD -> points the current 
branch we are working on, in this case its master branch. on the left on the commits, there is a green and red line between stars 
- representing till when the branches are in sync. The dash that come out on right indicates when the branch is created and if 
there is dash back into the main straight line then it indicates the branch is merged. red dashes indicate that there is 
different content in both the files, where as geen line represents that the branch is merged back into the master and all the 
branches are in sync. The same is in our case there is branch created after two commits and third commit is performed in branch 
math whereas fourth commit is performed in master branch.
```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch. Summarize the difference from master to the other branch.

```
$ git diff math
diff --git a/A.py b/A.py
index 0afa98c..dc1e9bd 100644
--- a/A.py
+++ b/A.py
@@ -1,11 +1,3 @@
 #this is just an example, do not freak out
 def calculate_this(operator, num1, num2):
-   if operator == 'sum':
-      print num1 + num2
-      print 'That was easy buddy'
-   else:
-      if operator == 'subtraction':
-         print num1 - num2
-         print 'I could handle that...'
-      else:
-         print 'my knowledge is limited'
+   print 'my knowledge is limited'
diff --git a/B.py b/B.py
index e69de29..c63f94c 100644
--- a/B.py
+++ b/B.py
@@ -0,0 +1 @@
+# Another file that will receive a line of code... at least.


Summarization : 
In the child branch A.py file, inside method there is some if else logic added in it, where as the master branch A.py file inside 
the method there is only one print statement - printing - 'my knowledge is limited'. whereas in B.py file in the child branch 
there is no comment added but in the master branch's B.py file there is a comment added. I am checking the difference from master 
branch so '--- a/A.py' mean that there is some content less in master branch when compared to child branch, '+++ b/B.py' means 
that there is content in master branch's B.py which is not there in child branch's B.py. 

```

4. Write a command sequence to merge the non-master branch into `master`.

```
git merge math

```


5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) and (ii) change to this branch.

```
$ git branch math

$ git checkout math
Switched to branch 'math'
```
   
6. Edit B.py adding the following source code below the content you have there.
```
print 'I know math, look:'
print 2+2
```

7. Write a command (or sequence) to commit your changes.
```
$ git commit -a -m "I know math commit"
[math1 29d4dc5] I know math commit
 1 file changed, 2 insertions(+)


```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'hello world!'
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened.
```
$ git merge math
Auto-merging B.py
CONFLICT (content): Merge conflict in B.py
Automatic merge failed; fix conflicts and then commit the result.


Merge conflict occured, because the same line in both the files have different content.
```
   
10. Write a set of commands to abort the merge.
```
$ git merge --abort

```
   
11. Now repeat item 9, but proceed with the manual merge (editing B.py). All implemented methods are needed. Explain your procedure.
```
Since its aborted earlier I merged again so that conflicts will show up.
After the conflicts showed up, I decided which file's content to keep in file. I decided to keep both the files content. 
So I removed (<<<<<<< HEAD, =======, >>>>>>> math) and followed the following steps.

Then I added all the files once again.

$ git add .

Committed my changes into master branch and the conflict is resolved.
$ git commit -a -m "resolve conflict"
[master f8ef1b6] resolve conflict

But these changes are only in master but not in my child branch so I switch back to child branch and rebase it from 
master to keep both in sync. I followed the bellow commands to do it.

$ git checkout math
Switched to branch 'math'

$ git rebase master
Successfully rebased and updated refs/heads/math.
```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date.
```
Since I am in child branch 'math' I followed these commands:

$ git checkout master
Switched to branch 'master'

$ git merge math
Already up to date.
```

13. Complete Part 2. Then, come back here and answer the following:
Report your experience of submitting the Part 2. Please, include the steps you followed, the commands you used, and the hurdles you faced (within the file you created for the **Part 1**).
```
1. First I forked your repository 'INF502-Fall22' to mine.
2. I went into the students folder in my forked repository and added my file 'PALAPARTHY_NAGA UMA DEVI.md'.
3. Again on Git webpage, I edited the file to create basic structure, like writting tittle, journal name, pages etc.
4. I went into my local machine and the did git clone - using command 
    '$ git clone https://github.com/UmaDeviPalaparthy/INF502-Fall22.git'
5. I open my file with my name in notepad++ and added rest of the content to it.
6. After finishing edditing, I commited it into my local repository. using command '$git commit -a -m "Adding outcomes"'
7. After commiting it, now I have to piush these changes into remote repository. For which I used command '$ git push origin main'.
8. After checking if my changes are reflected in the webpage of git, I created pull request.

Hurdles faced - when pushing my changes from local repository to remote repository, my machine asked me to sign into github locally.
I was confused why it was asking and also I had issues with my web browser (microsoft edge) which didnt allow me to sign in straight 
away. after I changed the browser to chome only then things started working and was able to push. Main task that took time here is 
recognizing the browser issue.
```

### Part 2: Using GitHub

The goal of this assignment is to put you in touch with the fork-pull request process, with an extra of dealing a little bit with Markdown. To learn more about Markdown [click here](https://guides.github.com/features/mastering-markdown/).

To complete this submission, follow these steps:

1. Fork the course repository (available [here](https://github.com/chavesana/INF502-Fall22)).

2. Into the students folder, create a markdown file called LASTNAME_FIRSTNAME.md (please change LASTNAME_FIRSTNAME for your actual last and first names). 

3. Use markdown to write a report of the last paper you've read. You can structure your markdown the way you want, but the following information must be there:
- Title
- Venue (journal name/conference)
- Number of pages
- Three outcomes of the paper
- Link to the paper online

4. Commit your file and push to your own GitHub repository (INF502).

5. Create a pull request to the course repository. Your pull request needs to appear [here](https://github.com/chavesana/INF502-Fall22/pulls).

6. Go back to Part 1 and answer the question 13 based on your experience in solving Part 2.

Your Part 2 submission is complete when your pull request is listed in the link above.
