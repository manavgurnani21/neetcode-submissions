class Solution:
    def checkRows(self, board) -> bool:
        for row in board: # checking each sub array (row)
            sudoku_nums = defaultdict(int)
            for idx in range(len(row)): # for each value in row
                if row[idx] != ".":
                    if int(row[idx]) in sudoku_nums:
                        print(f"Duplicate found at row {row} and column {idx}")
                        return False
                    sudoku_nums[int(row[idx])] = idx
                    print(f"Adding value {int(row[idx])} in index [{idx}]")
        return True

    # checking columns
    def checkCols(self, board) -> bool:
        for i in range(len(board)):
            sudoku_nums = defaultdict(int)
            for j in range(len(board[i])):
                if board[j][i] != ".":
                    if int(board[j][i]) in sudoku_nums:
                        print(f"Duplicate found at row {j} and column {i}")
                        return False
                    else:
                        sudoku_nums[int(board[j][i])] = [i, j]
                        print(f"Adding value {int(board[j][i])} in idx [{i}][{j}]")
        return True

    def checkGrids(self, board) -> bool:
        for square in range(len(board)):
            sudoku_nums = defaultdict(int)
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] != ".":
                        if int(board[row][col]) in sudoku_nums:
                            print(f"Duplicate found at row {row} and column {col}")
                            return False
                        else:
                            sudoku_nums[int(board[row][col])] = [row, col]
                            print(f"Adding value {int(board[row][col])} in idx [{row}][{col}]")
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkGrids(board)