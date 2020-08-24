Problem: 
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate a given row in Pascal's Triangle (we'll call it R):
for R[i] in row R, sum up R[i] and R[i-1] from previous row R - 1.

Example:
Given numRows = 5,
Return
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]




Solution:
def pascal_triangle(numRows):
  triangle = []
  for triangle_rows in range(numRows):
    row = []
    # triangle always starts with 1 
    if triangle_rows == 0:
      row.append(1)

    # for every other row in the triangle, this adds 1 to the beginning and end, also adds all numbers from the row before 
    else:
      row.append(1)
      for index in range(0, len(triangle[triangle_rows-1])-1):
        pascal_number = triangle[triangle_rows-1][index] + triangle[triangle_rows-1][index+1]
        row.append(pascal_number)
      row.append(1)
    triangle.append(row)
  return triangle

print(pascal_triangle(3))




Process: 
create list called triange that will have all the row lists

for loop from 0 to numRows

	create list called row

	if its the beginning of the loop

		row is equal to [1]

		append row to triangle list

	else

		append 1 to list row

		for loop through the row list before the current one

			number = add current index num to the next

			append number to current list row

		append 1 to current list row

		append current list row to triangle

return the triangle list






