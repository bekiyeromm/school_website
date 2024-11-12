# admissions.py
import mysql.connector
from werkzeug.security import generate_password_hash

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='school',
        password='School#123', 
        database='school_db' 
    )
    return connection


def add_user(full_name, email, password, class_assigned):
    # Use 'pbkdf2:sha256' for password hashing (which is the default)
    hashed_password = generate_password_hash(password)

    connection = get_db_connection()
    cursor = connection.cursor()

    # SQL Insert query
    insert_query = """
    INSERT INTO users (full_name, email, password, class_assigned)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (full_name, email, hashed_password, class_assigned))
    connection.commit()

    cursor.close()
    connection.close()

def view_all_user():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users
    

