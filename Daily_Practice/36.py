'''
36. Valid Sudoku: https://leetcode.com/problems/valid-sudoku/

Time Complexity: 
'''
import collections

def isValidSudoku(board):
  #create set dictionary to store integer on the board. 
  cols = collections.defaultdict(set)
  rows = collections.defaultdict(set)
  square = collections.defaultdict(set)  # key = (r /3, c /3) for 3 x 3 square

  for r in range(9):      #loop the rows  
   for c in range(9):     #loop the columns
      if board[r][c] == ".":      #Skip if the spot is empty
       continue

      #if the integer is already exit in rows & cols and its 3x3 square, return False
      if(board[r][c] in rows[r] 
         or board[r][c] in cols[c] 
         or board[r][c] in square[(r//3, c//3)]): 
        return False

      #if not, add them in the set
      cols[c].add(board[r][c])
      rows[c].add(board[r][c])
      square[(r//3, c//3)].add(board[r][c])

   return True


print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9",".",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))