from flask import Blueprint, render_template, request, url_for, redirect, session, abort
from db import db
from db.models import users, Articles
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

lab9 = Blueprint('lab9', __name__)

user_data = {}

@lab9.route('/lab9', methods=['GET', 'POST'])
def lab92():
    if request.method == 'POST':
        name = request.form.get('name')  
        if name:
            user_data['name'] = name
            return redirect(url_for('lab9.lab9_age'))  
        return render_template('lab9/name.html', error="Имя не указано")
    return render_template('lab9/name.html')

@lab9.route('/lab9/age', methods=['GET', 'POST'])
def lab9_age():
    if request.method == 'POST':
        age = request.form.get('age')  
        if age:
            try:
                user_data['age'] = int(age)
                return redirect(url_for('lab9.lab9_gender'))  
            except ValueError:
                return render_template('lab9/age.html', error="Возраст должен быть числом")
        return render_template('lab9/age.html', error="Возраст не указан")
    return render_template('lab9/age.html')

@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def lab9_gender():
    if request.method == 'POST':
        gender = request.form.get('gender')  
        if gender:
            user_data['gender'] = gender
            return redirect(url_for('lab9.lab9_question1'))  
        return render_template('lab9/gender.html', error="Пол не выбран")
    return render_template('lab9/gender.html')

@lab9.route('/lab9/question1', methods=['GET', 'POST'])
def lab9_question1():
    if request.method == 'POST':
        choice1 = request.form.get('choice1')  
        if choice1:
            user_data['choice1'] = choice1
            return redirect(url_for('lab9.lab9_question2'))  
        return render_template('lab9/question1.html', error="Выберите вариант")
    return render_template('lab9/question1.html')

@lab9.route('/lab9/question2', methods=['GET', 'POST'])
def lab9_question2():
    if request.method == 'POST':
        choice2 = request.form.get('choice2')  
        if choice2:
            user_data['choice2'] = choice2
            return redirect(url_for('lab9.lab9_congratulations'))  
        return render_template('lab9/question2.html', choice1=user_data['choice1'], error="Выберите вариант")
    return render_template('lab9/question2.html', choice1=user_data['choice1'])

@lab9.route('/lab9/congratulations', methods=['GET'])
def lab9_congratulations():
    return render_template('lab9/happycard.html', user_data=user_data)
