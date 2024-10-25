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


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    background = request.args.get('background')
    font_size = request.args.get('font_size')
    header_footer_color = request.args.get('header_footer_color')  # Новое поле

    if color or background or font_size or header_footer_color:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if background:
            resp.set_cookie('background', background)
        if font_size:
            resp.set_cookie('font_size', font_size)
        if header_footer_color:
            resp.set_cookie('header_footer_color', header_footer_color) 
        return resp

    color = request.cookies.get('color')
    background = request.cookies.get('background')
    font_size = request.cookies.get('font_size')
    header_footer_color = request.cookies.get('header_footer_color')

    resp = make_response(render_template('lab3/settings.html', color=color, background=background, font_size=font_size, header_footer_color=header_footer_color))
    return resp

@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('background')
    resp.delete_cookie('font_size')
    resp.delete_cookie('header_footer_color')
    return resp


@lab3.route('/lab3/ticket', methods=['GET', 'POST'])
def ticket():
    return render_template('lab3/ticket.html')

@lab3.route('/lab3/ticket_result', methods=['POST'])
def ticket_result():
    name = request.form['name']
    polka = request.form['polka']
    age = int(request.form['age'])
    departure = request.form['departure']
    destination = request.form['destination']
    date = request.form['date']
    
    free = 'linen' in request.form
    baggage = 'baggage' in request.form
    insurance = 'insurance' in request.form

    if age < 18:
        price = 700
        ticket_type = "Детский билет"
    else:
        price = 1000
        ticket_type = "Взрослый билет"
    
    if polka in ['нижняя', 'нижняя боковая']:
        price += 100
    if free:
        price += 75
    if baggage:
        price += 250
    if insurance:
        price += 150

    return render_template('lab3/ticket_success.html', name=name, polka=polka, age=age, departure=departure, destination=destination, date=date, ticket_type=ticket_type, price=price)