from flask import Flask, redirect, url_for, render_template, request
from lab1 import lab1
from lab2 import lab2

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)

@app.route('/')
@lab1.route('/index')
def start():

    return redirect("/menu", code=302)

