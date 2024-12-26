from flask import Blueprint, render_template, request, abort, session, redirect
from db import db
from db.models import users, Articles
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

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

    login_user(new_user)
    return redirect('/lab8/articles')

@lab8.route('/lab8/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('/lab8/login.html')
    
    login_form = request.form.get('login')
    password_form = request.form.get('password')
    remember = request.form.get('remember') == 'on'

    if not login_form:
        return render_template('lab8/login.html', error='Имя пользователя не может быть пустым')

    if not password_form:
        return render_template('lab8/login.html', error='Пароль не может быть пустым')

    user = users.query.filter_by(login=login_form).first()

    if user and check_password_hash(user.password, password_form):
        login_user(user, remember=remember)
        return redirect('/lab8/articles')
        
    return render_template('/lab8/login.html', error='Ошибка входа: логин и/или пароль неверны')


@lab8.route('/lab8/articles/')
@login_required
def articles_list():
    articles = Articles.query.filter_by(login_id=current_user.id).all()
    return render_template('lab8/articles.html', articles=articles)


@lab8.route('/lab8/logout')
@login_required
def logout():
    logout_user()
    return redirect('/lab8/')

@lab8.route('/lab8/create', methods=['GET', 'POST'])
@login_required
def create_article():
    if request.method == 'GET':
        return render_template('lab8/create_article.html')
    
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_public = bool(request.form.get('is_public'))

    if not title or not article_text:
        return render_template('lab8/create_article.html', error='Все поля обязательны для заполнения')

    new_article = Articles(
        login_id=current_user.id,
        title=title,
        article_text=article_text,
        is_favourite=False,
        is_public=is_public,
        likes=0
    )
    db.session.add(new_article)
    db.session.commit()
    return redirect('/lab8/articles')


@lab8.route('/lab8/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    article = Articles.query.get_or_404(article_id)
    if article.login_id != current_user.id:
        abort(403)

    if request.method == 'GET':
        return render_template('lab8/edit_article.html', article=article)

    article.title = request.form.get('title')
    article.article_text = request.form.get('article_text')
    db.session.commit()
    return redirect('/lab8/articles')

@lab8.route('/lab8/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    article = Articles.query.get_or_404(article_id)
    if article.login_id != current_user.id:
        abort(403)

    db.session.delete(article)
    db.session.commit()
    return redirect('/lab8/articles')

@lab8.route('/lab8/public_articles')
def public_articles():
    articles = Articles.query.filter_by(is_public=True).all()
    return render_template('lab8/public_articles.html', articles=articles)

@lab8.route('/lab8/search_articles/', methods=['GET', 'POST'])
def search_articles():
    if request.method == 'POST':
        search_query = request.form.get('query')

        if not search_query:
            return render_template('lab8/search_articles.html', error="Введите строку для поиска.")

        articles = Articles.query.filter(Articles.title.ilike(f"%{search_query}%") | Articles.article_text.ilike(f"%{search_query}%")).all()

        return render_template('lab8/search_articles.html', articles=articles, query=search_query)

    return render_template('lab8/search_articles.html')

