"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""
board = [
 ["5", "3", ".", ".", "7", ".", ".", ".", "."]
,["6", ".", ".", "1", "9", "5", ".", ".", "."]
,[".", "9", "8", ".", ".", ".", ".", "6", "."]
,["8", ".", ".", ".", "6", ".", ".", ".", "3"]
,["4", ".", ".", "8", ".", "3", ".", ".", "1"]
,["7", ".", ".", ".", "2", ".", ".", ".", "6"]
,[".", "6", ".", ".", ".", ".", "2", "8", "."]
,[".", ".", ".", "4", "1", "9", ".", ".", "5"]
,[".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# answer: true

board2 = [
 ["8", "3", ".", ".", "7", ".", ".", ".", "."]
,["6", ".", ".", "1", "9", "5", ".", ".", "."]
,[".", "9", "8", ".", ".", ".", ".", "6", "."]
,["8", ".", ".", ".", "6", ".", ".", ".", "3"]
,["4", ".", ".", "8", ".", "3", ".", ".", "1"]
,["7", ".", ".", ".", "2", ".", ".", ".", "6"]
,[".", "6", ".", ".", ".", ".", "2", "8", "."]
,[".", ".", ".", "4", "1", "9", ".", ".", "5"]
,[".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# answer: false

def valid_sudoku(board):
    sideways = [[row[x] for row in board3][::-1] for x in range(0,10)]
    squares = []
    squares.append([row[0:2]] + [])
    # print(board_sideways)
    for x in range(0,10):
        if len(board[x]) != len(set(board[x])):
            return False
        
        if len(sideways[x]) != len(set(sideways[x])):
            return False
        

    
        

print(valid_sudoku(board))

board3 = [
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3],
    [4,4,4,4],
]

sideways = [[row[x] for row in board3][::-1] for x in range(0,4)]
print(sideways)