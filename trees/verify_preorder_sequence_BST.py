Problem:
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?




Solution:
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        s = [] # stack to store left side nums of tree 
        low = float('-inf') # var to store current lowest num when checking
        
        for num in preorder:
            if num < low: return False # if a num < the current lowest, its false since the lowest is infinity until you start going right and popping, the nums should only get bigger from there. 
            while s and s[-1] < num: # you are on left side so pop nums and set them to the new lowest
                low = s.pop()
            s.append(num) # add each num in stack to compare 
            
        return True # if you go through all the code without errors, traversal is fine, even if theres still nums in stack. 




Process:
The way we solve this is with a stack. 

Basically, since this is preorder traversal, the left should be decreasing and then increase as we go to the right. 
So we have a low num and check if num in the traversal if its lower the the low var, if not we are still going to the left so add the nums to a stack. 
Once you find a num that is greater than the last num you added, you are going to the right of the tree so pop elements and make the the new low var. 

You do this process cause the right should ways be bigger than the left. 

If a num is lower than the current low, than return false because you are at the right but finding a lower num which is wrong. 




