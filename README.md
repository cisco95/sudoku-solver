# Sudoku Solver

A Python-based Sudoku-solving framework built to explore recursive search algorithms, software architecture, testing practices, and advanced puzzle-solving techniques.

This project currently implements a complete recursive backtracking solver capable of solving standard 9×9 Sudoku puzzles. It is being developed as an ongoing software engineering and algorithm design project, with future plans to incorporate automated testing, solver metrics, human-style solving strategies, and performance optimizations.

---

## Project Status

🚧 Active Development

### Current Features

- Recursive backtracking solver
- Sudoku rule validation
- Object-oriented board representation
- Console-based puzzle display
- Modular project architecture
- Support for loading and solving multiple puzzles

### Planned Features

- Automated test suite using pytest
- Solver performance statistics
- Human-style solving techniques
  - Naked Singles
  - Hidden Singles
  - Naked Pairs
  - Hidden Pairs
  - Additional advanced strategies
- Difficulty classification
- Puzzle benchmarking
- Interactive user interface
- Multiple solving algorithms for comparison

---

## Motivation

Sudoku is a classic constraint satisfaction problem that provides an excellent opportunity to practice algorithm design and software architecture.

Rather than building a single-purpose script, this project is structured as a reusable and extensible framework. The goal is to create a codebase that can evolve from a simple backtracking solver into a platform for experimenting with different Sudoku-solving techniques and optimization strategies.

---

## Features

### Recursive Backtracking Solver

The current implementation uses depth-first search with recursive backtracking.

The solver:

1. Finds the next empty cell.
2. Tries values 1 through 9.
3. Validates each move.
4. Recursively attempts to solve the remaining board.
5. Backtracks when a contradiction is encountered.

This approach guarantees a solution for any valid, solvable Sudoku puzzle.

### Board Management

The `Board` class encapsulates all puzzle state and provides utility methods for:

- Reading cell values
- Updating cells
- Identifying empty spaces
- Displaying puzzles in a human-readable format

### Move Validation

The validation system enforces Sudoku constraints by ensuring:

- No duplicate values in a row
- No duplicate values in a column
- No duplicate values within a 3×3 subgrid

---

## Example Puzzle

### Input

```text
      2 6   7   1
6 8     7     9
1 9         4 5

8 2   1       4
    4 6   2 9
  5         2 8

    9 3       7 4
  4     5     3 6
7   3   1 8
```

### Output

```text
4 3 5 2 6 9 7 8 1
6 8 2 5 7 1 4 9 3
1 9 7 8 3 4 5 6 2
8 2 6 1 9 5 3 4 7
3 7 4 6 8 2 9 1 5
9 5 1 7 4 3 6 2 8
5 1 9 3 2 6 8 7 4
2 4 8 9 5 7 1 3 6
7 6 3 4 1 8 2 5 9
```

---

## Project Structure

```text
sudoku_solver/
│
├── docs/
│
├── src/
│   ├── board.py
│   ├── solver.py
│   └── validate.py
│
├── tests/
│   └── test_solver.py
│
├── main.py
├── puzzles.py
└── README.md
```

---

## Architecture

The project follows a modular design that separates puzzle management, validation, and solving logic into independent components.

### Board

**File:** `src/board.py`

Responsible for:

- Storing puzzle state
- Accessing board values
- Updating board values
- Finding empty cells
- Formatting board output

Key methods:

```python
get(row, col)
set(row, col, value)
is_empty(row, col)
next_empty()
```

---

### Validator

**File:** `src/validate.py`

Responsible for enforcing Sudoku rules.

Checks:

- Rows
- Columns
- 3×3 boxes

Key method:

```python
Validator.is_valid(board, row, col, num)
```

---

### Solver

**File:** `src/solver.py`

Responsible for solving the puzzle through recursive search.

Key method:

```python
solve(board)
```

The solver delegates rule checking to the Validator and board management to the Board class.

---

### Entry Point

**File:** `main.py`

Responsibilities:

1. Load puzzle data
2. Create a Board instance
3. Initialize a Solver
4. Solve the puzzle
5. Display results

---

### Puzzle Definitions

**File:** `puzzles.py`

Contains puzzle data and serves as the source for Sudoku boards loaded by the application.

The structure allows multiple puzzles to be added and solved without modifying solver logic.

---

## Solver Algorithm

### Backtracking Search

The current solver uses recursive backtracking.

Pseudo-process:

```text
Find an empty cell

For each value 1-9:
    Check if valid
    Place value

    Recursively solve remaining puzzle

    If solved:
        Return success

    Otherwise:
        Remove value

Return failure
```

### Why Backtracking?

Advantages:

- Guaranteed correctness
- Simple and maintainable implementation
- Works on virtually any valid Sudoku puzzle
- Excellent demonstration of recursion and search algorithms

Limitations:

- Does not emulate human solving techniques
- May perform unnecessary searches on difficult puzzles
- Can be optimized through constraint propagation and heuristic selection

Future development will focus on addressing these limitations.

---

## Design Goals

This project is intended to demonstrate:

### Software Engineering Skills

- Object-oriented programming
- Separation of concerns
- Modular architecture
- Maintainable code organization
- Extensibility

### Algorithmic Thinking

- Recursive algorithms
- Backtracking
- Constraint satisfaction problems
- State-space search
- Problem decomposition

### Development Practices

- Git and GitHub workflow
- Automated testing
- Incremental feature development
- Documentation
- Refactoring and optimization

---

## Requirements

- Python 3.9+

No external dependencies are currently required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/cisco95/sudoku-solver.git
```

Move into the project directory:

```bash
cd sudoku-solver
```

---

## Usage

Run the application:

```bash
python main.py
```

The program will:

1. Display the original puzzle.
2. Solve the puzzle.
3. Display the completed solution.

If no valid solution exists:

```text
No solution exists.
```

will be displayed.

---

## Testing

A dedicated testing structure has been created and will be expanded as development continues.

Planned test coverage includes:

- Board operations
- Validation logic
- Solver correctness
- Invalid puzzle detection
- Unsolvable puzzle handling
- Edge cases

Future testing will be implemented using:

```bash
pytest
```

---

## Future Roadmap

### Phase 1: Test Coverage

- Unit tests for Board
- Unit tests for Validator
- Unit tests for Solver
- Regression testing

### Phase 2: Solver Metrics

Track and display:

- Recursive calls
- Backtracking operations
- Solution time
- Search efficiency

### Phase 3: Human-Style Solving

Implement logic-based techniques before invoking brute-force search:

- Naked Singles
- Hidden Singles
- Naked Pairs
- Hidden Pairs
- Pointing Pairs
- Additional advanced methods

### Phase 4: Performance Optimization

- Candidate tracking
- Constraint propagation
- Heuristic cell selection
- Search-space reduction

### Phase 5: User Experience Enhancements

- Interactive CLI
- Puzzle import/export
- Difficulty ratings
- Solve visualization
- Graphical interface

---

## Skills Demonstrated

- Python
- Object-Oriented Programming
- Recursion
- Backtracking Algorithms
- Data Structures
- Constraint Satisfaction Problems
- Software Design
- Modular Architecture
- Git
- GitHub
- Test Planning
- Technical Documentation

---

## Lessons Learned

This project has provided hands-on experience with recursive search algorithms, Sudoku constraint validation, and software architecture principles. By separating implementation into specialized modules, the codebase remains readable, maintainable, and ready for future enhancements.

As development continues, the project will serve as a platform for exploring advanced solving techniques, testing methodologies, and performance optimization strategies.

---

## License

This project is available for educational and personal use.