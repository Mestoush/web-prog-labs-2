from flask import Flask, redirect, url_for, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from db import db
from os import path
import psycopg2
from psycopg2.extras import RealDictCursor
from db.models import users
from flask_login import LoginManager

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'danis_chervonyak_orm'
    db_user = 'denischervonyak'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'

else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "denis_cherbonyak_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

db.init_app(app)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)

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
                <li><a href="/lab8" target="_blank">Лабораторная 8</a></li>
            </ul>
        </nav>
    </main>

    <footer>
        &copy; Червоняк Денис, ФБИ-24, 3 курс, 2024
    </footer>
</body>
</html>
"""
