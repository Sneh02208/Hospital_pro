import sys
import random
import string
from datetime import datetime
from PyQt5.QtWidgets import QApplication
from ui import (app, window, Patient_Fname_input, Patient_lname_input, Phone_number_input, Blood_group_input, 
                email_input, Gender_input, create_password_input, create_button)

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
    print(patient_data)  # Perform further processing as required like redshift push 

create_button.clicked.connect(collect_data) # this may be better to be used in the 

if __name__ == "__main__":
    sys.exit(app.exec_())





