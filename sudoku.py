import random


def start_board(difficulty_number: int) -> list[list[int]]:
    """
    generates the sudoku board based on a difficulty number.
    The function works by generating a solved board, then removing
    numbers based on the difficulty. 
    
    here is how the argument integer relates to the 
    difficulty and how many numbers are removed:

    0 -> easy (  )

    1 -> medium (  )
    
    2 -> hard (  )
    
    3 -> expert (  )
    
    param: difficulty (int) -> the difficulty of the board to be generated
    returns: an integer matrix for the sudoku board 
    """
    board = generate_solved_board()

    number_to_remove = 0
    
    match difficulty_number:
        case 0: # easy
            number_to_remove = 32
        case 1: # medium
            number_to_remove = 45
        case 2: # mard
            number_to_remove = 50
        case 3: # expert
            number_to_remove = 56


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

    board = [
        [1,2,3,4,5,6,7,8,9],
        [9,1,2,3,4,5,6,7,8],
        [8,9,1,2,3,4,5,6,7],
        [7,8,9,1,2,3,4,5,6],
        [6,7,8,9,1,2,3,4,5],
        [5,6,7,8,9,1,2,3,4],
        [4,5,6,7,8,9,1,2,3],
        [3,4,5,6,7,8,9,1,2],
        [2,3,4,5,6,7,8,9,1]
    ]

    board_is_valid = False
    while not board_is_valid:
        random.shuffle(board)
        board_is_valid = verify_valid_board( board )

    return board



def verify_valid_board( board: list[list[int]] ) -> bool :

    all_rows_valid = verify_rows( board )
    all_columns_valid = verify_columns( board )
    all_squares_valid = verify_squares( board )

    return all_rows_valid and all_columns_valid and all_squares_valid



def verify_rows( board: list[list[int]] ) -> bool:
    
    valid_numbers = {1,2,3,4,5,6,7,8,9}
    seen_numbers = set()

    for rows in board:
        for num in rows:
            if ( num in valid_numbers ) and (num not in seen_numbers):
                seen_numbers.add(num)
            else:
                return False
            
        seen_numbers.clear()
    
    return True


def verify_columns( board: list[list[int]] ) -> bool:

    valid_numbers = {1,2,3,4,5,6,7,8,9}
    seen_numbers = set()

    for column_number in range( 9 ):
        for row_number in range( 9 ):
            num = board[row_number][column_number]

            if ( num in valid_numbers ) and (num not in seen_numbers):
                seen_numbers.add(num)
            else:
                return False
            
        seen_numbers.clear()

    return True


def verify_squares( board: list[list[int]] ) -> bool:

    valid_numbers = {1,2,3,4,5,6,7,8,9}
    seen_numbers = set()

    squares = [
        [(0,0), (0,1), (0,2),
         (1,0), (1,1), (1,2),
         (2,0), (2,1), (2,2)
        ],
        [(0,3), (0,4), (0,5),
         (1,3), (1,4), (1,5),
         (2,3), (2,4), (2,5)
        ],
        [(0,6), (0,7), (0,8),
         (1,6), (1,7), (1,8),
         (2,6), (2,7), (2,8)
        ],
        [(3,0), (3,1), (3,2),
         (4,0), (4,1), (4,2),
         (5,0), (5,1), (5,2)
        ],
        [(3,3), (3,4), (3,5),
         (4,3), (4,4), (4,5),
         (5,3), (5,4), (5,5)
        ],
        [(3,6), (3,7), (3,8),
         (4,6), (4,7), (4,8),
         (5,6), (5,7), (5,8)
        ],
        [(6,0), (6,1), (6,2),
         (7,0), (7,1), (7,2),
         (8,0), (8,1), (8,2)
        ],
        [(6,3), (6,4), (6,5),
         (7,3), (7,4), (7,5),
         (8,3), (8,4), (8,5)
        ],
        [(6,6), (6,7), (6,8),
         (7,6), (7,7), (7,8),
         (8,6), (8,7), (8,8)
        ]
    ]

    for square in squares:
            seen_numbers.clear()  
            for row, col in square:
                num = board[row][col]

                if (num in valid_numbers) and (num not in seen_numbers):
                    seen_numbers.add(num)
                else:
                    return False
    
    return True


generate_solved_board()