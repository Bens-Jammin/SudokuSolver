
def display( board: list[list[int]] ) -> None:
    for row in board:
        formatted_row = ""
        for col in row:
            if col == -1:
                formatted_row += "[ ]"
                continue

            formatted_row += "["+str(col)+"]"
        print( formatted_row )


# print("easy:")
# display( start_board(0) )
# print("\nmedium:")
# display( start_board(1) )
# print("\nhard:")
# display( start_board(2) )
# print("\nexpert:")
# display( start_board(3) )
