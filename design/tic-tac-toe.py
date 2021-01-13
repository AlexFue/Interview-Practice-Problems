Problem:
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
Follow up:
Could you do better than O(n2) per move() operation?

 

Example 1:

Input
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]

Explanation
TicTacToe ticTacToe = new TicTacToe(3);
Assume that player 1 is "X" and player 2 is "O" in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

ticTacToe.move(0, 2, 2); // return 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

ticTacToe.move(2, 2, 1); // return 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

ticTacToe.move(1, 1, 2); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

ticTacToe.move(2, 0, 1); // return 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

ticTacToe.move(1, 0, 2); // return 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
 

Constraints:

2 <= n <= 100
player is 1 or 2.
1 <= row, col <= n
(row, col) are unique for each different call to move.
At most n2 calls will be made to move.





Solution:
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[0 for x in range(n)] for y in range(n)] # n X n board
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player # add the marker 
        
        for x in range(len(self.board)): # loop at each index of row
            if self.board[row][x] != player: # if current marker doesnt match player, stop
                break
            if x == len(self.board)-1: return player # if at the end of row and marker matches player, return win 
            
        for x in range(len(self.board)): # loop at each index of column
            if self.board[x][col] != player: # if current marker doesnt match player, stop
                break
            if x == len(self.board) -1: return player # if at the end of column and marker matches player, return win 
            
        for x in range(len(self.board)): # loop at each index diagonally
            if self.board[x][x] != player: # if current marker doesnt match player, stop
                break
            if x == len(self.board) -1: return player # if at the end of diagonal and marker matches player, return win 
            
        for x in range(len(self.board)): # loop at each index of other way diagonally
            if self.board[x][len(self.board)-1-x] != player: # if current marker doesnt match player, stop
                break
            if x == len(self.board) -1: return player # if at the end of diagonal and marker matches player, return win 
            
        return 0 # return 0 if no wins for player




Process:
The way to solve this is by using efficient searching. 

For creating a board, we just use a nested forloop and add zeros to the board 

Since all moves are valid, we can just add it straight to the board. 
Now we should check if there is a win after every move because it could potentially be a win. 
To check for a win, we do not havfe to check the whole board, instead check just the row and col of the move you just added.
Doing this makes our search faster. 

We look at every column in the row and every row of the column that was added a move. 
We also check for diagonals to see if there is a win there. 
For every check, we stop checking if the current element in the index doesnt match the current player because its not their marker. 
If it is, we continue and at the last index we return the player that won if the marker matches the player. 

If all checks fail, return 0 because there is no win. 



