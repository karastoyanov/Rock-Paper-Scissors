#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout, QGroupBox, QGridLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random, sys
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
        email_address_text_field.setFont(QFont(families[0], 10))
        email_address_text_field.setAlignment(Qt.AlignCenter)
        email_address_text_field.setFixedWidth(300)

        user_name_label = QLabel(self)
        user_name_label.setText("User Name")
        user_name_label.setFont(QFont(families[0], 12))
        user_name_label.setAlignment(Qt.AlignCenter)

        user_name_text_field = QLineEdit(self)
        user_name_text_field.setFont(QFont(families[0], 10))
        user_name_text_field.setAlignment(Qt.AlignCenter)
        user_name_text_field.setFixedWidth(300)

        password_label = QLabel(self)
        password_label.setText("Password")
        password_label.setFont(QFont(families[0], 12))
        password_label.setAlignment(Qt.AlignCenter)

        password_text_field = QLineEdit(self)
        password_text_field.setFont(QFont(families[0], 10))
        password_text_field.setEchoMode(QLineEdit.Password)
        password_text_field.setFixedWidth(300)
        password_text_field.setAlignment(Qt.AlignCenter)

        password_label_rep = QLabel(self)
        password_label_rep.setText("Repeat Password")
        password_label_rep.setFont(QFont(families[0], 12))
        password_label_rep.setAlignment(Qt.AlignCenter)

        password_text_field_rep = QLineEdit(self)
        password_text_field_rep.setFont(QFont(families[0], 10))
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

app = QApplication(sys.argv)
window = RegisterMenu()
window.show()
app.exec()
