from flask import Blueprint, render_template, request, url_for, redirect, session, current_app, abort
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

lab7 = Blueprint('lab7', __name__)

films = [
    {
        'title': 'The Shawshank Redemption',
        'title_ru': 'Побег из Шоушенка',
        'year': 1994,
        'description': 'История о дружбе двух заключённых, один из которых несправедливо осуждён за убийство жены и её любовника.'
    },

    {
        'title': 'The Green Mile',
        'title_ru': 'Зелёная миля',
        'year': 1999,
        'description': 'Драма о тюремном охраннике, который сталкивается с чудесными событиями, связанными с заключённым, обладающим сверхъестественными способностями.'
    },

    {
        'title': 'Forrest Gump',
        'title_ru': 'Форрест Гамп',
        'year': 1994,
        'description': 'История жизни мужчины с низким IQ, который становится свидетелем и участником ключевых событий американской истории.'
    }
]

@lab7.route('/lab7/')
def lab62():
    login = session.get('login', 'Аноним')
    return render_template('lab7/index.html', login=login)


@lab7.route('/lab7/rest-api/films/', methods = ['GET'])
def get_films():
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods = ['GET'])
def get_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    
    return films[id]

@lab7.route('/lab7/rest-api/films/<int:id>', methods = ['DELETE'])
def del_film():
    if id < 0 or id >= len(films):
        abort(404)
    del films[id]
    return "", 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods = ['PUT'])
def put_film(id):
    if id < 0 or id >= len(films):
        abort(404)
    film = request.get_json()
    films[id] = film
    return films[id]

@lab7.route('/lab7/rest-api/films/', methods = ['POST'])
def add_film():
    film = request.get_json()
    films.append(film)
    return films[-1], 201