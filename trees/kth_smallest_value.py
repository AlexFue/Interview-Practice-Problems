Problem:
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

 

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.





Solution:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.ans = None
        self.helper(root)
        return self.ans
    
    def helper(self, root):
        if root:
            self.helper(root.left)
            self.k -= 1
            if self.k is 0: 
                self.ans = root.val
                return 
            self.helper(root.right)




Process: 	
The way we are going to solve this problem is with the inorder traversal of a tree method.
When we do an inorder traversal, we go all the way to the left, print out the value, then go to the right. In a 
BST, the smallest value in the the left most node and it gets bigger as we go more to the right. So we can do inorder traversal to get to the smallest value(left most) and then start counting out kth smallest element as we go back up to bigger numbers(right most). We will create a helper function to do that for us and also be decrementing our k, everytime we go back up the tree after we went all the way down. It will also be helpful to create a sort of static k variable so all of our recursions will link to the same k. 

1.) Variables: 
    a.) k: 
        - creates a self.k so that the whole class can have access to that one variable
    b.) ans: 
        - creates self.ans to represent our answer and it will be changed in the helper function once we find our
          kth smallest value

2.) Function helper function that will find the kth smallest value and put it inside self.ans

3.) return the answer with new value if there was a tree, otherwise we just return the default value of None

Helper function(takes in a node):
    - we check if we have a node to do the traversal process
        - we call the function recursively for the left child of the curent node, this will get us to the smalles             value
        - decrement k, this will run once we get to the smallest value 
        - if k is 0, we are at out kth smallest value and so we set out ans to it and return to end that recursive           process
        - call function recursively for the right child of the current node, this will get us to the biggest value,           also if we run this then we are going up the smallest values
        
* one thing to note is that once we find out kth smallest value, we stil keep traversing the tree to finish doing the code for the rest of the tree nodes.
    





