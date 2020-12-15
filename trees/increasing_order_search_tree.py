Problem:
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]




Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.cur = TreeNode() # creating class variable cur to a empty node and ans is a pointer to the class variable cur
        self.work(root) # calling function to build our tree
        return ans.right # return the right child of ans because self.cur built the tree and ans still pointer to the empty node 
    
    def work(self, node):
        if node:
            self.work(node.left) # gets us to the smallest number
            node.left = None # cuts ties with left child of current node so we can add it to our new tree
            self.cur.right = node # builds our new tree by adding current node of function to the right side of self.cur
            self.cur = self.cur.right # moves self.cur to the new right child to do the same process in the future, its like a pointer 
            self.work(node.right) # gets us to bigger numbers once we got all theh way to bottom





Process:
The way we solve this is with recursion and backtracking
Basically we create a new node to build our tree. We then traverse the old tree all the way to the smallest number. 
Once there we start building our new tree with the smallest numbers first and putting them on the right. 
Make sure to cut ties of the nodes your are putting on the new tree from it's older left childs.



