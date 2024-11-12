from flask import Flask, render_template, redirect, url_for, request, flash
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import bcrypt
from models.about_us import insert_about_us  # Assuming this is your function from earlier
from models.event import (
    get_all_events,
    add_event,
    update_event,
    get_event_by_id,
    delete_event
)
load_dotenv()
# Configure your database connection
con_string = os.getenv("DATABASE_CONNECTION_STRING")
engine = create_engine(con_string)

# Create a session factory using sessionmaker
Session = sessionmaker(bind=engine)

# Initialize Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

#####################################
#####       about us         ########
###################################### 
import mysql.connector
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='school',
        password='School#123', 
        database='school_db' 
    )
    return connection
@app.route('/')
def index():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM about_us WHERE id=1"))
        about_us_data = result.fetchone()
        contact_info_data = get_all_contact_info()
    # Ensure that about_us_data is not None before passing it to the template
    if not about_us_data:
        about_us_data = {}  # Fallback to an empty dict if no data is found
    # Convert 'contact_info_data' to a list of dicts
    contacts = [dict(row.items()) for row in contact_info_data] if contact_info_data else []
    # Pass the fetched data to the template
    return render_template('index.html', about_us_data=about_us_data, contacts=contacts)


@app.route('/insert_form')
def insert_form():
    return render_template('insert_about_us.html')


@app.route('/insert', methods=['POST'])
def insert():
    """Insert new 'about us' data into the database from form data."""
    # Fetch form data
    data = {
        "school_history": request.form.get('school_history'),
        "mission": request.form.get('mission'),
        "vision": request.form.get('vision'),
        "administration": request.form.get('administration'),
        "contact_info": request.form.get('contact_info'),
        "social_media": request.form.get('social_media'),
        "privacy": request.form.get('privacy')
    }
    # Use the insert_about_us function to insert the data into the database
    try:
        insert_about_us(data)  # Call the insert function (should be imported from models.about_us)
        flash("Data inserted successfully!", "success")
    except Exception as e:
        flash(f"Error inserting data: {e}", "danger")
    # Redirect to the index or another page
    return redirect(url_for('index'))

from models.about_us import update_about_us  # Assuming this is your update function from above

