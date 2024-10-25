from flask import Blueprint, redirect, render_template, url_for, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/index')
def start():

    return redirect("/menu", code=302)

@lab3.route('/lab3')
def lab3_index():
    return render_template('lab3.html')