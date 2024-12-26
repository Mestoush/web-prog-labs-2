from flask import Blueprint, render_template, request, abort, session, redirect
from db import db
from db.models import users, Articles
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash

lab8 = Blueprint('lab8', __name__)

def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='denis_chervonyak_knowledge_base',
        user='denis_chervonyak_knowledge_base',
        password='123'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

@lab8.route('/lab8/')
def lab82():
    login = session.get('login', 'Аноним')
    return render_template('lab8/lab8.html', login=login)


@lab8.route('/lab8/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('lab8/register.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')

    if not login_form:
        return render_template('lab8/register.html', error='Имя пользователя не может быть пустым')

    if not password_form:
        return render_template('lab8/register.html', error='Пароль не может быть пустым')

    login_exists = users.query.filter_by(login = login_form).first()
    if login_exists:
        return render_template('lab8/register.html', error = 'Такой пользователь уже существует')
    
    password_hash = generate_password_hash(password_form)
    new_user = users(login = login_form, password = password_hash)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/lab8/')
