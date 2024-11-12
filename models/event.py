# event.py
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='school',
        password='School#123', 
        database='school_db' 
    )
    return connection

def get_all_events():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM events"
    cursor.execute(query)
    events = cursor.fetchall()
    cursor.close()
    connection.close()
    return events

def add_event(title, description, date, location):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO events (title, description, date, location) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (title, description, date, location))
    connection.commit()
    cursor.close()
    connection.close()

def get_event_by_id(event_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM events WHERE id = %s"
    cursor.execute(query, (event_id,))
    event = cursor.fetchone()
    cursor.close()
    connection.close()
    return event

def update_event(event_id, title, description, date, location):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "UPDATE events SET title = %s, description = %s, date = %s, location = %s WHERE id = %s"
    cursor.execute(query, (title, description, date, location, event_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_event(event_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM events WHERE id = %s"
    cursor.execute(query, (event_id,))
    connection.commit()
    cursor.close()
    connection.close()
