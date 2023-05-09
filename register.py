#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton, 
                             QLabel, 
                             QLineEdit, 
                             QMessageBox, 
                             QPlainTextEdit, 
                             QHBoxLayout, 
                             QVBoxLayout) 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import db_connect, login
import random, sys, re, string

def start_app():
    global win
    win = RegisterMenu()
    win.show()

class RegisterMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A game of Rock-Paper-Scissors - Create New Account")
        self.setWindowIcon(QIcon(r'images/console.png'))
        self.setGeometry(650, 300, 800, 400)
        self.setMaximumWidth(800)
        self.setMaximumHeight(400)
        self.initUI()

    def initUI(self):
        # Fonts setting
        font = QFontDatabase.addApplicationFont(r'fonts/ElementalEnd.ttf')
        if font < 0: print("Error in fonts.")
        families = QFontDatabase.applicationFontFamilies(font)

        # Layout for the user input / register form
        register_layout = QVBoxLayout()
        register_layout.addStretch()
        register_layout.addSpacing(10)

        email_address_label = QLabel(self)
        email_address_label.setText("Email address")
        email_address_label.setFont(QFont(families[0], 12))
        email_address_label.setAlignment(Qt.AlignCenter)

        email_address_text_field = QLineEdit(self)
        email_address_text_field.setFont(QFont(families[0], 12))
        email_address_text_field.setAlignment(Qt.AlignCenter)
        email_address_text_field.setFixedWidth(300)

        user_name_label = QLabel(self)
        user_name_label.setText("User Name")
        user_name_label.setFont(QFont(families[0], 12))
        user_name_label.setAlignment(Qt.AlignCenter)

        user_name_text_field = QLineEdit(self)
        user_name_text_field.setFont(QFont(families[0], 12))
        user_name_text_field.setAlignment(Qt.AlignCenter)
        user_name_text_field.setFixedWidth(300)
        
        password_label = QLabel(self)
        password_label.setText("Password")
        password_label.setFont(QFont(families[0], 12))
        password_label.setAlignment(Qt.AlignCenter)

        password_text_field = QLineEdit(self)
        password_text_field.setFont(QFont(families[0], 12))
        password_text_field.setEchoMode(QLineEdit.Password)
        password_text_field.setFixedWidth(300)
        password_text_field.setAlignment(Qt.AlignCenter)

        password_label_rep = QLabel(self)
        password_label_rep.setText("Repeat Password")
        password_label_rep.setFont(QFont(families[0], 12))
        password_label_rep.setAlignment(Qt.AlignCenter)

        password_text_field_rep = QLineEdit(self)
        password_text_field_rep.setFont(QFont(families[0], 12))
        password_text_field_rep.setEchoMode(QLineEdit.Password)
        password_text_field_rep.setFixedWidth(300)
        password_text_field_rep.setAlignment(Qt.AlignCenter)

        # Buttons Layout
        buttons_vert_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addSpacing(2)

        # Register Button
        register_button = QPushButton(self)
        register_button.clicked.connect(lambda : postgres_register_user())
        register_button.setIcon(QIcon(r'images/register.png'))
        register_button.setIconSize(QSize(30, 30))
        register_button.setText("Create Account")
        register_button.setFont(QFont(families[0], 10))
        register_button.setFixedWidth(300)

        buttons_layout.addWidget(register_button)
        buttons_layout.setAlignment(Qt.AlignCenter)
        buttons_layout.addStretch()
        buttons_layout.addSpacing(10)
        buttons_vert_layout.addStretch()

        register_layout.addWidget(email_address_label)
        register_layout.addWidget(email_address_text_field)
        register_layout.addWidget(user_name_label)
        register_layout.addWidget(user_name_text_field)
        register_layout.addWidget(password_label)
        register_layout.addWidget(password_text_field)
        register_layout.addWidget(password_label_rep)
        register_layout.addWidget(password_text_field_rep)
        register_layout.setAlignment(Qt.AlignCenter)
        register_layout.addSpacing(10)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(register_layout)
        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)
        self.show()

        def postgres_register_user():
            
            user_id_valid = False
            email_address_valid = False
            user_name_valid = True
            password_valid = True
            
            create_account_errors = [] # This array will store the error during the user account creation and will return them to the error box.
            
            db_connect.database_connect() # Initialize connection to PostgreSQL DB
            
            # Generate random user ID
            while True:
                #user_id = ''.join(random.choice(string.digits) for i in range(1, 11))
                user_id = []
                for i in range(1, 11):
                    user_id.append(random.choice(string.digits))
                user_id = ''.join(user_id)
                db_connect.POSTGRES_CURSOR.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
                result = db_connect.POSTGRES_CURSOR.fetchone()
                if result:
                    continue
                else:
                    user_id_valid = True
                    break

            # Check if user email is valid and unique
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if re.match(email_pattern, email_address_text_field.text()):
                db_connect.POSTGRES_CURSOR.execute(f"SELECT * FROM users WHERE email_address = '{email_address_text_field.text()}'")
                result = db_connect.POSTGRES_CURSOR.fetchone()
                if result != None:
                    create_account_errors.append(f"Account with email address {email_address_text_field.text()} already exists.")
                else:
                    email_address_valid = True
            else:
                create_account_errors.append("Email address is not valid.")
            
            # Check if user name is valid and unique
            db_connect.POSTGRES_CURSOR.execute(f"SELECT * FROM users WHERE user_name = '{user_name_text_field.text()}'")
            result = db_connect.POSTGRES_CURSOR.fetchone()
            if result != None:
                create_account_errors.append(f"Username {user_name_text_field.text()} already exists.")
                user_name_valid = False

            # Check if password is valid
            #password_pattern = re.compile('!@#$%^&*()-+?_=,<>/')
            if password_text_field.text() != password_text_field_rep.text():
                password_valid = False
                create_account_errors.append('Password fields does not match.')
            if len(password_text_field.text()) < 8:
                password_valid = False
                create_account_errors.append('Password is too short. It must be at least 8 characters.')
            if not re.search(re.compile('[!@#$%^&*()-+?_=,<>/]'), password_text_field.text()):
                password_valid = False
                create_account_errors.append("Password must contain at least one special character.")
            if not re.search(re.compile('[A-Z]'), password_text_field.text()):
                password_valid = False
                create_account_errors.append("Password must contain at least one uppercase letter.")
            if not re.search(re.compile('[0-9]'), password_text_field.text()):
                password_valid = False
                create_account_errors.append("Password must contain at least one number.")
            
            # Check if all inputs are valid and create new user in the database
            if user_id_valid and email_address_valid and user_name_valid and password_valid:
                # PostgreSQL query to create new user account and new record in `users` table
                db_connect.POSTGRES_CURSOR.execute(f"CREATE USER {user_name_text_field.text()}_rpsuser WITH PASSWORD '{password_text_field.text()}';")
                db_connect.POSTGRES_CURSOR.execute(f"INSERT INTO users VALUES ('{user_id}', '{user_name_text_field.text()}', '{email_address_text_field.text()}');")
                #db_connect.POSTGRES_CURSOR.execute(f"INSERT INTO users VALUES ('{user_id}', '{user_name_text_field.text()}', '{email_address_text_field.text()}');")
                db_connect.POSTGRES_CURSOR.execute(f"GRANT rpsrole TO {user_name_text_field.text()}_rpsuser;")
                db_connect.POSTGRES_CONNECTION.commit()
                # Throw msg box 
                reg_msg_box = QMessageBox(self)
                reg_msg_box.setIcon(QMessageBox.Information)
                reg_msg_box.setText("Account created successfully")
                reg_msg_box.setWindowTitle("You have created a new account")
                reg_msg_box.setStandardButtons(QMessageBox.Ok)
                reg_box = reg_msg_box.exec()
                # Return to Login screen
                login.start_app()
                win.hide()

            else:
                # Throw error in the error box(GUI)
                error_msg_box = QMessageBox(self)
                error_msg_box.setIcon(QMessageBox.Warning)
                error_msg = '\n'.join(create_account_errors)
                error_msg_box.setText(error_msg)
                error_msg_box.setWindowTitle("Error during creating new account")
                error_msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box = error_msg_box.exec()


def init_app():
    app = QApplication(sys.argv)
    window = RegisterMenu()
    window.show()
    app.exec()

