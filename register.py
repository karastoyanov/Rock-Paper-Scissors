#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout, QGroupBox, QGridLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random, sys, re
import pysnc

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
        # email_address_text_field.setFont(QFont(families[0], 10))
        email_address_text_field.setAlignment(Qt.AlignCenter)
        email_address_text_field.setFixedWidth(300)

        user_name_label = QLabel(self)
        user_name_label.setText("User Name")
        user_name_label.setFont(QFont(families[0], 12))
        user_name_label.setAlignment(Qt.AlignCenter)

        user_name_text_field = QLineEdit(self)
        # user_name_text_field.setFont(QFont(families[0], 10))
        user_name_text_field.setAlignment(Qt.AlignCenter)
        user_name_text_field.setFixedWidth(300)
        
        password_label = QLabel(self)
        password_label.setText("Password")
        password_label.setFont(QFont(families[0], 12))
        password_label.setAlignment(Qt.AlignCenter)

        password_text_field = QLineEdit(self)
        # password_text_field.setFont(QFont(families[0], 10))
        password_text_field.setEchoMode(QLineEdit.Password)
        password_text_field.setFixedWidth(300)
        password_text_field.setAlignment(Qt.AlignCenter)

        password_label_rep = QLabel(self)
        password_label_rep.setText("Repeat Password")
        password_label_rep.setFont(QFont(families[0], 12))
        password_label_rep.setAlignment(Qt.AlignCenter)

        password_text_field_rep = QLineEdit(self)
        # password_text_field_rep.setFont(QFont(families[0], 10))
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
        register_button.clicked.connect(lambda : servicenow_register_user())
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

        def servicenow_register_user():
            client = pysnc.ServiceNowClient('dev109438', ('admin', 'LrmsjVJB@8^3'))
            
            email_address_valid = False
            user_name_valid = True
            password_valid = True
            
            # Check if user email is valid
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if re.match(email_pattern, email_address_text_field.text()):
                print("Email Matches")
                email_address_valid = True
            else:
                print("Email does not match")
            
            # Check if user name is valid (unique)
            gr_custom_table = client.GlideRecord('u_rock_paper_scissors_users')
            gr_custom_table.query()
            gr_custom_table.next()
            for custom_user in gr_custom_table:
                if custom_user.get_display_value('u_user_name') == user_name_text_field:
                    user_name_valid = False
                    break
            # gr_sys_table = client.GlideRecord('sys_user')
            # gr_sys_table.query()
            # gr_sys_table.next()
            # for sys_user in gr_sys_table:
            #     if sys_user.get_display_value('user_name') == user_name_text_field:
            #         user_name_valid = False
            #         break
            
            # Check if user password is valid
            password_pattern = r'!@#$%^&*()-+?_=,<>/'
            password_errors = []
            if password_text_field.text() != password_text_field_rep.text():
                password_valid = False
                password_errors.append('Password does not match')
            if len(password_text_field.text()) < 8:
                password_valid = False
                password_errors.append('Password is too short. It must be at least 8 characters.')
            if not re.match(password_pattern, password_text_field.text()):
                password_valid = False
                password_errors.append("Password must contain at least one special character.")
            if not re.match("[A-Z]", password_text_field.text()):
                password_valid = False
                password_errors.append("Password must contain at least one uppercase letter.")
            if not re.match("[0-9]", password_text_field.text()):
                password_valid = False
                password_errors.append("Password must contain at least one number.")
                    
                
                    
            
            
            
            
            # # Create New User in Rock-Paper-Scissors Table
            # gr = client.GlideRecord('u_rock_paper_scissors_users')
            # gr.initialize()
            # gr.u_user_name = user_name_text_field.text()
            # gr.u_user_email = email_address_text_field.text()
            # gr.insert()

            # # Create New User in sys_user table
            # gr = client.GlideRecord('sys_user')
            # gr.initialize()
            # gr.user_name = user_name_text_field.text()
            # gr.name = user_name_text_field.text()
            # gr.email = email_address_text_field.text()
            # gr.insert()








app = QApplication(sys.argv)
window = RegisterMenu()
window.show()
app.exec()
