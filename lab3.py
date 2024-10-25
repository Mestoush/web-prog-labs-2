from flask import Blueprint, redirect, render_template, request, make_response, url_for
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', 'Аноним')
    name_color = request.cookies.get('name_color')
    age = request.cookies.get('age', 'Неизвестный возраст')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)

@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp

@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp

@lab3.route('/lab3/form')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '' or age == None or age == " ":
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/pay/success')
def pay_success():
    price = request.args.get('price', 0)
    card = request.args.get('card')
    name = request.args.get('name')
    cvv = request.args.get('cvv')
    return render_template('lab3/pay_success.html', price=price, card=card, name=name, cvv=cvv)


@lab3.route('/lab3/settings', methods=['GET', 'POST']) 
def settings():
    color = request.args.get('color')
    if color:
        resp = make_response(redirect('lab3/settings'))
        print(f"Setting cookie: {color}")  # Добавьте это перед resp.set_cookie
        resp.set_cookie('color', color)
        return resp
    
    color = request.cookies.get('color')
    resp = render_template('lab3/settings.html', color=color)
    return resp
