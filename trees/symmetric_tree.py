Problem:
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3




Solution:
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left or not right:
            return left == right
        
        if left.val != right.val:
            return False
        
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)




Process:
The way we are going to solve this is with recursion. 
We are going to create a helper function that will do everything for us. It takes in a left and right. 
It checks if either one is empty and figures out if they are equal or not and returns that. 
If none of the nodes are empty, it then then checks if the values are not the same and returns false. 
If they are the same it returns the function again recursively to do the checks again but for other sides like this: 
    
            head
           /    \
          c      c checks both sides of head
         / \    / \
        c1  c2 c2  c1 checks left of left, right of right -AND- right of left, left of right
                        continues to do this process 
            
1.) Edge case: 
        - checks if root is empty and returns because there is nothing to check
2.) helper function (takes in left and right child nodes)
    a.) checks if either one of the nodes is empty 
        - determines if they are equal or not and returns the bool value
    
    (if both nodes are present, it goes on with the code)
    
    b.) checks if both node values do not have the same value 
        returns false if so
        
    (if both nodes are present and have equal values, it goes on with the code)
        
    c.) returns the function recursively with the left child node of current left node and right child node of current right node. Also check does with right child node of current left node and left child node of current right node. (It gets checked like this because they are symmetrical parts)
    
        





