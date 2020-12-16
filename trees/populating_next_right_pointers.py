Problem:
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

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



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000




Solution:
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left: # checks if we are not at a leaf
            root.left.next = root.right # connects the current left child to the right 
            if root.next: # if current node has a next, connect the current right to the next's left
                root.right.next = root.next.left
            self.connect(root.left) # process is done again for the left and right childs 
            self.connect(root.right)
        return root 




Process:
The way we solve this problem is with recursion. 
Since the tree is complete, we can just check if we have a node and the left child, if it has a left, then it has a right. 
Then we set the left child next to the right child. 
After if the current root has a next, then there is a node on the right with childs so we connect the current right child to the current nodes next left child. 
Last we continue to do this process recursively on the left and right childs
 
***Draw this out on a whiteboard to visualize it***



