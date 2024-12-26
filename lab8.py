from flask import Blueprint, render_template, request, abort, session
import psycopg2
from psycopg2.extras import RealDictCursor

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
