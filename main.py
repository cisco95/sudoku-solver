from src.board import Board
from src.solver import Solver
from puzzles import board


sudoku_puzzle = Board(board[0])


print(sudoku_puzzle)

solver = Solver()

if solver.solve(sudoku_puzzle):
    print("Solved Sudoku:")
    print(sudoku_puzzle)
else:
    print("No solution exists.")