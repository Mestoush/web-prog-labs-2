from flask import Flask, redirect, url_for
app = Flask(__name__)

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
            </ul>
        </nav>
    </main>

    <footer>
        &copy; Червоняк Денис, ФБИ-24, 3 курс, 2024
    </footer>
</body>
</html>
"""

@app.route('/lab1')
def lab1():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Червоняк Денис Павлович, лабораторная 1</title>
</head>
<body>
    <header>
        НГТУ, ФБ, Лабораторная работа 1
    </header>

    <h1>web-сервер на flask</h1>

    <p>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
    </p>

    <footer>
        &copy; Червоняк Денис, ФБИ-24, 3 курс, 2024
    </footer>
</body>
</html>
"""

@app.route('/lab1/oak')
def oak():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oak</title>
    <link rel="stylesheet" href="../static/lab1.css">
</head>
<body>
    <h1>Дуб</h1>
    <img src="''' + url_for('static', filename='oak.jpeg') + '''" alt="" srcset="">
</body>
</html>
'''