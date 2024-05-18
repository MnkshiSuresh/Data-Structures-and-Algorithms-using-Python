''' Problem Statement:------
You are given a matrix of integers and there will be Q queries. You have to write a class NumMatrix and the function sumRegion.
An object of the class NumMatrix will be created and some queries will be made. sumRegion finds the sum of the elements inside the rectangle 
defined by its upper left corner (row1, col1) and lower right corner (row2, col2).For example, Input:
Given matrix = [
[3, 0, 1, 4, 2], 
[5, 6, 3, 2, 1], 
[1, 2, 0, 1, 51, 
[4, 1, 0, 1, 71, 
[1, 0, 3, 0, 5]]
Q = 3
row1 = 2, col1 = 1, row2 = 4, col2 = 3
row1 = 1, coll = 1, row2 = 2, col2 = 2
rowl = 1, coll = 2, row2 = 2, col2 = 4  

Explanation:
sumRegion(2, 1, 4, 3) → 8 sumRegion(1, 1, 2, 2) → 11 sumRegion(1, 2, 2, 4) → 12
Input Format
* First-line takes input N and M, the size of the matrix.
* Next N lines take input M space-separated integers representing the elements of the matrix.
* The next line takes input Q.
* Next, Q lines take input space-separated integers row1,col1, row2, and col2 for Q queries.
* Q lines containing the result of Q queries.  

Input Format:
5 5 
3 0 1 4 2 
5 6 3 2 1 
1 2 0 1 5 
4 1 0 1 7 
1 0 3 0 5 
3 
2 1 4 3 
1 1 2 2 
1 2 2 4

Output Format:
8
11
12      '''



code:

class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return

        self.rows, self.cols = len(matrix), len(matrix[0])
        # Create a prefix sum matrix with an extra row and column (for easier calculations)
        self.prefix_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]

        # Fill the prefix sum matrix
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                self.prefix_sum[r][c] = (matrix[r-1][c-1] +
                                         self.prefix_sum[r-1][c] +
                                         self.prefix_sum[r][c-1] -
                                         self.prefix_sum[r-1][c-1])

    def sumRegion(self, row1, col1, row2, col2):
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (self.prefix_sum[row2][col2]
                - self.prefix_sum[row1 - 1][col2]
                - self.prefix_sum[row2][col1 - 1]
                + self.prefix_sum[row1 - 1][col1 - 1])

# Input and output handling
def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0

    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2

    matrix = []
    for i in range(N):
        row = list(map(int, data[idx:idx + M]))
        matrix.append(row)
        idx += M

    Q = int(data[idx])
    idx += 1

    queries = []
    for _ in range(Q):
        row1 = int(data[idx])
        col1 = int(data[idx + 1])
        row2 = int(data[idx + 2])
        col2 = int(data[idx + 3])
        queries.append((row1, col1, row2, col2))
        idx += 4

    numMatrix = NumMatrix(matrix)

    for row1, col1, row2, col2 in queries:
        print(numMatrix.sumRegion(row1, col1, row2, col2))

if __name__ == "__main__":
    main()
