from flask import Blueprint, render_template, request, url_for, redirect, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

lab6 = Blueprint('lab6', __name__)


def db_connect():
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='denis_chervonyak_knowledge_base',
        user='denis_chervonyak_knowledge_base',
        password='123'
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

@lab6.route('/lab6/')
def lab62():
    login = session.get('login', 'Аноним')
    return render_template('lab6/lab6.html', login=login)

@lab6.route('/lab6/json-rpc-api/', methods = ['POST'])
def api():
    data = request.json
    id = data['id']

    if data['method'] == 'info':
        conn, cur = db_connect()
        cur.execute("SELECT * FROM offices ORDER BY id ASC")
        offices = cur.fetchall()
        cur.close()
        conn.close()
        return {
            'jsonrpc': '2.0',
            'result': offices,
            'id': id
        }

    login = session.get('login')
    if not login:
        return {
            'jsonrpc': '2.0',
            'error': {
                'code': 1,
                'message': 'Unathorized'
            },
            'id': id
        }

    if data['method'] == 'booking':
        office_id = data['params']
        conn, cur = db_connect()
        cur.execute("SELECT tenant FROM offices WHERE id = %s", (office_id,))
        office = cur.fetchone()
        if not office:
            cur.close()
            conn.close()
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 5,
                    'message': 'Office not found'
                },
                'id': id
            }
        if office['tenant']:
            cur.close()
            conn.close()
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 2,
                    'message': 'Already booked'
                },
                'id': id
            }
        cur.execute("UPDATE offices SET tenant = TRUE WHERE id = %s", (office_id,))
        conn.commit()
        cur.close()
        conn.close()
        return {
            'jsonrpc': '2.0',
            'result': 'success',
            'id': id
        }

    if data['method'] == 'cancellation':
        office_id = data['params']
        conn, cur = db_connect()
        cur.execute("SELECT tenant FROM offices WHERE id = %s", (office_id,))
        office = cur.fetchone()
        if not office:
            cur.close()
            conn.close()
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 5,
                    'message': 'Office not found'
                },
                'id': id
            }
        if not office['tenant']:
            cur.close()
            conn.close()
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 3,
                    'message': 'Office is not booked'
                },
                'id': id
            }
        cur.execute("UPDATE offices SET tenant = FALSE WHERE id = %s", (office_id,))
        conn.commit()
        cur.close()
        conn.close()
        return {
            'jsonrpc': '2.0',
            'result': 'success',
            'id': id
        }

    return {
        'jsonrpc': '2.0',
        'error': {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }

