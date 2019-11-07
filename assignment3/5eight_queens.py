"""Adapted from https://github.com/sol-prog/N-Queens-Puzzle
"""
import random
solutions = 0

def solve(start_row):
    """Solve the n queens puzzle and print the number of solutions"""
    global solutions
    # Place k queens, 1 in each row
    positions = random.sample(range(8), start_row)
    positions.extend([-1] * (8 - start_row))
    show_full_board(positions)
    glued_queens_legal = True
    current_row = 0
    for row in range(start_row):
        # Reject all invalid positions
        if not check_place(positions, current_row, positions[row]):
            glued_queens_legal = False
            break
        current_row = current_row + 1
    if glued_queens_legal:
        put_queen(positions, start_row)
    print(solutions)

def put_queen(positions, target_row):
    """
    Try to place a queen on target_row by checking all N possible cases.
    If a valid place is found the function calls itself trying to place a queen
    on the next row until all N queens are placed on the NxN board.
    """
    global solutions
    # Base (stop) case - all N rows are occupied
    if target_row == 8:
        show_full_board(positions)
        # show_short_board(positions)
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

solve(3)