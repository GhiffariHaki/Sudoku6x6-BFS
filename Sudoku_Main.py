from Sudoku_DFS import solve

#papan sudoku
print ("\n\nSolving Sudoku 6x6...")
board = [[0,6,0,0,0,0],
      [0,0,3,0,0,0],
      [0,0,0,0,0,1],
      [0,0,0,3,0,0],
      [0,0,0,0,6,0],
      [0,0,0,0,0,0]]

print ("Board:")
for row in board:
      print (row)

solve(board)
