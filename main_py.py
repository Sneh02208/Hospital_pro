import random
import string
import sys
from datetime import datetime
from ui import app, window, create_button, Patient_Fname_input, Patient_lname_input, Phone_number_input, Blood_group_input, email_input, Gender_input, create_password_input

def generate_random_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    return f"{prefix}{digits}"

def generate_current_date():
    return datetime.today().strftime('%Y-%m-%d')

def collect_data():
    patient_data = {
        "Patient_ID": generate_random_id(),
        "Patient_FName": Patient_Fname_input.text(),
        "Patient_LName": Patient_lname_input.text(),
        "Phone": Phone_number_input.text(),
        "Blood_Type": Blood_group_input.text(),
        "Email": email_input.text(),
        "Gender": Gender_input.text(),
        "Password": create_password_input.text(),
        "Admission_Date": generate_current_date(),
    }
    print(patient_data)  # This is where you'd handle further processing (e.g., saving to a database)

create_button.clicked.connect(collect_data)

if __name__ == "__main__":
    window.show()
    sys.exit(app.exec_())








"""
import sys
import random
import string
from datetime import datetime
import psycopg2
from PyQt5.QtWidgets import QApplication
from ui import (app, window, fname_input, lname_input, phone_input, blood_type_input, 
                email_input, gender_input, password_input, submit_button)

def load_redshift_config(filepath='redshift_config.txt'):
    config = {}
    with open(filepath, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

def generate_random_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=6))
    return f"{prefix}{digits}"

def generate_current_date():
    return datetime.today().strftime('%Y-%m-%d')

def push_to_redshift(patient_data):
    config = load_redshift_config()

    try:
        # Establish a connection to the Redshift database
        conn = psycopg2.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['dbname'],
            user=config['user'],
            password=config['password']
        )
        cur = conn.cursor()
        
        # Insert data into the Redshift table
        insert_query = 
        #INSERT INTO Patient (Patient_ID, Patient_FName, Patient_LName, Phone, Blood_Type, 
         #                    Email, Gender, Condition, Admission_Date, Discharge_Date)
        #VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NULL);
        
        cur.execute(insert_query, (
            patient_data['Patient_ID'],
            patient_data['Patient_FName'],
            patient_data['Patient_LName'],
            patient_data['Phone'],
            patient_data['Blood_Type'],
            patient_data['Email'],
            patient_data['Gender'],
            patient_data['Password'],  # Assuming Condition is mapped to Password (Adjust accordingly)
            patient_data['Admission_Date'],
        ))

        # Commit the transaction
        conn.commit()

        # Close the connection
        cur.close()
        conn.close()

        print("Data pushed to Redshift successfully")

    except Exception as e:
        print(f"Error pushing data to Redshift: {e}")

def collect_data():
    patient_data = {
        "Patient_ID": generate_random_id(),
        "Patient_FName": fname_input.text(),
        "Patient_LName": lname_input.text(),
        "Phone": phone_input.text(),
        "Blood_Type": blood_type_input.text(),
        "Email": email_input.text(),
        "Gender": gender_input.text(),
        "Password": password_input.text(),
        "Admission_Date": generate_current_date(),
    }
    
    # Push the collected data to Redshift
    push_to_redshift(patient_data)

submit_button.clicked.connect(collect_data)

if __name__ == "__main__":
    sys.exit(app.exec_())
"""
