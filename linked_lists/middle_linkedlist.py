Problem:
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.




Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cur = head
        counter = 0
        while cur != None:
            counter += 1
            cur = cur.next
        middle = counter // 2
        
        cur = head
        while middle != 0:
            middle -= 1
            cur = cur.next
        return cur




Process:
# we can find the answer by finding the index of the middle value and then going to it with a loop

create a method to find the length of the list
1.) Create variables: variable to keep track of length and current node 
2.)loop through the list until there is no more nodes
    a.) increment the length variable and go on the the next node
3.) return the counter // 2, this returns the middle index

now that we know the middle index, we can loop til we get to the middle index and return that node
4.) get the current head 
5.) loop while the middle variable does not = zero
    a.) go on to the next node and decrement middle variable 
6.) return the current node







