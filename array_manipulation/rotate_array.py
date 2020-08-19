Problem: 
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
Do not return anything, modify the input array in-place instead.




Solution:
def rotate_array(input_array, k):
 # does the process k amount of times 
  for rotate in range(k):
  	# grabs the last element from the array 
    elem = input_array.pop(len(input_array)-1)
    # inserts last element to the front 
    input_array.insert(0, elem)




Process: 
so to rotate an array, instead of moving all the elements to the right,
you can just move the last element to the front and it simulates 1 
rotation of moving to the right 

create a temp variable
for loop k amount of times
  for loop through input_array starting from the back of the input_array and ending at second element
    temp equal to input_array[i-1]
    input_array[i-1] equal input_array[i]
    input_array[i] equal to temp
  
  
