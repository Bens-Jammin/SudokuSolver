from flask import Blueprint,render_template,request
from sudoku import *
import html_generator as html
views = Blueprint(__name__,"views")

@views.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        userin = request.form["in"]
        return "hi"
    else:
        board = start_board(3)
        board = html.generate_board_matrix(board)
        return render_template("index.html",sudoku_board = board)

#     for line in board: return line