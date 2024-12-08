import json

empty_board = {
    "board" :[
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    }

def read_board(filename):
    '''Reads a board from a specified file and returns the board as a JSON.'''
    
    # Attempt to read the file.
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data['board']
    except:
        print(f"ERROR: '{filename}' could not be read.")
        return empty_board["board"]

def save_board(filename, board):
    '''Saves a passed board to a specified file.'''

    # If no filename is passed, create a place to save the board.
    if filename == "":
        filename = "dump.json"

    # Open the file.
    with open(filename, 'w') as file: 
        
        # Save the JSON data into the file.
        json.dump({
            'board': board
            }, file)

def print_error(err_type, err_value):
    '''Accepts an error type and value, and prints an appropriate error 
        message.'''
    
    # Pre-processing asserts.
    assert err_type in("invalid_square", "invalid_value", "filled")
    assert type(err_value) in(str, tuple, int)

    if err_type == "invalid_square":
        print(f"ERROR: Square {err_value} is invalid")
    elif err_type == "invalid_value":
        print(f"ERROR: The value {err_value} is invalid")
    else:
        row = err_value[0]
        col = err_value[1]
        # err_value is "*#"
        print("ERROR: Square",
              f"{chr(col + ord('A'))}{row + 1}",
                "is filled")

def parse_pos(pos):
    '''Convert a string of characters to a position tuple.'''

    # Set initial values as invalid values.
    col = -1
    row = -1

    # The only correct format will have only 2 characters; a letter and a
    # number.
    if type(pos) == str and len(pos) == 2:
        for letter in pos:
            if "A" <= letter.upper() <= "Z":

                # ensure there's only one letter in pos.
                if col == -1:
                    col = ord(letter.upper()) - ord("A")
                else:
                    print_error("invalid_square", pos)
                    return (-1, -1)
            if letter.isdigit():

                # Have to separate here for error printing.
                if 1 <= int(letter) <= 9:

                    # Ensure there's only one number in pos
                    if row == -1:
                        row = int(letter) - 1
                    else:
                        print_error("invalid_square", pos)
                        return (-1, -1)
                else:  
                    print_error("invalid_square", pos)
                    return (-1, -1)
        
    # If it made it this far, the input is a valid square.
    if row != -1 and col != -1:
        return (row, col)
    
    # If it was invalid, return preset invalid value.
    else:
        print_error("invalid_square", pos)
        return (-1, -1)

def get_possible_values(board, row, col):
    '''Will determine the possible values for a given square on the board.'''
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i_value in range(1, 10):
        is_found = False
    
        # Check row
        if i_value in(board[row]):
            is_found = True
            values.remove(i_value)
        
        # Check column if not yet found.
        if not is_found:
            
            # It has to iterate through the rows, since the column is static.
            for i_row in range(0, 9):
                if board[i_row][col] == i_value:
                    is_found = True
                    values.remove(i_value)

        # Check block if not yet found. We can ignore squares in the same
        # row and column in the block, since we've already checked them.
        if not is_found:
            block_row_start = (row // 3) * 3
            block_col_start = (col // 3) * 3

            # Check the rows in the block we haven't checked yet.
            for i_row in range(block_row_start, block_row_start + 3):
                if i_row % 3 != row % 3:
                    
                    # Check the columns in the block we haven't checked yet.
                    for i_col in range(block_col_start, block_col_start + 3):
                        if i_col % 3 != col % 3:
                            if board[i_row][i_col] == i_value and i_value in values:
                                values.remove(i_value)
    return values

def get_value(row, col):
    '''Will get a value from the user.'''
    value = ""
    value = input(
        f"What is the value at '{chr(col + ord('A'))}{row + 1}': ")

    # In the final version of this, the value must also be in 
    # possible values.
    if value.isnumeric() and 0 < int(value) < 10:
        return int(value)
    else:
        print_error("invalid_value", value)
    return -1

def display(board):
    '''Display the current board.'''
    print("   A B C D E F G H I")
    for i_row in range(0, 9):
        if i_row == 3 or i_row == 6:
            print("   -----+-----+-----")
        print(f"{i_row + 1}  ", end="")

        for i_col in range(0, 9):
            separator = "  |  |  \n"
            print(board[i_row][i_col] if board[i_row][i_col] != 0 else " ",
                   end="")
            print(separator[i_col], end="") 

def play_game(board):
    '''Plays the game of Sudoku.'''
    pos = input("> ")
    if pos.upper() != "Q":
        (row, col) = parse_pos(pos)

        # Do things if pos was valid.
        if (row, col) != (-1, -1):

            # Do things if the square is empty.
            if board[row][col] == 0:

                # Calculate possible values in this spot.
                possible_values = get_possible_values(board, row, col)
        
                value = get_value(row, col)
                if value in possible_values:
                    board[row][col] = value
                
                # If the value wasn't returned as invalid, it must not be a valid
                # value. Therefore, we still need to print an invalid value error
                # message.
                elif value != -1:
                    print_error("invalid_value", value)
            else:
                print_error("filled", (row, col))

        # If the user entered 'Q', return false. Otherwise, return true.
        return True
    return False

def game_done(board):
    '''Will determine if the Sudoku board is complete. For now, it will
    only check if there are any empty spaces in the board.'''
    is_board_finished = True
    for row in board:
        if 0 in row:
            is_board_finished = False
    return is_board_finished
    
def main():

    # At the beginning of the game, ask what board they're playing.
    filename = input("Where is your board located? ")
    board = read_board(filename)
    assert board != ""
    
    # Start the game loop.
    is_playing = True
    while is_playing:
        display(board)
        is_playing = play_game(board) and not game_done(board)
    
    # When they're done, save the board. and end the program.
    filename = input("Where would you like to save your game? ")
    save_board(filename, board)

if __name__ == "__main__":
    main()