@app.route('/edit_about_us_form/<int:user_id>')
def edit_about_us_form(user_id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM about_us WHERE id = :user_id"), {"user_id": user_id})
        about_us_data = result.fetchone()
    # Ensure that about_us_data is not None before passing it to the template
    if not about_us_data:
        about_us_data = {}
    return render_template('edit_about_us.html', about_us_data=about_us_data)


@app.route('/edit_about_us/<int:user_id>', methods=['POST'])
def edit_about_us(user_id):
    """Update 'about us' data for a given user."""
    data = {
        "school_history": request.form.get('school_history'),
        "mission": request.form.get('mission'),
        "vision": request.form.get('vision'),
        "administration": request.form.get('administration'),
        "contact_info": request.form.get('contact_info'),
        "social_media": request.form.get('social_media'),
        "privacy": request.form.get('privacy')
    }
    try:
        # Call the update function and update the record
        update_about_us(data, user_id)
        flash("About Us updated successfully!", "success")
    except Exception as e:
        flash(f"Error updating About Us: {e}", "danger")
    return redirect(url_for('index'))


####################################################
######### contact us   #############################

from models.contact_info import get_all_contact_info

@app.route('/contact_us')
def contact_us():
    contacts = get_all_contact_info()
    return render_template('contact_us.html', contacts=contacts)

#################################
##    event            ##########
#################################


@app.route('/events')
def events():
    events = get_all_events()
    return render_template('manage.html', events=events)
from flask import jsonify


@app.route('/manage-events')
def manage_events():
    events = get_all_events()
    return render_template('view_event.html', events=events)
    # return jsonify(events)


@app.route('/add_event', methods=['GET', 'POST'])
def add_event_route():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        location = request.form['location']
        add_event(title, description, date, location)  
        flash('Event added successfully!', 'success')
        return redirect(url_for('events'))
    return render_template('add_event.html')


@app.route('/update_event/<int:event_id>', methods=['GET', 'POST'])
def update_event_route(event_id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        location = request.form['location']
        update_event(event_id, title, description, date, location)  
        flash('Event updated successfully!', 'success')
        return redirect(url_for('events')) 
    event = get_event_by_id(event_id)
    return render_template('update_event.html', event=event)


@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event_route(event_id):
    delete_event(event_id)
    
    flash('Event deleted successfully!', 'success')
    return redirect(url_for('events'))


#############################
##       admissions  ########
#############################


from models.admissions import get_admissions, insert_admission,update_admission,delete_admission,get_admission_by_id
# Route to view admissions
@app.route('/admissions')
def view_admissions():
    admissions = get_admissions()
    return render_template('view_admissions.html', admissions=admissions)


# Route to insert a new admission
@app.route('/add_admission', methods=['GET', 'POST'])
def add_admission():
    if request.method == 'POST':
        process = request.form['process']
        requirements = request.form['requirements']
        application_form_link = request.form['application_form_link']
        # Insert the data into the admissions table
        insert_admission(process, requirements, application_form_link)
        flash('Admission process added successfully!', 'success')
        return redirect(url_for('view_admissions'))
    return render_template('add_admission.html')


# Update an existing admission
@app.route('/update_admission/<int:id>', methods=['GET', 'POST'])
def update_admission_route(id):
    admission = get_admission_by_id(id)
    
    if request.method == 'POST':
        process = request.form['process']
        requirements = request.form['requirements']
        application_form_link = request.form['application_form_link']
        
        update_admission(id, process, requirements, application_form_link)
        flash('Admission process updated successfully!', 'success')
        return redirect(url_for('view_admissions'))
    
    return render_template('update_admission.html', admission=admission)


# Delete an existing admission
@app.route('/delete_admission/<int:id>', methods=['POST'])
def delete_admission_route(id):
    delete_admission(id)
    flash('Admission process deleted successfully!', 'success')
    return redirect(url_for('view_admissions'))


###############################
#       announcement  #########
###############################
# Function to strip HTML tags
from bs4 import BeautifulSoup  # Install with pip install beautifulsoup4
def strip_html_tags(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()

from models.announcements import get_all_announcements, insert_announcement
from models.announcements import update_announcement, delete_announcement, get_announcement_by_id
@app.route('/announcements')
def view_announcements():
    announcements = get_all_announcements()
    for announcement in announcements:
        text_content = strip_html_tags(announcement['content'])
        if len(text_content) > 50:
            announcement['preview'] = text_content[:50] + '...'  # Preview first 100 chars + "..."
        else:
            announcement['preview'] = text_content  # Full text if less than 100 chars
    return render_template('view_announcements.html', announcements=announcements)

@app.route('/add_announcement', methods=['GET', 'POST'])
def add_announcement():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        expiry_date = request.form['expiry_date']
        insert_announcement(title, content, category, expiry_date)
        flash('Announcement added successfully!', 'success')
        return redirect(url_for('view_announcements'))
    return render_template('add_announcement.html')


@app.route('/update_announcement/<int:id>', methods=['GET', 'POST'])
def update_announcement_route(id):
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        expiry_date = request.form['expiry_date']
        update_announcement(id, title, content, category, expiry_date)
        flash('Announcement updated successfully!', 'success')
        return redirect(url_for('view_announcements'))
    announcement = get_announcement_by_id(id)
    return render_template('update_announcement.html', announcement=announcement)

@app.route('/delete_announcement/<int:id>', methods=['POST'])
def delete_announcement_route(id):
    delete_announcement(id)
    flash('Announcement deleted successfully!', 'success')
    return redirect(url_for('view_announcements'))

#######################################
####  sttaf profile              ######
#######################################

from werkzeug.utils import secure_filename
import os
from models.staff_model import insert_staff_profile, update_staff_profile,fetch_all_staff_profiles
from models.staff_model import delete_staff_profile,fetch_staff_profile_by_id
# Define where uploaded images will be stored
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/add_staff_profile', methods=['GET', 'POST'])
def add_staff_profile():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        experience = request.form['experience']
        qualification = request.form['qualification']
        expert_areas = request.form['expert_areas']
        position = request.form['position']

        # Check if a file is uploaded
        if 'profile_photo' not in request.files:
            return "No file part", 400
        
        file = request.files['profile_photo']

        # If the user does not select a file, the browser may also submit an empty part
        if file.filename == '':
            return "No selected file", 400
        
        # If file is allowed
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            # Ensure the upload directory exists
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            # Save the file
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # Insert data into the database via the model
            insert_staff_profile(name, file_path, experience, qualification, expert_areas, position)
            return redirect(url_for('staff_profiles'))
    return render_template('add_staff_profile.html')


# Route to view all staff profiles
@app.route('/staff_profiles')
def staff_profiles():
    staff_profiles = fetch_all_staff_profiles()
    return render_template('staff_profiles.html', staff_profiles=staff_profiles)


# Route to update staff profile
@app.route('/update_staff/<int:id>', methods=['GET', 'POST'])
def update_staff(id):
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        experience = request.form['experience']
        qualification = request.form['qualification']
        expert_areas = request.form['expert_areas']
        position = request.form['position']
        # Update staff profile in the database
        update_staff_profile(id, name, experience, qualification, expert_areas, position)
        return redirect(url_for('staff_profiles'))
    # Fetch the current profile to pre-fill the form
    staff = fetch_staff_profile_by_id(id)
    return render_template('update_staff.html', staff=staff)


# Route to delete staff profile
@app.route('/delete_staff/<int:id>', methods=['POST'])
def delete_staff(id):
    delete_staff_profile(id)
    return redirect(url_for('staff_profiles'))

####################################
#### Attendance    #################
####################################
from models.attendance import insert_attendance
from datetime import datetime

@app.route('/attendance')
def attendance_form():
    return render_template('attendance_form.html')


@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    required_fields = ['grade', 'full_name', 'section', 'absence_date', 'homeroom_teacher']
    missing_fields = [field for field in required_fields if field not in request.form or not request.form[field]]
    if missing_fields:
        flash(f"Missing fields: {', '.join(missing_fields)}", 'error')
        return redirect('/attendance')
    full_name = request.form['full_name']
    grade = request.form['grade']
    section = request.form['section']
    absence_date = request.form['absence_date']
    homeroom_teacher = request.form['homeroom_teacher']
    insert_attendance(full_name, grade, section, absence_date, homeroom_teacher)
    flash('Attendance submitted successfully!', 'success')
    return redirect(url_for('attendance_form'))

@app.route('/view_absences', methods=['GET', 'POST'])
def view_absences():
    if request.method == 'POST':
        # Gather filtering data
        start_month = int(request.form['start_month'])
        end_month = int(request.form['end_month'])
        start_year = int(request.form['start_year'])
        end_year = int(request.form['end_year'])
        grade = request.form.get('grade')
        section = request.form.get('section')

        # Database connection and query setup
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Calculate start and end date based on range
        start_date = datetime(start_year, start_month, 1)
        end_date = datetime(end_year, end_month + 1, 1) if end_month < 12 else datetime(end_year + 1, 1, 1)

        # Query with optional filters for grade and section
        query = """
    SELECT full_name, grade, section, homeroom_teacher, COUNT(absence_date) AS absence_count, ANY_VALUE(id) AS id
    FROM attendance
    WHERE absence_date >= %s AND absence_date < %s
"""
        params = [start_date, end_date]

        if grade:
            query += " AND grade = %s"
            params.append(grade)
        if section:
            query += " AND section = %s"
            params.append(section)

        query += " GROUP BY full_name, grade, section, homeroom_teacher ORDER BY absence_count DESC"
        
        cursor.execute(query, params)
        students = cursor.fetchall()
        cursor.close()
        connection.close()

        count = len(students)
        return render_template('view_absences.html', students=students, count=count, 
                               start_year=start_year, start_month=start_month, 
                               end_year=end_year, end_month=end_month)
    return render_template('view_absences.html', students=[], count=0)

@app.route('/edit_attendance/<int:id>', methods=['GET', 'POST'])
def edit_attendance(id):
    # Connect to the database and fetch the attendance record
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Fetch the specific attendance record based on the id
    cursor.execute("SELECT * FROM attendance WHERE id = %s", (id,))
    attendance = cursor.fetchone()
    cursor.close()
    connection.close()

    if request.method == 'POST':
        # Get updated data from form
        full_name = request.form['full_name']
        grade = request.form['grade']
        section = request.form['section']
        absence_date = request.form['absence_date']
        homeroom_teacher = request.form['homeroom_teacher']

        # Update the attendance record in the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE attendance 
            SET full_name = %s, grade = %s, section = %s, absence_date = %s, homeroom_teacher = %s 
            WHERE id = %s
        """, (full_name, grade, section, absence_date, homeroom_teacher, id))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('view_absences'))  # Redirect after update

    return render_template('edit_attendance.html', attendance=attendance)

@app.route('/delete_attendance/<int:id>', methods=['POST'])
def delete_attendance(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM attendance WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    flash('Attendance record deleted successfully!', 'success')
    return redirect(url_for('view_absences'))

##############################################
#### home room teacher #######################
##############################################
from models.home_room_teacher import add_user
@app.route('/add_user', methods=['GET', 'POST'])
def add_user_view():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = request.form['password']
        class_assigned = request.form['class_assigned']

        # Call the add_user function to insert data into the database
        add_user(full_name, email, password, class_assigned)

        return redirect(url_for('add_user_view'))  # Redirect to the same page or another page

    return render_template('add_user.html')

from models.home_room_teacher import view_all_user
@app.route('/view_homeroom', methods=['GET'])
def view_users():
    all_user = view_all_user()
    return render_template('view_users.html', all_user=all_user)

@app.route('/update_users', methods=['GET','POST'])
def update_homeroom_teachers():
    pass

@app.route ('/delete_users', methods=['GET','POST'])
def delete_homeroom_teacher(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    flash('user record deleted successfully!', 'success')
    return redirect(url_for('view_users'))

if __name__ == '__main__':
    app.run(debug=True)
