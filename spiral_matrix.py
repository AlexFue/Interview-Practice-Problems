Problem:
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]




Solution:
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return [] # if matrix is empty then return nothing
        s = [matrix[0][0]] # initialize matrix with first element
        row = 0 # index to move through rows
        col = 0 # index to move through cols
        row_boundary = len(matrix) # variable to know number of rows
        col_boundary = len(matrix[0]) # variable to know number of rows
        
        while len(s) != row_boundary*col_boundary: # does prcess until all length of list != # of elems in matrix
            while col+1 < col_boundary and matrix[row][col+1] not in s: # shift right, checks if theres an element to the right that we havent added 
                s.append(matrix[row][col+1]) # adds it 
                col += 1 # moves to right
            
            while row+1 < row_boundary and matrix[row+1][col] not in s: # shift down, checks if theres an element under that we havent added 
                s.append(matrix[row+1][col]) # adds it 
                row += 1 # moves down row
            
            while col-1 >= 0 and matrix[row][col-1] not in s: # shift left, checks if theres an elements to the left that we havent added 
                s.append(matrix[row][col-1]) # adds it 
                col -= 1 # moves to left
                
            while row-1 >= 0 and matrix[row-1][col] not in s: # shift up, checks if theres an element up that we havent added 
                s.append(matrix[row-1][col]) # adds it 
                row -= 1 # moves up
        return list(s)




Process:
They way this we are going to solve this is with array manipulation. 

So since we want to spiral the matrix, we can do traverse clockwise like a clock to get all the elements. 

What we can do is create 4 movement systems: right, down, left, and right in that order. 
If we cant do one, we move on to the next until we are either going to be out of bounds, or we are going to reach a place we already went. 

We do this until we have all the elements and we know that if the length of our storage is the same as m * n, the amount of elements in the matrix 






