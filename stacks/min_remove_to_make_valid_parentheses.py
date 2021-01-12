Problem:
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.




Solution:
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] # stack to check for valid parentheses
        invalids = set() # set to add invalid closing parentheses that have to open ones
        for i, c in enumerate(s):
            if c not in '()': # skip non parentheses characters
                continue
            if c == '(': # if its an open, store in stack 
                stack.append(i)
            elif not stack: # if its a close and theres no open in stack for it to be valid, store in set of invalid closing
                invalids.add(i)
            else: # if its a close and theres an open in stack for it to be valid, pop open from stack 
                stack.pop()
                
        invalids = invalids.union(set(stack)) # add any remiaining opens from stack and invalid closings into 1 set
        ans = '' # string to store final valid string 
        
        for i, c in enumerate(s): # now loop through s again and add all chars into ans except that invalid parentheses from set
            if i not in invalids:
                ans += c
            
        return ans




Process:
They way we are going to solve this problem is with a stack 

So we want to get rid of all the parentheses that make the string invalid. 
Like valid parentheses problem, we use a stack to add the open parentheses and pop when we see a closing parentheses
The difference is we store the indexes of where the open parentheses. 
We also create another data structure that stores indexes of closing parentheses when there is not open ones in the stack to pop, this makes the closing ones invalid.

The reason we store the indexes is so we can loop through the string again and add all the characters except the invalid parentheses whose indexes are store, into a final string to return 


