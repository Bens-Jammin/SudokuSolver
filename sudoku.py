import random
import display

def start_board(difficulty_number: int) -> list[list[int]]:
    """
    generates the sudoku board based on a difficulty number.
    The function works by generating a solved board, then removing
    numbers based on the difficulty. 
    
    here is how the argument integer relates to the 
    difficulty and how many numbers are removed:

    0 -> easy ( 35 )

    1 -> medium ( 45 )
    
    2 -> hard ( 55 )
    
    3 -> expert ( 65 )
    
    param: difficulty (int) -> the difficulty of the board to be generated
    returns: an integer matrix for the sudoku board 
    """
    board = generate_solved_board()

    number_to_remove = 0
    
    match difficulty_number:
        case 0: # easy
            number_to_remove = 35
        case 1: # medium
            number_to_remove = 45
        case 2: # mard
            number_to_remove = 55
        case 3: # expert
            number_to_remove = 65


    return remove_random_values( number_to_remove, board )
    
    


def remove_random_values( number_of_values_to_remove: int, board: list[list[int]] ) -> list[list[int]]:

    total_removed_values = 0

    while total_removed_values < number_of_values_to_remove:
        row = random.randint( 0, 8 )
        col = random.randint( 0, 8 )

        value_already_removed = ( board[row][col] == -1 ) 
        if( value_already_removed ):
            continue

        board[row][col] = -1
        total_removed_values += 1
    
    return board



def generate_solved_board():
    board = [[0 for i in range(9)] for j in range(9)]

    numbers = [1,2,3,4,5,6,7,8,9]
    while True:
            
        for i in range(9):
            random.shuffle( numbers )
            board[i] = numbers
            


        if is_valid_board(board):
            break
    return board


def is_valid_board(board):
    for row in board:
       if len(set(row)) != 9:
           return False

   # Check columns
    for col in zip(*board):
        if len(set(col)) != 9:
            return False

    # Check boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            for x in range(3):
                for y in range(3):
                    box.append(board[i+x][j+y])
            if len(set(box)) != 9:
                return False

    return True
        


generate_solved_board()