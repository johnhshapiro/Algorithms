"""John Shapiro
5. Eight Queens
Adapted from https://github.com/sol-prog/N-Queens-Puzzle

Finds all 92 solutions of the 8 queens problem using back tracking.
Times how long it takes to find all 92 solutions when using random starting positions for various numbers of k < 9 queens.
"""
import random
import time
import copy
solutions = 0
boards = []

def solve(start_row):
    """Solve the n queens puzzle and print the number of solutions"""
    global solutions
    global boards
    boards = []
    solutions = 0
    while solutions < 92:
        positions = legal_starting_k_queens(start_row)
        put_queen(positions, start_row)

def legal_starting_k_queens(start_row):
    """Check if the starting positions of k glued queens are legal
    
    Arguments:
        start_row {int} -- Number of rows to glue random queens on
    
    Returns:
        [int] -- List of legal starting positions
    """
    while True:
        # place k queens
        positions = random.sample(range(8), start_row)
        positions.extend([-1] * (8 - start_row))
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
    global boards
    # Base (stop) case - all N rows are occupied
    if target_row == 8:
        # show_full_board(positions)
        # show_short_board(positions)
        if positions not in boards:
            boards.append(copy.copy(positions))
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

def run_tests():
    """Run each number of k glued queens 10 times and print the elapsed time.
    """
    for test in range(9):
        start = time.time()
        for i in range(10):
            solve(test)
        elapsed = time.time() - start
        print("{:.4}".format(elapsed))

run_tests()