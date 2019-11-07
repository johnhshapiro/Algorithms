"""Adapted from https://github.com/sol-prog/N-Queens-Puzzle
"""
import random
import time
solutions = 0

def solve(start_row):
    """Solve the n queens puzzle and print the number of solutions"""
    global solutions
    positions = legal_starting_k_queens(start_row)
    put_queen(positions, start_row)
    print("found", solutions, "solutions")

def legal_starting_k_queens(start_row):
    while True:
        # place k queens
        positions = random.sample(range(8), start_row)
        positions.extend([-1] * (8 - start_row))
        show_full_board(positions)
        current_row = 0
        for row in range(start_row):
            if check_place(positions, current_row, positions[row]):
                current_row = current_row + 1
        if current_row == start_row:
            return positions

def put_queen(positions, target_row):
    """
    Try to place a queen on target_row by checking all N possible cases.
    If a valid place is found the function calls itself trying to place a queen
    on the next row until all N queens are placed on the NxN board.
    """
    global solutions
    # Base (stop) case - all N rows are occupied
    if target_row == 8:
        # show_full_board(positions)
        show_short_board(positions)
        solutions += 1
    else:
        # For all N columns positions try to place a queen
        for column in range(8):
            # Reject all invalid positions
            if check_place(positions, target_row, column):
                positions[target_row] = column
                put_queen(positions, target_row + 1)


def check_place(positions, ocuppied_rows, column):
    """
    Check if a given position is under attack from any of
    the previously placed queens (check column and diagonal positions)
    """
    for i in range(ocuppied_rows):
        if positions[i] == column or \
            positions[i] - i == column - ocuppied_rows or \
            positions[i] + i == column + ocuppied_rows:

            return False
    return True

def show_full_board(positions):
    """Show the full NxN board"""
    for row in range(8):
        line = ""
        for column in range(8):
            if positions[row] == column:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

def show_short_board(positions):
    """
    Show the queens positions on the board in compressed form,
    each number represent the occupied column position in the corresponding row.
    """
    line = ""
    for i in range(8):
        line += str(positions[i]) + " "
    print(line)


start = time.time()
solve(0)
elapsed = time.time() - start
print(elapsed)
solutions = 0
start = time.time()
solve(4)
elapsed = time.time() - start
print(elapsed)