Problem:
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]





Solution:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode() # new linked list for merge
        ptr = l # pointer to traverse list
        
        while l1 and l2: # loop to add nodes from lists to new list
            if l1.val < l2.val: # if current l1 node is smaller, add it to new list 
                ptr.next = l1 # sets it as current new list's node next
                l1 = l1.next  # increment list pointer to next node
            else: # if current l2 node is smaller or equal, add it to new list
                ptr.next = l2 # sets it as current new list's node next
                l2 = l2.next # increment list pointer to next node
            ptr = ptr.next # increment ptr for new list to add anymore nodes 
            
        if l1 or l2: ptr.next = l1 or l2 # add remaining nodes of a list 
        
        return # l.next return the next of new list head because thats where the nodes that were added start




Process:
The way we solve this problem is by using pointers.

We create a new linked list for merging the 2 linked list and a pointer to traverse it. 
Then we traverse the 2 linked list and add them to the new one, depending which is smaller. 
We increment the pointers according from what list we added a node from, and we also increment new linked list pointer for adding. 

At the end, if 1 list still has nodes, we add it to the end the new list since there is nothing to compare anymore






