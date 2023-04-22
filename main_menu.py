#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, 
                             QWidget, 
                             QPushButton, 
                             QLabel, 
                             QLineEdit, 
                             QMessageBox, 
                             QPlainTextEdit, 
                             QHBoxLayout, 
                             QVBoxLayout,
                             QGroupBox) 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

def start_app():
    global win
    win = MainMenu()
    win.show()

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A game of Rock-Paper-Scissors - Main Menu")
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
        
        # Main Horizontal Layout
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch()
        horizontal_layout.addSpacing(5)

        # Buttons Layout
        buttons_layout = QVBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addSpacing(5)

        play_button = QPushButton(self)
        play_button.setText("Play New Game")
        play_button.setFont(QFont(families[0], 12))
        play_button.setFixedWidth(300)

        all_players_ranklist = QPushButton(self)
        all_players_ranklist.setText("Players ranklist")
        all_players_ranklist.setFont(QFont(families[0], 12))
        all_players_ranklist.setFixedWidth(300)

        edit_user_button = QPushButton(self)
        edit_user_button.setText("Edit User")
        edit_user_button.setFont(QFont(families[0], 12))
        edit_user_button.setFixedWidth(300)

        new_login_button = QPushButton(self)
        new_login_button.setText("Logout")
        new_login_button.setFont(QFont(families[0], 12))
        new_login_button.setFixedWidth(300)

        buttons_layout.addWidget(play_button)
        buttons_layout.addWidget(all_players_ranklist)
        buttons_layout.addWidget(edit_user_button)
        buttons_layout.addWidget(new_login_button)
        buttons_layout.setAlignment(Qt.AlignLeft)
        buttons_layout.addStretch()
        buttons_layout.addSpacing(5)

        # User View Menu
        user_layout = QVBoxLayout()
        user_layout.addStretch()
        user_layout.addSpacing(5)

        group_two = QGroupBox(self)
        group_two.setFixedWidth(500)
        group_two.setFixedHeight(400)

        user_layout.addWidget(group_two)
        user_layout.setAlignment(Qt.AlignRight)
        user_layout.addStretch()
        user_layout.addSpacing(5)

        horizontal_layout.addLayout(buttons_layout)
        horizontal_layout.addLayout(user_layout)
        horizontal_layout.addStretch()
        horizontal_layout.addSpacing(5)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(horizontal_layout)
        self.setLayout(main_layout)
        self.show()

def init_window():
    app = QApplication(sys.argv)
    window = start_app()
    app.exec_()

