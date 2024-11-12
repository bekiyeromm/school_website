# admissions.py
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='school',
        password='School#123', 
        database='school_db' 
    )
    return connection

# Get all admissions
def get_admissions():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM admissions"
    cursor.execute(query)
    admissions = cursor.fetchall()
    cursor.close()
    connection.close()
    return admissions

# Insert new admission
def insert_admission(process, requirements, application_form_link):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO admissions (process, requirements, application_form_link) VALUES (%s, %s, %s)"
    cursor.execute(query, (process, requirements, application_form_link))
    connection.commit()
    cursor.close()
    connection.close()

# Get a specific admission by id
def get_admission_by_id(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM admissions WHERE id = %s"
    cursor.execute(query, (id,))
    admission = cursor.fetchone()
    cursor.close()
    connection.close()
    return admission

# Update an admission
def update_admission(id, process, requirements, application_form_link):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "UPDATE admissions SET process = %s, requirements = %s, application_form_link = %s WHERE id = %s"
    cursor.execute(query, (process, requirements, application_form_link, id))
    connection.commit()
    cursor.close()
    connection.close()

# Delete an admission
def delete_admission(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM admissions WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()
    connection.close()