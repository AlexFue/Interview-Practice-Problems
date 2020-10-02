Problem:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false




Solution:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for lst in matrix:
            if len(lst) > 0 and target <= lst[-1]:
                left = 0
                right = len(lst) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if lst[mid] == target:
                        return True
                    elif lst[mid] > target:
                        right = mid-1
                    else:
                        left = mid+1
                return False
        return False




Process:
o here we are going to create a half linear search/ half binary search solution
1.) We need to find out which list our target is even going to be in. We do that by looping through each list in the matrix and we check if our target is in there by checking the last number in the list. if our target number is less than or equal to the last number in the list, then we know the target may be in that list (the lists are sorted so we can do this). 

***if we do not pass this first check, then we go onto the next list in the matrix***

2.) Now that we found the list that our target may be in, we do a normal binary search within the list. The only thing different from this binary search is that if we find the number, we return true. We also might not even find the target in the list so in that case, we will break out of the binary search and return false

3.) Another case we have to take into consideration is what if we never find the target, anywhere in the matrix, well we would have gone checked each last number in the matrix and then exit out the forloop. So then we return false at the end

***Note: To make an even more efficient solution, instead of loop through each list, try doing another binary search for the list the target may be in. 

# we should loop through each list in the matrix 
#     check if our target is less than or equal to the last number in the matrix 
#         we are going to do a form of binary search 
#         create pointer for the beginning of list 
#         create pointer for the end of list
#         do search while left pointer < right pointer
#             create mid pointer = left + right // 2
#             if mid number of is the target 
#                 return true 
#             if mid number > target
#                 move right pointer to mid-1 
#             else if mid number < target 
#                 move left pointer to mid+1
#         return false since we did not find it 
#     return false 
    






