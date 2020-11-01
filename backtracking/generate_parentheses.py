Problem:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]




Solution:
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []
        self.helper(lst, '', 0, 0, n)
        return lst
    
    def helper(self, lst, string, o, c, n):
        if len(string) == n*2:
            lst.append(string)
            return
        
        if o < n:
            self.helper(lst,string + '(', o+1, c, n)
            
        if c < o:
            self.helper(lst, string + ')', o, c+1, n)




Process:
The way we are going to solve this problem is with backtracking. 
We want to create all the different permutations for the parentheses. We can create a list to 
store the permutations and create a function to do the process. We will insert a empty string 
to start the permuations and go on from there. We should keep track of the number of open/close
parentheses we have to make sure we are making valid parentheses. Also our function will have 3
cases, a base case, a case to add an open parenthesis, and a case to add a close parenthesis. 

1.) Variables: 
    a.) list - to store all different permutations

2.) Helper function: takes in the list, a empty string to start permutations, amount of open parenthesis for string, amount of close parenthesis for string, n input
    - to create permutations
    a.) Base case:  
        - checks if the string is a full permutation, meaning is has n open/close parenthesis to add to list
    b.) First check:
        - checks if number of open parenthesis is less than n to add another to it recursively 
    c.) Second check:
        - checks if number of close parenthesis is less than open to add another to it recursively 


3.) Return list 


Picture this as a tree (even though its not)
lets say n was 2

                            ''
                    '('
        '(('             "()"
            '(()'     "()("
                '(())'     "()()"
It goes all the was to use all open parenthesis
then closes them to create '(())'
the code is finished so it backtracks to '(' and goes to the next line of code
eventually gets to '()()' by recursion











