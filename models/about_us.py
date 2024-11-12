from sqlalchemy import create_engine, text
import dotenv
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()

# Load the connection string from the .env file
con_string = os.getenv("DATABASE_CONNECTION_STRING")

# Set up the SQLAlchemy engine and sessionmaker
engine = create_engine(con_string)
Session = sessionmaker(bind=engine)

def insert_about_us(data):
    try:
        with Session() as session:
            query = text("""
                INSERT INTO about_us (school_history, mission, vision, administration_staff_profiles, 
                                      contact_info, social_media_links, privacy)
                VALUES (:school_history, :mission, :vision, :administration, 
                        :contact_info, :social_media, :privacy)
            """)
            session.execute(query, data)
            session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error occurred: {e}")


def update_about_us(data, about_us_id):
    with Session() as session:
        query = text("""
            UPDATE about_us
            SET school_history = :school_history,
                mission = :mission,
                vision = :vision,
                administration_staff_profiles = :administration,
                contact_info = :contact_info,
                social_media_links = :social_media,
                privacy = :privacy
            WHERE id = :about_us_id
        """)
        session.execute(query, {**data, "about_us_id": about_us_id})
        session.commit()