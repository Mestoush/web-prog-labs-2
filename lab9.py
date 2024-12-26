from flask import Blueprint, render_template, request, url_for, redirect, session, current_app, abort
from db import db
from db.models import users, Articles
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab8/')
def lab82():
    login = session.get('login', 'Аноним')
    return render_template('lab8/lab8.html', login=login)