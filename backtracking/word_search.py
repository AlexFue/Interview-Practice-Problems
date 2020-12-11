Problem:
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false




Solution:
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board, r, c, word):
                    return True
        return False

        # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res




Process:
The way we are going to solve this problem is with backtracking. 
We loop through each box on the board and for each box, we call our dfs function. The function
takes in the board, row, col, and word we are trying to find. The function checks if the word 
is empty and returns true because we either found it or we never had one. Then we check if we are
out of bounds or if the first letter of the word is not the same as the current box from the
board. After we create a copy board to mark up so we know we already used that letter. Next we
create a function equal to the function recursively but we are checking all sides for the next 
letter in the word. At the end return the variable 
