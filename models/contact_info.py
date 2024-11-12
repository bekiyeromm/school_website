from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

# Configure your database connection
con_string = os.getenv("DATABASE_CONNECTION_STRING")
engine = create_engine(con_string)

def get_all_contact_info():
    """Fetch all contact records from the contact_information table."""
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM contact_information"))
        contact_info_list = result.fetchall()  # Fetch all records

    # Convert result to a list of dictionaries
    contacts = []
    for row in contact_info_list:
        contacts.append({
            'id': row[0],         # Access by index
            'address': row[1],
            'phone': row[2],
            'email': row[3]
        })

    return contacts
