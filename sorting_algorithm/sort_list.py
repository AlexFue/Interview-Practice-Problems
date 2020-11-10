Problem:
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []




Solution:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        tail, secondHead, secondTail = head, head, head
        while secondTail and secondTail.next:
            tail = secondHead
            secondHead = secondHead.next
            secondTail = secondTail.next.next
        tail.next = None
        
        left = self.sortList(head)
        right = self.sortList(secondHead)
        return self.merge(left, right)
        
    def merge(self, l1, l2):
        newList = ListNode(None)
        ptr = newList
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next 
        
        ptr.next = l1 or l2
        
        return newList.next




Process:
The way we are going to solve this is by using merge sort.
To split the linked list in halves we are going to use 3 pointers, to differentiate the tail of the first list, the head of the second list, and tail of the second list. Once we split our list, we call functions recursively to split more until they are singles, only then we can merge them together and sort. In the sort method we create a linked list that is going to represent the sort list that we will be returning. we figure out which is smallest and add it to the dummy linked list and any left overs afterwards to return. 

1.) Variables - variables to define our range of our sub linked lists
    a.) tail: represents the tail of the first list
    b.) secondHead: represents the head of the second list
    c.) secondTail: represents the tail fo the second list
        
2.) Splitting
    a.) loop while the secondTail and its next is not null - this is to set the range of our linked lists
        - increment each pointer accordingly 
    - set the next of the tail to none so you can have 2 seperate linked lists
    - call function recursively on the left and right linked list
    
3.) Merge(left, right)
    a.) create a dummy linked list to return at the end and pointer to set the valus of the linked list
    b.) loop while both left and right and not null
        - figure out which is smaller and add it to the new linked list
        increment pointers accordingly
    c.) whatever list still has values, add them to the new linked list
    - return linked list

This will eventually merge the lists together


