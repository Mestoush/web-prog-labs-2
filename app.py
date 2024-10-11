from flask import Flask, redirect, url_for, render_template
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
    <link rel="stylesheet" href="../static/lab1.css">
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
    <li><a href="/menu" target="_blank">Меню</a></li>

    <h1>Реализованные роуты</h1>

    <nav>
        <ul>
            <li><a href="/lab1/oak" target="_blank">Дуб</a></li>
            <li><a href="/lab1/python" target="_blank">Python</a></li>
            <li><a href="/lab1/s7air" target="_blank">S7 Airlines</a></li>
        </ul>
    </nav>

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
    <img class='oak' src="''' + url_for('static', filename='oak.jpeg') + '''" alt="" srcset="">
</body>
</html>
'''

@app.route('/lab1/student')
def student():
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
    <h1>Червоняк Денис Павлович</h1>
    <img class='nstu' src="''' + url_for('static', filename='logo.png') + '''" alt="" srcset="">
</body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>python</title>
    <link rel="stylesheet" href="../static/lab1.css">
</head>
<body>
    <h1>Язык программирования python</h1>
    <p>
        Python — мультипарадигмальный высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[14][15], ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[16]. Язык является полностью объектно-ориентированным в том плане, что всё является объектами[14]. Необычной особенностью языка является выделение блоков кода отступами[17]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[16]. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[14]. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++[14][16].
        </p>
        <p>
        Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, объектно-ориентированное программирование[14], метапрограммирование[18], функциональное программирование[14] и асинхронное программирование[19]. Задачи обобщённого программирования решаются за счёт динамической типизации[20][21]. Аспектно-ориентированное программирование частично поддерживается через декораторы[22], более полноценная поддержка обеспечивается дополнительными фреймворками[23]. Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений[24]. Основные архитектурные черты — динамическая типизация, автоматическое управление памятью[14], полная интроспекция, механизм обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора (GIL)[25], высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты[26].
    </p>
    <img class='python' src="''' + url_for('static', filename='images.jpeg') + '''" alt="" srcset="">
</body>
</html>
'''

@app.route('/lab1/s7air')
def s7air():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S7 Airlines</title>
    <link rel="stylesheet" href="../static/lab1.css">
</head>
<body>
    <h1>Авиакомпания S7 Airlines</h1>
    <p>
       S7 Airlines (рус. эс сэвэн эйрлайнс, юридическое наименование: Акционерное общество «Авиакомпания „Сибирь“») — российская авиакомпания, выполняет внутренние и международные пассажирские авиаперевозки, входит в перечень системообразующих организаций России[6], является крупнейшей частной авиакомпанией России. Штаб-квартира расположена в Новосибирске.
    </p>
    <p>
        Входит в российский холдинг S7 Group. До апреля 2022 года являлась членом глобального авиационного альянса Oneworld, по состоянию на август 2024 года членство приостановлено.
    </p>
    <p>
        Маршрутная сеть авиакомпании выстроена на базе авиатранспортных узлов, расположенных в аэропортах Домодедово (Москва) и Толмачёво (Новосибирск), по состоянию на 2016 год охватывала 205 направлений и 181 город в 26 странах мира 
    </p>
    <img src="''' + url_for('static', filename='s7.jpg') + '''" alt="" srcset="">
</body>
</html>
'''

@app.route('/lab2/a')
def a():
    return 'без слеша'

@app.route('/lab2/a/')
def asl():
    return 'со слешем'

flower_list = ['роза', 'тюлбпан', 'хризонтема', 'астра']

@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return 'нет такого цветка', 404
    else:
        return f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Цветок {flower_list[flower_id]}</title>
            </head>
            <body>
                <h1>Цветок: {flower_list[flower_id]}</h1>
                <p>Порядковый номер цветка: {flower_id}</p>
                <a href="/lab2/flowers">Посмотреть все цветы</a>
            </body>
            </html>
        '''
    
@app.route('/lab2/add_flower/', defaults={'name': None})
@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    if not name:
        return 'вы не задали имя цветка', 400
    flower_list.append(name)
    return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Цветок {name}</title>
        </head>
        <body>
            <h1>Добавлен новый цветок</h1>
            <p>Название нового цветка: {name}</p>
            <p>Всего цветов: {len(flower_list)}</p>
            <p>Полный список: {flower_list}</p>
            <a href="/lab2/flowers">Посмотреть все цветы</a>
        </body>
        </html>
    '''

# роут для вывода всех цветков
@app.route('/lab2/flowers')
def all_flowers():
    flowers_html = ''.join(f'<li>{flower}</li>' for flower in flower_list)
    return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Все цветы</title>
        </head>
        <body>
            <h1>Список всех цветов</h1>
            <p>Всего цветов: {len(flower_list)}</p>
            <ul>{flowers_html}</ul>
            <a href="/lab2/clear_flowers">Очистить список цветов</a>
        </body>
        </html>
    '''

@app.route('/lab2/clear_flowers')
def clear_flowers():
    flower_list.clear()
    return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Цветы очищены</title>
        </head>
        <body>ч 
            <h1>Список цветов был очищен</h1>
            <a href="/lab2/flowers">Посмотреть все цветы</a>
        </body>
        </html>
    '''

@app.route('/lab2/example')
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
    return render_template('examples.html', name = name, lab_number = lab_number, group = group, course = course, fruits = fruits)

@app.route('/lab2')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filtres')
def filres():
    phrase = '0 <b>сколько</b> <u>нам</u> <i>открытий</i> чудных...'
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
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

@app.route('/lab2/calc/')
def default_calc():
    return redirect('/lab2/calc/1/1')

@app.route('/lab2/calc/<int:a>')
def calc_with_default_b(a):
    return redirect(f'/lab2/calc/{a}/1')

@app.route('/lab2/books')
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
    return render_template('books.html', books=books)


@app.route('/lab2/cars')
def show_cars():
    cars = [
        {'name': 'Tesla Model S', 'description': 'Электрический седан с высоким запасом хода', 'image': 'tesla_model_s.jpg'},
        {'name': 'BMW M5', 'description': 'Самый быстрый спортивный седан с мире', 'image': 'bmw_m5.jpg'},
        {'name': 'Audi R8', 'description': 'Высокоскоростной суперкар с двигателем V10', 'image': 'audi_r8.jpg'},
        {'name': 'Mercedes S-Class', 'description': 'Роскошные седан премиум-класса', 'image': 'mercedes_s_class.jpg'},
        {'name': 'KIA Sorento', 'description': 'Корейский внедорожник', 'image': 'sorento.jpg'}
    ]
    return render_template('cars.html', cars=cars)
