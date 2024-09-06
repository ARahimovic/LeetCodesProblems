'''
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
'''
def countLiveAdjacentCell(matrix,m,n,row,col):
    count = 0

    for i in range(-1,2):
        for j in range(-1,2): 
            if (0 <= row + i < m) and (0 <= col + j < n) and (i != 0 or j != 0):
                if matrix[row + i][col + j] == 1:
                    count +=1
    return count

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        liveCellDict = {}
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n) :
                liveCellDict[(i,j)] = countLiveAdjacentCell(board,m,n,i,j)
        
        for key in liveCellDict:
            row = key[0]
            col = key[1]
            #if cell is alive
            if board[row][col] == 1 :
                if liveCellDict[key] == 2 or liveCellDict[key] == 3 :
                    board[row][col] = 1 #redundant but it seems faster than using   if not (liveCellDict[key] == 2 or liveCellDict[key] == 3): board[row][col] = 0 
                else:
                    board[row][col] = 0
            else :
                if liveCellDict[key] == 3:
                    board[row][col] = 1