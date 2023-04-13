#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout, QGroupBox, QGridLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random, sys
import pysnc


class LoginMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A game of Rock-Paper-Scissors - Login Screen")
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

        # Layout for the user name layout
        login_layout = QVBoxLayout()
        login_layout.addStretch()
        login_layout.addSpacing(10)

        user_name_label = QLabel(self)
        user_name_label.setText('User Name')
        user_name_label.setFont(QFont(families[0], 10))
        user_name_label.setAlignment(Qt.AlignCenter)
    
        user_name_text_field = QLineEdit(self)
        user_name_text_field.setFont(QFont(families[0], 12))
        user_name_text_field.setAlignment(Qt.AlignCenter)
        user_name_text_field.setFixedWidth(300)

        password_label = QLabel(self)
        password_label.setText('Password')
        password_label.setFont(QFont(families[0], 10))
        password_label.setAlignment(Qt.AlignCenter)

        password_text_field = QLineEdit(self)
        password_text_field.setEchoMode(QLineEdit.Password)
        password_text_field.setFont(QFont(families[0], 12))
        password_text_field.setAlignment(Qt.AlignCenter)
        password_text_field.setFixedWidth(300)

        login_layout.addWidget(user_name_label)
        login_layout.addWidget(user_name_text_field)
        login_layout.addWidget(password_label)
        login_layout.addWidget(password_text_field)
        login_layout.setAlignment(Qt.AlignCenter)
        login_layout.addSpacing(10)

        # Buttons Layout
        buttons_vert_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addSpacing(2)

        # Login Button
        login_button = QPushButton(self)
        login_button.setIcon(QIcon(r'images/login.png'))
        login_button.setIconSize(QSize(30, 30))
        login_button.setText("Login")
        login_button.setFixedWidth(147)
        login_button.setFont(QFont(families[0], 10))

        register_button = QPushButton(self)
        register_button.setIcon(QIcon(r'images/register.png'))
        register_button.setIconSize(QSize(30, 30))
        register_button.setText("Register")
        register_button.setFixedWidth(147)
        register_button.setFont(QFont(families[0], 10))

        buttons_layout.addWidget(login_button)
        buttons_layout.addWidget(register_button)
        buttons_layout.addStretch()
        buttons_layout.addSpacing(2)
        buttons_vert_layout.addStretch()

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(login_layout)
        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)
        self.show()









app = QApplication(sys.argv)
window = LoginMenu()
window.show()
app.exec()


#client = pysnc.ServiceNowClient('dev109438', ('admin', 'LrmsjVJB@8^3'))
#gr = client.GlideRecord('problem')
