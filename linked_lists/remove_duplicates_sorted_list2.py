Problem: 
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.




Solution:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        sentinal = ListNode(0, head) # create sentinal node to return 
        prev = sentinal # pointer to keep track of previous node of current/head
        
        while head: #loop through linked list
            if head.next and head.val == head.next.val: # if current node is same as next, theres a copy
                while head.next and head.val == head.next.val: # move current pointer forward until no more copies
                    head = head.next 
                prev.next = head.next # set the previous next to currents next to skip copies 
            else: # if no copies, move previous pointer forward
                prev = prev.next 
            head = head.next #  move current pointer forward
            
        return sentinal.next # return sentinal.next which is the new head of linked list 




Process: 
The way we are going to solve this problem is by using pointers 

We need 3 pointers to solve this, 1 to return theh linked list at the end, 1 to keep track of a previous node, and the other to traverse the copies. 

We are going to loop through the whole linked list once, 

At each iteration, check if the current node is equal to the next, if so do another loop to skip over the copies.
Then you set the previous.next to the current.next, skipping over the copies 

If the current node doesnt equal the next, then theres no copies so increment the previous node 

Also, always increment the current node 

At the end, return the sentinal.next which is the head since sentinal itself is a dummy node. 






