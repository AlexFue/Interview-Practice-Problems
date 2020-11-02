Problem:
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.




Solution:
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return 
        
        dic = {}
        copy_head = Node(head.val)
        dic[head] = copy_head
        
        while head:
            if head not in dic:
                copy = Node(head.val)
                dic[head] = copy
                
            if head.next and head.next not in dic:
                copy = Node(head.next.val)
                dic[head.next] = copy
                dic[head].next = copy
            elif head.next in dic:
                dic[head].next = dic[head.next]
                
            if head.random and head.random not in dic:
                copy = Node(head.random.val)
                dic[head.random] = copy
                dic[head].random = copy 
            elif head.random in dic:
                dic[head].random = dic[head.random]
                
            head = head.next
            
        return copy_head




Process:
The way we are going to solve this is with a dictionary 
We create a dictionary to store all the nodes, but we have to make sure we make a new node as a 
copy, it cant be the same node that is given to us. We loop through the linked list given to us
and check if we have made a copy of it in our dictionary, if not then we make a copy and add 
it and connect its. next and random variable to the appropriate node. If the node is already made, 
we just point to it. 


1.) Variables: 
	a.) dictionary: 
		- to store all copies of nodes
	b.) copy head: 
		- copy of given head and used to return copied linked list at end

2.) While Loop:  (add the real node as the key, and the copy as the value so we can peek in dictionary)
	- loops through the given linked list
	a.) check if current node is not in the dictionary yet 
		- create a copy of it and add it
	b.) check if current node has a next node and if its not in dictionary 
		- create a copy of it and add it 
		- connect the copy current node to the copy next node 
	c.) check if the current nodes next node is in dictionary
		- connect the copy current node to the copy next node 
	d.) check if current node has a random node and if its not in dictionary
		- create a copy of it and add it 
		- connect the copy current node to the copy random node 
	e.) check if current nodes random node is in dictionary
		- connect the copy current node to the copy random node 
	move the current node to the next node in the linked list

3.) Return head of copied linked list















