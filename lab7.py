from flask import Blueprint, render_template, request, abort, session
import psycopg2
from psycopg2.extras import RealDictCursor

lab7 = Blueprint('lab7', __name__)

def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='denis_chervonyak_knowledge_base',
        user='denis_chervonyak_knowledge_base',
        password='123'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur


def get_all_films():
    conn, cur = db_connect()
    cur.execute("SELECT * FROM films;")
    films = cur.fetchall()
    conn.close()
    return films

def get_film_by_id(id):
    conn, cur = db_connect()
    cur.execute("SELECT * FROM films WHERE id = %s;", (id,))
    film = cur.fetchone()
    conn.close()
    return film

def add_film_to_db(film):
    conn, cur = db_connect()
    cur.execute(
        "INSERT INTO films (title, title_ru, year, description) VALUES (%s, %s, %s, %s) RETURNING id;",
        (film['title'], film['title_ru'], film['year'], film['description'])
    )
    film_id = cur.fetchone()['id']
    conn.commit()
    conn.close()
    return film_id

def update_film_in_db(id, film):
    conn, cur = db_connect()
    cur.execute(
        "UPDATE films SET title = %s, title_ru = %s, year = %s, description = %s WHERE id = %s;",
        (film['title'], film['title_ru'], film['year'], film['description'], id)
    )
    conn.commit()
    conn.close()

def delete_film_from_db(id):
    conn, cur = db_connect()
    cur.execute("DELETE FROM films WHERE id = %s;", (id,))
    conn.commit()
    conn.close()

@lab7.route('/lab7/')
def lab62():
    login = session.get('login', 'Аноним')
    return render_template('lab7/index.html', login=login)


@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    films = get_all_films()
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    film = get_film_by_id(id)
    if not film:
        abort(404)
    return film

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    film = get_film_by_id(id)
    if not film:
        abort(404)
    delete_film_from_db(id)
    return "", 204


@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    film = request.get_json()

    errors = {}
    try:
        year = int(film.get('year', 0))
        if not (1895 <= year <= 2024):
            errors['year'] = "Год должен быть в диапазоне от 1895 до текущего."
    except ValueError:
        errors['year'] = "Год должен быть числом."

    if not film.get('title') and not film.get('title_ru'):
        errors['title'] = "Оригинальное название должно быть непустым, если русское название не задано."
    if not film.get('title_ru'):
        errors['title_ru'] = "Русское название должно быть задано."
    if not film.get('description'):
        errors['description'] = "Описание не может быть пустым."
    elif len(film['description']) > 2000:
        errors['description'] = "Описание не может превышать 2000 символов."

    if errors:
        return errors, 400

    if not film.get('title'):
        film['title'] = film['title_ru']

    update_film_in_db(id, film)
    return film

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()

    errors = {}
    try:
        year = int(film.get('year', 0))
        if not (1895 <= year <= 2024):
            errors['year'] = "Год должен быть в диапазоне от 1895 до текущего."
    except ValueError:
        errors['year'] = "Год должен быть числом."

    if not film.get('title') and not film.get('title_ru'):
        errors['title'] = "Оригинальное название должно быть непустым, если русское название не задано."
    if not film.get('title_ru'):
        errors['title_ru'] = "Русское название должно быть задано."
    if not film.get('description'):
        errors['description'] = "Описание не может быть пустым."
    elif len(film['description']) > 2000:
        errors['description'] = "Описание не может превышать 2000 символов."

    if errors:
        return errors, 400

    if not film.get('title'):
        film['title'] = film['title_ru']

    film_id = add_film_to_db(film)
    film['id'] = film_id
    return film, 201
