from flask import Blueprint, redirect, url_for, request
lab1 = Blueprint('lab1', __name__)

@lab1.route('/index')
def start():

    return redirect("/menu", code=302)

@lab1.route('/lab1')
def lab():
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
            <li><a href="/lab2" target="_blank">Меню второй лабораторной</a></li>
        </ul>
    </nav>

    <footer>
        &copy; Червоняк Денис, ФБИ-24, 3 курс, 2024
    </footer>
</body>
</html>
"""


@lab1.route('/lab1/oak')
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


@lab1.route('/lab1/student')
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


@lab1.route('/lab1/python')
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


@lab1.route('/lab1/s7air')
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

