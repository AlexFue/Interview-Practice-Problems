Problem:
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.






Solution:
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1






Process:
The way we are going to solve this problem is with recursion 
We are going to get to a leaf node and return the value 0, this will represent the bottom of the tree. We then go 
back up and compare our value with other leaf nodes that went back up. We then compare which got the bigger value
(the deeper a node is, the greater the value). Once we get the bigger one we add 1 to it to account for the current 
level we are comparing for and go back up another level and do the same until we get to the root. 

1.) Base case:
    - sees if we are at a leaf node, checks if there is no existing node and returns 0 
2.) Recursive case: 
    - calls function recursively for left and right side of node, gets the max value and adds 1

-- I recommend watching a video on this problem and whiteboarding it.



