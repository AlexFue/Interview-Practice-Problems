Problem:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.




Solution:
def validate_sudoku_board(board):
  seen = []
  for row in range(9):
    for col in range(9):
      current_value = board[row][col]
      if current_value != ".":
        if ((current_value + " found in row " + str(row)) not in seen) and ((current_value + " found in col " + str(col)) not in seen) and ((current_value + ' found in box ' + str(row/3 + col/3)) not in seen):
          seen.append(current_value + " found in row " + str(row))
          seen.append(current_value + " found in col " + str(col))
          seen.append(current_value + ' found in box ' + str(row/3 + col/3))
        else:
          return False
  return True




Process:
we go through each box of the Sudoku board and keep track of each number that we have not aswell as the place we found them and put it all in a list.
if we come accross a number in one of the same positions we already noted it, the board is false but if we go through the whole board without any duplicates in the same locations, the board is true.
the locations we should keep track of each number is the column, row, and sub box it is in


makes a list where all the elements with their position will be placed and represented as numbers we have seen

loop through each row

	loop thorugh each col

		if the current number with its row, col, and box number has not been seen yet, (that means is it not in the seen list)

			then we add it to the seen list along with its row, col, and box number

		if it is then that means that there is a duplicate number in either a row, col, or box (the number and positions is in the seen list) and so we return the board as invalid

if we made it through the loop without breaking then each number in the row, cols, and boxes are unique and so the board is valid (each number with its position has not been seen in the list)