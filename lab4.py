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
    {'login': 'alex', 'password': '123'},
    {'login': 'bob', 'password': '345'},
    {'login': 'anton', 'password': '567'},
    {'login': 'artyom', 'password': '789'}
]

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        if 'login' in session:
            authorized = True
            login = session['login']
        else:
            authorized = False
            login = ''
        return render_template('lab4/login.html', authorized = authorized, login = login)
    
    login = request.form.get('login')
    password = request.form.get('password')

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            return redirect('/lab4/login')
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error = error, authorized = False)

@lab4.route('/lab4/logout', methods = ['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')