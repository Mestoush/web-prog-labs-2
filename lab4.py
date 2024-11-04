from flask import Blueprint, render_template, request, url_for, redirect, session
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div', methods=['GET', 'POST'])
def div():
    if request.method == 'GET':
        return render_template('lab4/div.html')

    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены', back_url=url_for('lab4.lab'))

    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error='Деление на 0 невозможно', back_url=url_for('lab4.lab'))
    
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result, back_url=url_for('lab4.div'))

@lab4.route('/lab4/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('lab4/add.html')

    x1 = request.form.get('x1') or '0'
    x2 = request.form.get('x2') or '0'

    if x1 == '' or x2 == '':
        return render_template('lab4/add.html', error='Оба поля должны быть заполнены', back_url=url_for('lab4.lab'))

    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/add.html', error='Деление на 0 невозможно', back_url=url_for('lab4.lab'))
    
    result = x1 + x2
    return render_template('lab4/add.html', x1=x1, x2=x2, result=result, back_url=url_for('lab4.add'))


@lab4.route('/lab4/minus', methods=['GET', 'POST'])
def minus():
    if request.method == 'GET':
        return render_template('lab4/minus.html')

    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if x1 == '' or x2 == '':
        return render_template('lab4/minus.html', error='Оба поля должны быть заполнены', back_url=url_for('lab4.lab'))

    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/minus.html', error='Деление на 0 невозможно', back_url=url_for('lab4.lab'))
    
    result = x1 - x2
    return render_template('lab4/minus.html', x1=x1, x2=x2, result=result, back_url=url_for('lab4.minus'))

@lab4.route('/lab4/umnozh', methods=['GET', 'POST'])
def umnozh():
    if request.method == 'GET':
        return render_template('lab4/umnozh.html')

    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if x1 == '' or x2 == '':
        return render_template('lab4/umnozh.html', error='Оба поля должны быть заполнены', back_url=url_for('lab4.lab'))

    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/umnozh.html', error='Деление на 0 невозможно', back_url=url_for('lab4.lab'))
    
    result = x1 * x2
    return render_template('lab4/umnozh.html', x1=x1, x2=x2, result=result, back_url=url_for('lab4.umnozh'))

@lab4.route('/lab4/stepen', methods=['GET', 'POST'])
def stepen():
    if request.method == 'GET':
        return render_template('lab4/stepen.html')

    x1 = request.form.get('x1')
    x2 = request.form.get('x2')

    if x1 == '' or x2 == '':
        return render_template('lab4/stepen.html', error='Оба поля должны быть заполнены', back_url=url_for('lab4.lab'))

    x1 = int(x1)
    x2 = int(x2)
    if x2 == 0:
        return render_template('lab4/stepen.html', error='Деление на 0 невозможно', back_url=url_for('lab4.lab'))
    
    result = x1 ** x2
    return render_template('lab4/stepen.html', x1=x1, x2=x2, result=result, back_url=url_for('lab4.stepen'))

tree_count = 0

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'POST':
        operation = request.form.get('operation')

        if operation == 'cut' and tree_count > 0:
            tree_count -= 1
        elif operation == 'plant' and tree_count < 10:
            tree_count += 1

    return render_template('lab4/tree.html', tree_count=tree_count)

users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex Johnson', 'gender': 'male'},
    {'login': 'bob', 'password': '345', 'name': 'Bob Smith', 'gender': 'male'},
    {'login': 'anton', 'password': '567', 'name': 'Anton Ivanov', 'gender': 'male'},
    {'login': 'artyom', 'password': '789', 'name': 'Artyom Petrov', 'gender': 'male'}
]

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        authorized = 'login' in session
        name = session.get('name', '') if authorized else ''
        return render_template('lab4/login.html', authorized=authorized, name=name)
    
    login = request.form.get('login')
    password = request.form.get('password')
    error = None

    if not login:
        error = 'Не введён логин'
    elif not password:
        error = 'Не введён пароль'
    else:
        for user in users:
            if login == user['login'] and password == user['password']:
                session['login'] = login
                session['name'] = user['name']
                return redirect('/lab4/login')

        error = 'Неверные логин и/или пароль'
    
    return render_template('lab4/login.html', error=error, login=login)


@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    temperature = request.form.get('temperature')
    message = ""
    snow = ""

    if temperature is None:
        message = "Ошибка: не задана температура"
    else:
        try:
            temp = int(temperature)
            if temp < -12:
                message = "Не удалось установить температуру — слишком низкое значение"
            elif temp > -1:
                message = "Не удалось установить температуру — слишком высокое значение"
            elif -12 <= temp <= -9:
                message = f"Установлена температура: {temp}°С"
                snow = "❄️❄️❄️"
            elif -8 <= temp <= -5:
                message = f"Установлена температура: {temp}°С"
                snow = "❄️❄️"
            elif -4 <= temp <= -1:
                message = f"Установлена температура: {temp}°С"
                snow = "❄️"
        except ValueError:
            message = "Ошибка: температура должна быть числом"

    return render_template('lab4/fridge.html', message=message, snow=snow)
