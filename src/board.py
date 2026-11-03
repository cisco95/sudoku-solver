class Board:
    SIZE = 9

    def __init__(self, board):
        self.board = board

    def get(self, row, col):
        return self.board[row][col]

    def set(self, row, col, value):
        self.board[row][col] = value

    def __str__(self):
        lines = ""
        for row in range(self.SIZE):
            if row != 0 and row % 3 == 0:
                lines += "-" * 21 + "\n"

            current = ""
            for col in range(self.SIZE):
                if col != 0 and col % 3 == 0:
                    current += "|"

                value = self.get(row, col)
                if value == 0:
                    current += " "
                else:
                    current += str(value)

            lines += " ".join(current) + "\n"
        return lines;

    def is_empty(self, row, col):
        return self.get(row, col) == 0

    def next_empty(self):
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                if self.is_empty(row, col):
                    return row, col
        return None






