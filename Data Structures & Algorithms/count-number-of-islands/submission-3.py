class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # main goal: find distinct number of islands
        # approach: go through every position, mark islands completely as they are found

        def mark(row, col):
            # checking to see if island exists or values out of bounds
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
                return
            else:
                # marking current island and recursively covering others
                grid[row][col] = "*"
                mark(row - 1, col)
                mark(row, col - 1)
                mark(row + 1, col)
                mark(row, col + 1)
            
        numIslands = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    numIslands += 1
                    mark(r, c)

        return numIslands
                