from flask import Blueprint, render_template, request, url_for, redirect, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

lab6 = Blueprint('lab6', __name__)

@lab6.route('/lab5/')
def lab62():
    return render_template('lab6/lab6.html')
