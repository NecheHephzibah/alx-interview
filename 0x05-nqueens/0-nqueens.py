#!/usr/bin/python3
"""A program that solves the N queens problem."""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    num_queens = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if num_queens < 4:
    print("N must be at least 4")
    exit(1)


def is_safe(board, row, col):
    """Check if it's safe to place a queen on board[row][col]"""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, num_queens, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    """Recursive function to solve the N Queens problem"""
    # Base case: If all queens are placed, return True
    if col == num_queens:
        solutions.append([])
        for i in range(num_queens):
            for j in range(num_queens):
                if board[i][j] == 1:
                    solutions[-1].append([i, j])
        return True

    # Try placing this queen in all rows of the current column
    for i in range(num_queens):
        if is_safe(board, i, col):
            board[i][col] = 1
            # Recur to place rest of the queens
            solve_n_queens(board, col + 1)
            # If placing queen here doesn't lead to a solution,
            # remove the queen
            board[i][col] = 0

    return False


def print_solutions(solutions):
    """Print all solutions to the N Queens problem"""
    solutions.sort()
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    solutions = []
    board = [[0 for x in range(num_queens)] for x in range(num_queens)]
    solve_n_queens(board, 0)
    print_solutions(solutions)
