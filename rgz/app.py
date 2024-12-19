from flask import Flask, render_template, request, redirect, url_for, session
import os
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')

# Функция подключения к SQLite3
def db_connect():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  
    cur = conn.cursor()
    return conn, cur

# Функция для получения сотрудников
def get_employees(page=1, per_page=20):
    conn, cur = db_connect()
    start = (page - 1) * per_page
    query = "SELECT * FROM employees ORDER BY id LIMIT ? OFFSET ?"
    cur.execute(query, (per_page, start))
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return employees

# Добавление нового сотрудника
def add_employee_to_db(name, position, gender, phone, email, start_date):
    conn, cur = db_connect()
    query = """INSERT INTO employees (name, position, gender, phone, email, start_date)
               VALUES (?, ?, ?, ?, ?, ?)"""
    cur.execute(query, (name, position, gender, phone, email, start_date))
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def index():
    username = session.get('username')
    return render_template("index.html", username=username)

@app.route("/employees", methods=["GET", "POST"])
def employees_list():
    page = int(request.args.get("page", 1))
    search = request.args.get("search", "").lower()
    sort = request.args.get("sort_by", "").lower()
    conn, cur = db_connect()

    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()

    cur.execute("SELECT DISTINCT position FROM employees")
    sorted_positions = ["Все должности"] + [row["position"] for row in cur.fetchall()]

    filtered_employees = [dict(emp) for emp in employees if search in emp["name"].lower()]

    if sort and sort != "все должности":
        filtered_employees = [emp for emp in filtered_employees if sort in emp["position"].lower()]

    for emp in filtered_employees:
        emp["probation_period"] = "Испытательный период" if emp["probation_period"] else "Постоянная работа"

    cur.execute("SELECT COUNT(*) FROM employees")
    total_employees = cur.fetchone()[0]
    employees_for_page = filtered_employees[(page - 1) * 20:page * 20]
    next_page = page + 1 if (page * 20) < total_employees else None

    cur.close()
    conn.close()
    return render_template("employees.html", employees=employees_for_page, next_page=next_page, user_authenticated=True, page=page, search=search, sorted=sorted_positions)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn, cur = db_connect()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["role"] = user["role"]
            return redirect(url_for("index"))
        return "Неверные логин или пароль"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return render_template("index.html")

@app.route("/add_employee", methods=["GET", "POST"])
def add_employee():
    if session.get("role") not in ["Администратор", "Кадровик"]:
        return redirect(url_for("login"))

    if request.method == "POST":
        name = request.form["name"]
        position = request.form["position"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        email = request.form["email"]
        start_date = request.form["start_date"]
        probation_period = 'probation_period' in request.form

        conn, cur = db_connect()
        cur.execute("""INSERT INTO employees 
                       (name, position, gender, phone, email, start_date, probation_period)
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (name, position, gender, phone, email, start_date, probation_period))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for("employees_list"))

    return render_template("add_employee.html")

@app.route('/edit_employee/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    conn, cur = db_connect()

    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        probation_period = 'probation_period' in request.form

        cur.execute("""UPDATE employees 
                       SET name = ?, position = ?, probation_period = ?
                       WHERE id = ?""",
                    (name, position, probation_period, employee_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/employees')

    cur.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
    employee = cur.fetchone()
    cur.close()
    conn.close()

    return render_template('add_employee.html', employee=dict(employee))

@app.route('/delete_employee/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    conn, cur = db_connect()
    cur.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/employees')

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if session.get("role") != "Администратор":
        return redirect(url_for("login"))

    conn, cur = db_connect()
    cur.execute("SELECT username, role FROM users")
    users = [dict(user) for user in cur.fetchall()]

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = "Кадровик"

        hashed_password = generate_password_hash(password)

        cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                    (username, hashed_password, role))
        conn.commit()
        cur.execute("SELECT username, role FROM users")
        users = [dict(user) for user in cur.fetchall()]
        cur.close()
        conn.close()

        return render_template("add_user.html", users=users)

    cur.close()
    conn.close()
    return render_template("add_user.html", users=users)

# Главная точка входа
if __name__ == "__main__":
    app.run(debug=True)
