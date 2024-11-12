import mysql.connector
from flask import flash
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='school',
        password='School#123', 
        database='school_db' 
    )
    return connection

def insert_attendance(full_name, grade, section, absence_date, homeroom_teacher):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO attendance (full_name, grade, section, absence_date, homeroom_teacher)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (full_name, grade, section, absence_date, homeroom_teacher))  # Note the order of parameters
        connection.commit()
    except Exception as e:
        # Log the error for debugging
        print(f"Error occurred: {e}")
        flash('An error occurred while submitting attendance. Please try again.', 'error')
    finally:
        cursor.close()
        connection.close()


def get_absent_students_by_date_grade_section(absence_date, grade, section):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM attendance WHERE absence_date = %s AND grade = %s AND section = %s", 
                   (absence_date, grade, section))
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students

def count_absent_students_by_date_grade_section(absence_date, grade, section):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM attendance WHERE absence_date = %s AND grade = %s AND section = %s", 
                   (absence_date, grade, section))
    count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return count


