import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='school',
        password='School#123',
        database='school_db'
    )

def insert_staff_profile(name, profile_photo_path, experience, qualification, expert_areas, position):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO staff_profiles (name, profile_photo, experience, qualification, expert_areas, position)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, profile_photo_path, experience, qualification, expert_areas, position))
    connection.commit()
    cursor.close()
    connection.close()
def fetch_all_staff_profiles():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM staff_profiles"
    cursor.execute(query)
    staff_profiles = cursor.fetchall()
    cursor.close()
    connection.close()
    return staff_profiles

def update_staff_profile(id, name, experience, qualification, expert_areas, position):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
    UPDATE staff_profiles
    SET name = %s, experience = %s, qualification = %s, expert_areas = %s, position = %s
    WHERE id = %s
    """
    cursor.execute(query, (name, experience, qualification, expert_areas, position, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_staff_profile(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM staff_profiles WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()
    connection.close()

def fetch_staff_profile_by_id(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM staff_profiles WHERE id = %s", (id,))
    staff = cursor.fetchone()
    cursor.close()
    connection.close()
    return staff
