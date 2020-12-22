Problem:
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False




Solution:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.lst = []
        self.index = None
        
        def storage(node):
            if node:
                storage(node.left)
                self.lst.append(node)
                storage(node.right)
            
        storage(root)    

    def next(self) -> int:
        if self.index == None:
            self.index = 0
            return self.lst[self.index].val
        else:
            self.index += 1
            return self.lst[self.index].val
        

    def hasNext(self) -> bool:
        if self.index == None and len(self.lst) > 0: return True
        if self.index < len(self.lst)-1: return True 
        return False




Process:
The way to solve this problem is by using a list

The idea for the init function is we traverse the tree inorder and put every node in a list as storage. 
We also create a index variable to know where we are at in the list

For the next function we would check if its our first time running this we so we return the first element in the list. 
If its not our first time, we increment the index before turning the node value.

For the has next we check if the index is less then the length of the list - 1 to ensure we can go to the next node, if not return false.
Also check a edgecase where we might be at the onexisting node and there is a next node, in that case return True 




