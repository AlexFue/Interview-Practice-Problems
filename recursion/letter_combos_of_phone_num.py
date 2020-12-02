Problem:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]




Solution:
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = {'2': 'abc',
             '3': 'def',
             '4': 'ghi',
             '5': 'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'}
        lst = []
        self.helper('', digits, lst, d)
        return lst
    
    def helper(self, s, digits, lst, d):
        if not digits:
            lst.append(s)
        else: 
            for l in d[digits[0]]:
                    self.helper(s + l, digits[1:], lst, d)





Process:
We are going to solve this problem using Depth First Search (dfs).
We use dfs because we go to every digit and once we get to the last one, we go through each of its "childs" or letters it represents and once it has exhausted all of them, it backtracks to the previous number and then go through each of its child and then back to the last digit to do the process again but for a different child of a digit. 
Heres a representation:
'2345'
adgj -> adgk -> adgl -> adhj -> adhk -> adhl -> adij ...
   ^       ^       ^      ^^       ^       ^      ^^
   |       |       |      ||       |       |      ||
you see it goes all the way to the end to go through each letter, and once it does that it back back 
forward to change a letter and then back go through each letter again but for a different letter combo

1.) Variables: 
    - a dictionary to convert numbers to their represented letters
    - a list to store all the letter combos of the digit string
    
2.) helper function(combo string, digits string, lst of combos, dictionary):
    - if digits string is empty then we create a combo so we add it to combos string
    - else you run a for loop that goes through each letter of the first digit of the digits string
        recursively call your function(add current letter to combo string, take away current digit from digits string, pass in same list of combos, pass in same dictionary)
    
We only our loop to go through one digit so we only get the first digit of the sting since everytime
we call the fucntion recursive, we pass in one less digit in the digits string. 

        
        

