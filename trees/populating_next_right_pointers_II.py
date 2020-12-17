Problem:
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100




Solution:
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root: # base case to see if we have a node to do work 
            if root.left: # check if we have a left node to connect
                if root.right: root.left.next = root.right # if we have a right node, connect the left to it
                else: root.left.next = self.helper(root.next) # if no right, call helper to try to find next closest node to the right 
            if root.right: # checks if we have right node to connect
                root.right.next = self.helper(root.next) # if we have right node, call helper to try to find next closest node to the right 
            
            self.connect(root.right) # do process again for current left node 
            self.connect(root.left) # do process again for current right node 
        return root 
    
    def helper(self, cur): # DFS process
        if not cur: return None # if there is no node, we reached the end of level, there was not node to connect to 
        elif cur.left: return cur.left # if we have a left node, return it to connect 
        elif cur.right: return cur.right # if we have a right node, return it to connect 
        return self.helper(cur.next) # if no child nodes on this parent node, go to next node in the level 




Process:
The way we solve this problem is with a recursive DFS approach. 

Similar to the Populating Next Right Pointers in Each Node I, we want to populate each node to the one on the right, but in this case, the right node might not be right next door.
In that case, we do DFS to keep on doing deeper in the current level to the right until we find the first closes right node to connect to. 

First we Check if we have a node to do the process to. 
Then we check if we have a left and right node individually because we might not have one. 

For connecting the right left child node, we see if we can connect it to the right child and if not, we call our DFS helper function that keeps on going to the next pointer of the current parent node and tries to find a next node to pointer the left to. 
For connecting the right child, we call our helper function on the parents next node because a right child always connects to a next child, and we keep on doing the same process of trying to find a node to connect it to. 

Last we return the root 


***Note: Not sure why we have to traverse from right to left instead of left to right on lines 57-58, maybe its to see what nodes are coming in advance?***




