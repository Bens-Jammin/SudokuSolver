from flask import Blueprint,render_template
from sudoku import *
views = Blueprint(__name__,"views")

@views.route("/")
def home():
    board = start_board(3)
    return render_template("index.html",x=board)

#     for line in board: return line