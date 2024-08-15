import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# Create the main window
window = QWidget()
window.setWindowTitle('Hospital Management System')
window.setGeometry(500, 500, 300, 200)

# Layouts for the main window
main_layout = QHBoxLayout()

# Login Layout
login_layout = QVBoxLayout()
login_layout.addStretch()

label = QLabel('LOGIN')
label.setAlignment(Qt.AlignCenter)
login_layout.addWidget(label)

username_layout = QHBoxLayout()
username_label = QLabel('Username:')
username_layout.addWidget(username_label)
username_input = QLineEdit()
username_layout.addWidget(username_input)
login_layout.addLayout(username_layout)
login_layout.addSpacing(40)

password_layout = QHBoxLayout()
password_label = QLabel('Password:')
password_layout.addWidget(password_label)
password_input = QLineEdit()
password_input.setEchoMode(QLineEdit.Password)
password_layout.addWidget(password_input)
login_layout.addLayout(password_layout)
login_layout.addSpacing(40)

login_button = QPushButton("Login")
login_layout.addWidget(login_button)
login_layout.addStretch()

# Signup Layout
signup_layout = QVBoxLayout()
signup_layout.addStretch()

label2 = QLabel("SignUP")
label2.setAlignment(Qt.AlignCenter)
signup_layout.addWidget(label2)

# First Name
Patient_fname_layout = QHBoxLayout()
Patient_first_name_label = QLabel('Patient_FName')
Patient_fname_layout.addWidget(Patient_first_name_label)
Patient_Fname_input = QLineEdit()
Patient_fname_layout.addWidget(Patient_Fname_input)
signup_layout.addLayout(Patient_fname_layout)
signup_layout.addSpacing(20)

# Last Name
Patient_lname_layout = QHBoxLayout()
Patient_lname_name_label = QLabel('Patient_LName')
Patient_lname_layout.addWidget(Patient_lname_name_label)
Patient_lname_input = QLineEdit()
Patient_lname_layout.addWidget(Patient_lname_input)
signup_layout.addLayout(Patient_lname_layout)
signup_layout.addSpacing(20)

# Phone Number
Phone_number_layout = QHBoxLayout()
Phone_number_label = QLabel('Phone')
Phone_number_layout.addWidget(Phone_number_label)
Phone_number_input = QLineEdit()
Phone_number_layout.addWidget(Phone_number_input)
signup_layout.addLayout(Phone_number_layout)
signup_layout.addSpacing(20)

# Blood Group
Blood_group_layout = QHBoxLayout()
Blood_group_label = QLabel('Blood Group')
Blood_group_layout.addWidget(Blood_group_label)
Blood_group_input = QLineEdit()
Blood_group_layout.addWidget(Blood_group_input)
signup_layout.addLayout(Blood_group_layout)
signup_layout.addSpacing(20)

# Gender
Gender_layout = QHBoxLayout()
Gender_label = QLabel('Gender')
Gender_layout.addWidget(Gender_label)
Gender_input = QLineEdit()
Gender_layout.addWidget(Gender_input)
signup_layout.addLayout(Gender_layout)
signup_layout.addSpacing(20)

# Email
email_layout = QHBoxLayout()
email_label = QLabel('Email :')
email_layout.addWidget(email_label)
email_input = QLineEdit()
email_layout.addWidget(email_input)
signup_layout.addLayout(email_layout)
signup_layout.addSpacing(20)

# Create Password
create_password_layout = QHBoxLayout()
create_password_label = QLabel('Create Password:')
create_password_layout.addWidget(create_password_label)
create_password_input = QLineEdit()
create_password_input.setEchoMode(QLineEdit.Password)
create_password_layout.addWidget(create_password_input)
signup_layout.addLayout(create_password_layout)
signup_layout.addSpacing(20)

# Confirm Password
confirm_password_layout = QHBoxLayout()
confirm_password_label = QLabel('Confirm Password:')
confirm_password_layout.addWidget(confirm_password_label)
confirm_password_input = QLineEdit()
confirm_password_input.setEchoMode(QLineEdit.Password)
confirm_password_layout.addWidget(confirm_password_input)
signup_layout.addLayout(confirm_password_layout)
signup_layout.addSpacing(20)

# Create Account Button
create_button = QPushButton("Create Account")
signup_layout.addWidget(create_button)
signup_layout.addStretch()

# Adding the login and signup layout to the main layout
main_layout.addStretch()
main_layout.addLayout(login_layout)
main_layout.addStretch()
main_layout.addLayout(signup_layout)
main_layout.addStretch()

window.setLayout(main_layout)
