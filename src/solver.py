from .validate import Validator

class Solver:
    def solve(self, board):
        empty_cell = board.next_empty()
        if not empty_cell:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if Validator.is_valid(board, row, col, num):
                board.set(row, col, num)

                if self.solve(board):
                    return True

                board.set(row, col, 0)

        return False