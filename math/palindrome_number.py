Problem:
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1





Solution:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        multiplier = 1 # variable to check ends 
        
        while x / multiplier >= 10: # will increment the variable to be the same length as x
            multiplier *= 10
            
        while multiplier >= 10: # do this while our variable can check more than 1 number 
            if x // multiplier != x % 10: return False # if the ends of x are not equal, return false
            x = (x % multiplier) // 10 # the modulo deletes the front end of x and takes off any leading zeros, and the division takes up the end of x
            multiplier = multiplier // 100 # shaves off 2 zero places from variable since we shaved off 2 nunmbers off x
            
        return True # if we went through whole number x and they ends were all the same, return x




Process:
The way we solve this problem is with math. 

The way the algorithm goes for this problem is that if we compare the front half of the number to the back half, then we can check if its a palindrome without having to go through the whole thing. 

To make this easier, we can get rid of the negative numbers since the - sign makes it not a palindome any more. 

We need another variable to let us do math and check each side of the number to see if they are equal, if so then we delete it and update our variables to check the next ends of the number. 





