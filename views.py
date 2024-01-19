from flask import Blueprint,render_template,request
from sudoku import *
views = Blueprint(__name__,"views")

@views.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        return "hi"
    else:
        board = start_board(3)
        return render_template("index.html",x=board,y="  ")

#     for line in board: return line