#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton, 
                             QLabel, 
                             QLineEdit, 
                             QMessageBox, 
                             QHBoxLayout, 
                             QVBoxLayout) 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random, sys
import db_connect, main_menu, register

USERNAME = ''


def start_app():
    global win
    win = LoginMenu()
    win.show()


class LoginMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A game of Rock-Paper-Scissors - Login Screen")
        self.setWindowIcon(QIcon(r'images/console.png'))
        self.setGeometry(650, 300, 800, 400)
        self.setMaximumWidth(800)
        self.setMaximumHeight(400)
        self.initUI()
    
    global window

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
        user_name_label.setText('user Name')
        user_name_label.setFont(QFont(families[0], 10))
        user_name_label.setAlignment(Qt.AlignCenter)
    
        user_name_text_field = QLineEdit(self)
        user_name_text_field.setFont(QFont(families[0], 10))
        user_name_text_field.setAlignment(Qt.AlignCenter)
        user_name_text_field.setFixedWidth(400)

        password_label = QLabel(self)
        password_label.setText('password')
        password_label.setFont(QFont(families[0], 10))
        password_label.setAlignment(Qt.AlignCenter)

        password_text_field = QLineEdit(self)
        password_text_field.setEchoMode(QLineEdit.Password)
        password_text_field.setFont(QFont('Arial', 10))
        password_text_field.setAlignment(Qt.AlignCenter)
        password_text_field.setFixedWidth(400)

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
        login_button.clicked.connect(lambda : open_login(self))
        login_button.setIcon(QIcon(r'images/login.png'))
        login_button.setIconSize(QSize(30, 30))
        login_button.setText("login")
        login_button.setFixedWidth(200)
        login_button.setFont(QFont(families[0], 10))

        register_button = QPushButton(self)
        register_button.clicked.connect(lambda : open_register(self))
        register_button.setIcon(QIcon(r'images/register.png'))
        register_button.setIconSize(QSize(30, 30))
        register_button.setText("register")
        register_button.setFixedWidth(200)
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
        
        def open_login(self):
            try:
                db_connect.user_connect(user_name_text_field.text().lower(), password_text_field.text()) # Init DB Connection
                print("Connected")
                main_menu.start_app()
                win.hide()
            except:
                error_msg_box = QMessageBox(self)
                error_msg_box.setIcon(QMessageBox.Warning)
                error_msg_box.setText("Wrong user name or password")
                error_msg_box.setWindowTitle("Error during login")
                error_msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box = error_msg_box.exec()

        def open_register(self):
            register.start_app()
            win.hide()
            
        



app = QApplication(sys.argv)
window = start_app()
app.exec_()



