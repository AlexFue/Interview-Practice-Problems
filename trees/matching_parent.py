Problem:
Find the closest parent of two nodes in a binary tree. 
You are given 2 child nodes. Each child node has it’s value and a reference to its parent. 
All node values are unique. You can expect to only receive nodes that are part of the binary tree. 

class Node:   			
	Node* parent
	int value
      		         
Example:
Given node with value 2 and node with value 11 the closest 
Parent is node with value 7
	
Given node with value 4 and node with value 5 the closest node is 2

Given any node twice then the closest parent is itself 





Solution:
class Node:
 def __init__(self, parent, value):
   self.parent = parent
   self.value = value
 
def parent(node1, node2):
 if node1.value == node2.value:
   return node1
 
  values = set()
 node1 = node1.parent
 node2 = node2.parent
 
 while node1 != None or node2 != None:
   if node1:
     if node1.value in values:
       return node1
     values.add(node1.value)
     node1 = node1.parent
 
   if node2:
     if node2.value in values:
       return node2
     values.add(node2.value)
     node2 = node2.parent
  return 'No matching parents'





Process:
Basically we keep on looping through each node's parent. every parent node we come across we put in a set to keep track and if either node appears in again, we return it because values are unique so that is the matching parent node.
 
1.) edge case: if nodes are the same
  return the node itself
 
2.) loop through the nodes until there is no more nodes
  - keep track of each parent in a set 
  - if we comeacross a duplicate, then we are coming across the same parent    
  	- we return that parent node
3.) if we went through the tree without no matching node values, then there is no matching parent








