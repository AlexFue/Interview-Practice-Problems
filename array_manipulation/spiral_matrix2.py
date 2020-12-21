Problem:
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20




Solution:
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # create a n*n matrix of zeros
        matrix = []
        for x in range(n):
            row = []
            for y in range(n):
                row.append(0)
            matrix.append(row)
        matrix[0][0] = 1 # changes the first elements 
        
        add = True # our bool to check if we have added all the elems
        row = 0 # index for our current row 
        col = 0 # index for our current col
        num = 2 # variable for num that we change in matrix 
        
        while add: # loop until wehave added all the nums 
            add = False # change to false and change back to true if we added a num, meaning theres possibly more nums to add
            
            while col+1 < n and matrix[row][col+1] == 0: # move right, check if we are in bounds and the next elem to the right hasnt been changed
                matrix[row][col+1] = num # change num
                num += 1 # increment num for next elements
                col += 1 # move to right
                add = True
            
            while row+1 < n and matrix[row+1][col] == 0: # move down, check if we are in bounds and the next elem down hasnt been changed
                matrix[row+1][col] = num
                num += 1 # increment num for next elements
                row += 1 # move down
                add = True
            
            while col-1 >= 0 and matrix[row][col-1] == 0: # move left, check if we are in bounds and the next elem to the left hasnt been changed
                matrix[row][col-1] = num
                num += 1 # increment num for next elements
                col -= 1 # move left 
                add = True
                
            while row-1 >= 0 and matrix[row-1][col] == 0: # move up, check if we are in bounds and the next elem up hasnt been changed
                matrix[row-1][col] = num
                num += 1 # increment num for next elements
                row -= 1 # move up 
                add = True
                
        return matrix 




Process:
The way we solve this problem is with array manipulation. 
We are going to do this by creating a n*n matrix full of zeros since the array will never have zeros, then traverse it spirally and change the zeros the the nums they are supposed to by. 


First create a n*n matrix full of zeros and add the first element.
Then we have to fill up the rest of the elements with their numbers accordingly. 

We do this process where we check if we added a num and when the algorithm first runs, its set to false but once we added a number its set to true, we know we added all nums if theh bool stays false. 
In this loop we have 4 movements: right, down, left, up. 
In each we check if the next elem is in bounds and has to be changed, if so we change it, move accordingly, and set our bool to true. 

we keep doing this until our we cant do any of the loops, meaning we added all the nums and our bool stays false, stoping the algorithm






