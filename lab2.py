from flask import Blueprint, redirect, render_template, url_for, request
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/a')
def a():
    return 'без слеша'


@lab2.route('/lab2/a/')
def asl():
    return 'со слешем'


flower_list = [
    {'name': 'роза', 'price': 100},
    {'name': 'тюльпан', 'price': 50},
    {'name': 'хризантема', 'price': 70},
    {'name': 'астра', 'price': 60}
]


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return 'нет такого цветка', 404
    flower = flower_list[flower_id]
    return render_template('/lab2/flower.html', flower_name=flower['name'], flower_price=flower['price'], flower_id=flower_id)

    
@lab2.route('/lab2/add_flower', methods=['POST'])
def add_flower():
    flower_name = request.form['flower_name']
    flower_price = int(request.form['flower_price'])
    flower_list.append({'name': flower_name, 'price': flower_price})
    return redirect(url_for('all_flowers'))


@lab2.route('/lab2/flowers')
def all_flowers():
    return render_template('/lab2/all_flowers.html', flowers=flower_list, total_flowers=len(flower_list))


@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return redirect(url_for('/lab2/all_flowers'))


@lab2.route('/lab2/delete_flowers/<int:flower_id>')
def delete_flower(flower_id):
    if flower_id >= len(flower_list):
        return 'нет такого цветка', 404
    del flower_list[flower_id]
    return redirect(url_for('/lab2/all_flowers'))


@lab2.route('/lab2/example')
def example():
    name = 'Червоняк Денис'
    lab_number = '№2'
    group = 'ФБИ-24'
    course = '3'
    fruits = [
        {'name' : 'яблоки', 'price' : 123},
        {'name' : 'груши', 'price' : 45},
        {'name' : 'бананы', 'price' : 235},
        {'name' : 'апельсины', 'price' : 526},
        {'name' : 'манго', 'price' : 431}]
    return render_template('/lab2/examples.html', name = name, lab_number = lab_number, group = group, course = course, fruits = fruits)


@lab2.route('/lab2')
def lab2_index():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/filtres')
def filres():
    phrase = '0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('lab2/filter.html', phrase = phrase)

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    try:
        sum_result = a + b
        sub_result = a - b
        mul_result = a * b
        div_result = a / b if b != 0 else 'деление на 0 невозможно'
        pow_result = a ** b
    except Exception as e:
        return f'Ошибка: {str(e)}'

    return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Калькулятор</title>
        </head>
        <body>
            <h1>Результаты операций с числами {a} и {b}</h1>
            <p>Сумма: {sum_result}</p>
            <p>Разность: {sub_result}</p>
            <p>Произведение: {mul_result}</p>
            <p>Деление: {div_result}</p>
            <p>Возведение в степень: {pow_result}</p>
        </body>
        </html>
    '''

@lab2.route('/lab2/calc/')
def default_calc():
    return redirect('/lab2/calc/1/1')

@lab2.route('/lab2/calc/<int:a>')
def calc_with_default_b(a):
    return redirect(f'/lab2/calc/{a}/1')

@lab2.route('/lab2/books')
def books():
    books = [
        {'author': 'Майк Омер', 'title': 'Внутри убийцы', 'genre': 'Детективный роман', 'pages': 416},
        {'author': 'Майк Омер', 'title': 'Заживо в темноте', 'genre': 'Детективный роман', 'pages': 448},
        {'author': 'Майк Омер', 'title': 'Глазами жертвы', 'genre': 'Детективный роман', 'pages': 328},
        {'author': 'Джексон Холли', 'title': 'Хороших девочек не убивают', 'genre': 'Детектив', 'pages': 398},
        {'author': 'Джексон Холли', 'title': 'Хорошая девочка, дурная кровь', 'genre': 'Детектив', 'pages': 208},
        {'author': 'Джексон Холли', 'title': 'Хорошая девочка должна умереть', 'genre': 'Детектив', 'pages': 448},
        {'author': 'Роулинг Дж.К.', 'title': 'Гарри Поттер и философский камень', 'genre': 'Фэнтези', 'pages': 320},
        {'author': 'Толстой Л.Н.', 'title': 'Война и мир', 'genre': 'Роман', 'pages': 1225},
        {'author': 'Достоевский Ф.М.', 'title': 'Преступление и наказание', 'genre': 'Роман', 'pages': 671},
    ]
    return render_template('/lab2/books.html', books=books)


@lab2.route('/lab2/cars')
def show_cars():
    cars = [
        {'name': 'Tesla Model S', 'description': 'Электрический седан с высоким запасом хода', 'image': 'tesla_model_s.jpg'},
        {'name': 'BMW M5', 'description': 'Самый быстрый спортивный седан с мире', 'image': 'bmw_m5.jpg'},
        {'name': 'Audi R8', 'description': 'Высокоскоростной суперкар с двигателем V10', 'image': 'audi_r8.jpg'},
        {'name': 'Mercedes S-Class', 'description': 'Роскошные седан премиум-класса', 'image': 'mercedes_s_class.jpg'},
        {'name': 'KIA Sorento', 'description': 'Корейский внедорожник', 'image': 'sorento.jpg'}
    ]
    return render_template('/lab2/cars.html', cars=cars)
