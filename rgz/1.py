from werkzeug.security import generate_password_hash

# Хешируем пароль
password = "123"
hashed_password = generate_password_hash(password)
print(hashed_password)