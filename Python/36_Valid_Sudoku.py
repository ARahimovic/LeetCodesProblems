'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules
'''

def is_value_possible(board, x,y):
    #test the row
    for i in range(9):
        if (i != y) and board[x][i] == board[x][y]:
            return False

    #test the column
    for i in range(9):
        if (i != x) and board[i][y] == board[x][y]:
            return False
    
    row_start = x //3 * 3
    column_start = y //3 * 3

    for i in range(3):
        for j in range(3):
            if (row_start + i != x or column_start + j != y) and board[row_start + i][column_start + j] == board[x][y]:
                return False
    return True

def is_value_possible_using_sets(board, x, y):
    row_set = set()
    column_set = set()
    subgrid_set = set()

    for i in range(9):
        if board[x][i] in row_set:
            return False
        row_set.add(board[x][i])
    
        if board[i][y] in column_set:
            return False
        column_set.add(board[i][y])

        subgrid_row = x//3 * 3 + i // 3
        subgrid_column = y//3 * 3 + i % 3
        
        if(board[subgrid_row][subgrid_column] in subgrid_set):
            return False
        subgrid_set.add(board[subgrid_row][subgrid_column])
                    


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == '.'):
                    continue
                if not is_value_possible(board, i,j):
                    return False

        return True