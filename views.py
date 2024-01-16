from flask import Blueprint,render_template
from display import *
views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")