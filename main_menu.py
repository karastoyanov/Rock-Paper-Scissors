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
                             QGroupBox,
                             QGraphicsDropShadowEffect)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from colorama import Fore
import sys, requests
import db_connect, game
class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A game of Rock-Paper-Scissors - Main Menu")
        self.setWindowIcon(QIcon(r'images/console.png'))
        self.setGeometry(650, 300, 800, 50)
        self.setMaximumWidth(800)
        self.setMaximumHeight(300)
        
        """Init database connection as admin"""
        db_connect.database_connect()

        font = QFontDatabase.addApplicationFont(r'fonts/ElementalEnd.ttf')
        if font < 0: print("Error in fonts.")
        families = QFontDatabase.applicationFontFamilies(font)

        db_connect.USER_POSTGRES_CURSOR.execute("SELECT current_user;")
        user_name_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        user_name_result = user_name_result[0]
        user_name_result = user_name_result.split('_', 1)
        user_name_result = user_name_result[0]

        """Buttons layout"""
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addSpacing(5)

        new_game_button = QPushButton()
        new_game_button.clicked.connect(lambda : open_game())
        new_game_button.setText("new game")
        new_game_button.setFont(QFont(families[0], 12))
        new_game_button.setFixedWidth(300)

        players_ranklist_button = QPushButton()
        players_ranklist_button.setText("players ranklist")
        players_ranklist_button.setFont(QFont(families[0], 12))
        players_ranklist_button.setFixedWidth(300)

        edit_player_button = QPushButton()
        edit_player_button.setText("edit player")
        edit_player_button.setFont(QFont(families[0], 12))
        edit_player_button.setFixedWidth(300)

        logout_button = QPushButton()
        logout_button.setText("edit player")
        logout_button.setFont(QFont(families[0], 12))
        logout_button.setFixedWidth(300)


        buttons_layout.addWidget(new_game_button)
        buttons_layout.addWidget(players_ranklist_button)
        buttons_layout.addWidget(edit_player_button)
        buttons_layout.addWidget(logout_button)

        """Init the main layout"""
        main_layout = QVBoxLayout()
        main_layout.addLayout(buttons_layout)
        self.setLayout(main_layout)
        self.show()


        def open_game():
            db_connect.POSTGRES_CURSOR.execute(f"UPDATE users SET total_games = total_games + 1 WHERE user_name = '{user_name_result}'")
            game.start_app()
            win.hide()


def init_window():
    app = QApplication(sys.argv)
    window = start_app()
    app.exec_()

def start_app():
    global win
    win = MainMenu()
    win.show()

# init_window()
