'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

def setRowColToZero(matrix,row, col):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

    for i in range(len(matrix)):
        matrix[i][col] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #add the indexs in a list of tuples
        tupleList = []
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0 :
                    tupleList.append((i,j))

        # a bit faster without use of function
        for tup in tupleList:
            for i in range(m):
                matrix[tup[0]][i] = 0
            for i in range(n):
                matrix[i][tup[1]] = 0
    

#way faster to use list for each rows and columns
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowsToZero = []
        colToZero = []

        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0 :
                    rowsToZero.append(i)
                    colToZero.append(j)

        for rowIndex in rowsToZero:
            for i in range(m):
                matrix[rowIndex][i] = 0
        
        for colIndex in colToZero:
            for i in range(n):
                matrix[i][colIndex] = 0