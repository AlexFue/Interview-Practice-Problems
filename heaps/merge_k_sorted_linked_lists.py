Problem: 
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []




Solution:
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ans = ListNode() # create new linked list to store sorted nodes 
        ptr = ans # pointer to iterate through linked list
        heap = [] # heap to help sort nodes
        
        for head in lists: # iterate through each head of the linked lists
            while head: # iterate through each nodes in a linked list 
                value = head.val  # get the value, add it to heap, iterate to next pointer of linked list 
                heapq.heappush(heap, value)
                head = head.next 
        while heap: # iterate through each value in heap 
            value = heapq.heappop(heap) # pop smallest value 
            ptr.next = ListNode(value) # add it to linked list 
            ptr = ptr.next # iterate linked list pointer 
            
        return ans.next # return new sort linked list 




Process: 
The way we are going to solve this problem is by using a min heap. 

So since we want to create a new linked list with all the value from lists but sorted, we should first get all the values of nodes. 

First, loo through each linked list in nodes and add the value in a heap, the heap will sort it. 

Once all values are in, start popping, the heap will pop the smallest values first since its a min heap. 

Create each value as a node and add it to a new linked list to return. 

Return that new linked list. 



