from flask import Blueprint, render_template, request, url_for, redirect, session, abort
from db import db
from db.models import users, Articles
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9', methods=['GET', 'POST'])
def lab92():
    if 'congratulations' in session:
        return redirect('/lab9/happycard')

    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            session['name'] = name
            return redirect('/lab9/age')
    return render_template('lab9/name.html', name=session.get('name', ''))

@lab9.route('/lab9/age', methods=['GET', 'POST'])
def lab9_age():
    if request.method == 'POST':
        age = request.form.get('age')
        if age:
            session['age'] = int(age)
            return redirect('/lab9/gender')
    return render_template('lab9/age.html', age=session.get('age', ''))

@lab9.route('/lab9/gender', methods=['GET', 'POST'])
def lab9_gender():
    if request.method == 'POST':
        gender = request.form.get('gender')
        if gender:
            session['gender'] = gender
            return redirect('/lab9/question1')
    return render_template('lab9/gender.html', gender=session.get('gender', ''))

@lab9.route('/lab9/question1', methods=['GET', 'POST'])
def lab9_question1():
    if request.method == 'POST':
        choice1 = request.form.get('choice1')
        if choice1:
            session['choice1'] = choice1
            return redirect('/lab9/question2')
    return render_template('lab9/question1.html', choice1=session.get('choice1', ''))

@lab9.route('/lab9/question2', methods=['GET', 'POST'])
def lab9_question2():
    if request.method == 'POST':
        choice2 = request.form.get('choice2')
        if choice2:
            session['choice2'] = choice2
            session['congratulations'] = {
                'name': session.get('name'),
                'age': session.get('age'),
                'gender': session.get('gender'),
                'choice1': session.get('choice1'),
                'choice2': session.get('choice2')
            }
            return redirect('/lab9/happycard')
    return render_template('lab9/question2.html', choice1=session.get('choice1', ''))

@lab9.route('/lab9/happycard', methods=['GET'])
def lab9_congratulations():
    if 'congratulations' not in session:
        return redirect('/lab9')
    return render_template('lab9/happycard.html', user_data=session['congratulations'])

@lab9.route('/lab9/reset', methods=['GET'])
def lab9_reset():
    session.clear()
    return redirect('/lab9')