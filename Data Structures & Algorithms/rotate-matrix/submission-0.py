class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # transpose calculation
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                # only swap for upper triangle
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        # reflection across rows
        l = 0
        r = len(matrix) - 1
        while l < r:
            # swap values between left and right columns
            for row in range(len(matrix)):
                temp = matrix[row][l]
                matrix[row][l] = matrix[row][r]
                matrix[row][r] = temp
            l += 1
            r -= 1
