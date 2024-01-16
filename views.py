from flask import Blueprint,render_template
from sudoku import *
views = Blueprint(__name__,"views")

@views.route("/")
def home():
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    return render_template("index.html",x=board)

#     for line in board: return line