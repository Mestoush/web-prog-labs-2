from flask import Flask, redirect, url_for, render_template, request
import os
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)

@app.route('/')


@app.route('/index')
def start():
    return redirect("/menu", code=302)


@app.route('/menu')
def menu():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Червоняк Денис Павлович, лабораторная 1</title>
    <link rel="stylesheet" href="../static/lab1.css">
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
    </header>

    <main>
        <h1>Меню:</h1>
        <nav>
            <ul>
                <li><a href="/lab1" target="_blank">Лабораторная 1</a></li>
                <li><a href="/lab2" target="_blank">Лабораторная 2</a></li>
                <li><a href="/lab3" target="_blank">Лабораторная 3</a></li>
                <li><a href="/lab4" target="_blank">Лабораторная 4</a></li>
                <li><a href="/lab5" target="_blank">Лабораторная 5</a></li>
                <li><a href="/lab6" target="_blank">Лабораторная 6</a></li>
                <li><a href="/lab7" target="_blank">Лабораторная 7</a></li>
            </ul>
        </nav>
    </main>

    <footer>
        &copy; Червоняк Денис, ФБИ-24, 3 курс, 2024
    </footer>
</body>
</html>
"""
