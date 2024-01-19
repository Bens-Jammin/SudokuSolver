

def generate_board_matrix( board: list[list[int]] ) -> str:
    '''
    generates the code for the board
    '''
    table = "<table class='sudoku-board'>"
    text_box = "<input type='number' min='1' max='9' step='1'>"
    
    for row in board:
        table += "<tr>"
        for col in row:
            if col == 0:
                table += "<td>"+text_box+"</td>"
            else:
                table += "<td>"+str(col)+"</td>"
            
        table += "</tr>"
        
    table += "</table>"
    
    return table