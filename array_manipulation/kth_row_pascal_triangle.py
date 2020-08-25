Problem: 
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]




Solution: 
def getRow(self, A):
        triangle = []
        for triangle_row in range(A+1):
            row = []
            row.append(1)
            for element in range(triangle_row):
                if element+1 < len(triangle[triangle_row-1]):
                    pascal_number = triangle[triangle_row-1][element] + triangle[triangle_row-1][element+1]
                    row.append(pascal_number)
                else:
                    row.append(1)
            triangle.append(row)
        return triangle[A]




Process:
basically we create a pascal triangle up to the amount of rows it wants up to retrieve and then returns the last row of the pascal triangle which is the want they want (not very efficient way)

create a triangle list

for loop range from 0 to A with variable triangle_rows

	create a row list

	append 1 to the variable row

	for loop range from 0 to triangle_rows

		if there is a number to the right of the current number (when accessing the row before)

			add them together and append it to the current row

		else then append 1 to the row

			appened the row to the triangle

return triangle[A]




Teacher Solution: 
class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        curr = [1]*(A+1)
        if A<2 : return curr
        
        prev = self.getRow(A-1)
        for i in range(1,A):
            curr[i] = prev[i]+prev[i-1]
        
        return curr



