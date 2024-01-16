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

        value_already_removed = ( board[row][col] == 0 ) 
        if( value_already_removed ):
            continue

        board[row][col] = 0
        total_removed_values += 1
    
    return board


def generate_solved_board():

    # pattern for a baseline valid solution
    def hash(r,c): return (3*(r%3)+r//3+c)%9

    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(s): return random.sample(s,len(s)) 

    rows  = [ g*3 + r for g in shuffle(range(3)) for r in shuffle(range(3)) ] 
    cols  = [ g*3 + c for g in shuffle(range(3)) for c in shuffle(range(3)) ]

    nums  = shuffle(range(1,10))

    # produce board using randomized baseline pattern
    board = [ [nums[hash(r,c)] for c in cols] for r in rows ]

    return board