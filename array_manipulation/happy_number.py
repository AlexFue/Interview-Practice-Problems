Problem:
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1




Solution:
class Solution:
    def isHappy(self, n: int) -> bool:
        lst = []
        while n != 1:
            if n not in lst:
                lst.append(n)
            else:
                return False
            total = 0
            for digit in str(n):
                total += int(digit)**2
            n = total
        return True




Process:
We are going to solve this problem with a list and a while loop. 
The process is adding the number to the list to see if we already had it and then generate the new number. 
We do this process over and over until we get 1 or repeat a number. 

1.)we create a list
2.)do a loop while our number != 1, since that is what we want
    a.)if the number is not in the list
        add it, to make sure if we are going to have a loop 
    b.)if it is 
        return false, because if the number appears again then there is going to be an infinite loop
    c.)do process to change number 

3.)we return true since our number is 1 and it broke out of the loop 










