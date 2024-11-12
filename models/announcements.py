import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='school',
        password='School#123', 
        database='school_db' 
    )
    return connection

# Insert new announcement
def insert_announcement(title, content, category, expiry_date):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO announcements (title, content, category, posted_date, expiry_date)
        VALUES (%s, %s, %s, NOW(), %s)
    """
    cursor.execute(query, (title, content, category, expiry_date))
    connection.commit()
    cursor.close()
    connection.close()


# Retrieve all announcements
def get_all_announcements():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM announcements")
    announcements = cursor.fetchall()
    cursor.close()
    connection.close()
    return announcements

# Update announcement by ID
def update_announcement(id, title, content, category, expiry_date):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "UPDATE announcements SET title = %s, content = %s, category = %s, expiry_date = %s WHERE id = %s"
    cursor.execute(query, (title, content, category, expiry_date, id))
    connection.commit()
    cursor.close()
    connection.close()

# Delete announcement by ID
def delete_announcement(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM announcements WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()
    connection.close()

# Retrieve announcement by ID for update form
def get_announcement_by_id(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM announcements WHERE id = %s"
    cursor.execute(query, (id,))
    announcement = cursor.fetchone()
    cursor.close()
    connection.close()
    return announcement

