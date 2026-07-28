class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row to traverse over
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2 # calculating midpoint of l and row
            print(mid)
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            print(matrix[row][col])
            if target == matrix[row][col]:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False