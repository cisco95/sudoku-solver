class Validator:

    @staticmethod
    def is_valid(board, row, col, num):
        # Check if num is not in the current row or column
        for x in range(board.SIZE):
            if board.get(row, x) == num or board.get(x, col) == num:
                return False

        # Check if num is not in the current 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board.get(i, j) == num:
                    return False

        return True