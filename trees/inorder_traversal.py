Problem:
Given the root of a binary tree, return the inorder traversal of its nodes values  

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]




Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            return self.helper(root, [])
        return []
    
    def helper(self, node, lst):
        if node:
            self.helper(node.left, lst)
            lst.append(node.val)
            self.helper(node.right, lst)
            return lst




Process:
create a helper function to do all the implementation like if you are just traversing the tree, but now you want to store the values in a list 

1.) the given function:
    a.) return the helper function with the root and a empty list to store values

this function is like like a normal traversal but appending values instead of printing
2.) helper function: (takes in a node and a list)
    a.) check if we have a node
        call resursively for left node and the same list
        we add our current node to list
        call resursively for right node and the same list
        return the list 




