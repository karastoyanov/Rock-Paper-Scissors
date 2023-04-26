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
import db_connect, login

def start_app():
    global win
    win = MainMenu()
    win.show()

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A game of Rock-Paper-Scissors - Main Menu")
        self.setWindowIcon(QIcon(r'images/console.png'))
        self.setGeometry(650, 300, 800, 300)
        self.setMaximumWidth(800)
        self.setMaximumHeight(300)
        self.initUI()

    def initUI(self):
        # Fonts setting
        font = QFontDatabase.addApplicationFont(r'fonts/ElementalEnd.ttf')
        if font < 0: print("Error in fonts.")
        families = QFontDatabase.applicationFontFamilies(font)
        
        # Right group objects (for buttons layout)
        # Buttons Layout
        buttons_layout = QVBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addSpacing(5)
        
        play_button = QPushButton(self)
        play_button.setText("play new game")
        play_button.setFont(QFont(families[0], 12))
        play_button.setFixedWidth(300)
        play_button.setStyleSheet("background-color: #009933; color: #FFFFFF;")


        all_players_ranklist = QPushButton(self)
        all_players_ranklist.setText("players ranklist")
        all_players_ranklist.setFont(QFont(families[0], 12))
        all_players_ranklist.setFixedWidth(300)
        all_players_ranklist.setStyleSheet("background-color: #009933; color: #FFFFFF;")

        edit_user_button = QPushButton(self)
        edit_user_button.setText("edit user")
        edit_user_button.setFont(QFont(families[0], 12))
        edit_user_button.setFixedWidth(300)
        edit_user_button.setStyleSheet("background-color: #009933; color: #FFFFFF;")

        logout = QPushButton(self)
        logout.clicked.connect(lambda : open_logout())
        logout.setText("logout")
        logout.setFont(QFont(families[0], 12))
        logout.setFixedWidth(300)
        logout.setStyleSheet("background-color: #009933; color: #FFFFFF;")
        
        right_dummy_group = QGroupBox(self)
        right_dummy_group.setFixedWidth(300)
        right_dummy_group.setFixedHeight(80)
       

        dummy_layout = QVBoxLayout()
        current_version = QLabel()
        current_version.setText("Current Version: 2.0-alpha")
        current_version.setFont(QFont('Calibri', 9))

        current_server_version = QLabel()
        db_connect.USER_POSTGRES_CURSOR.execute(f"SHOW server_version")
        current_server_version_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        server_version = current_server_version_result[0]
        linux_version = server_version[6:17]
        postgre_version = server_version[0:4]
        current_server_version.setText(f"Current PostgreSQL version: {postgre_version}")
        current_server_version.setFont(QFont('Calibri', 9))
        current_linux_version = QLabel()
        current_linux_version.setText(f"Current Linux version: {linux_version}")
        current_linux_version.setFont(QFont('Calibri', 9))

        

        dummy_layout.addWidget(current_version)
        dummy_layout.addWidget(current_server_version)
        dummy_layout.addWidget(current_linux_version)

        right_dummy_group.setLayout(dummy_layout)

        buttons_layout.addWidget(play_button)
        buttons_layout.addWidget(all_players_ranklist)
        buttons_layout.addWidget(edit_user_button)
        buttons_layout.addWidget(logout)
        buttons_layout.addWidget(right_dummy_group)
        buttons_layout.setAlignment(Qt.AlignRight)
        buttons_layout.addStretch()
        buttons_layout.addSpacing(5)
        
        

        
        # Left group objects (User stats)
        # Vertical layout for all elements in the left objects group
        user_stats_layout = QVBoxLayout()
        user_stats_layout.addStretch()
        user_stats_layout.addSpacing(5)

        # Vertical layout for the elements in the left objects group (User Name, User ID, User Rank and User Avatar)
        user_stats_content_layout = QVBoxLayout()
        user_name = QLabel()
        db_connect.USER_POSTGRES_CURSOR.execute("SELECT current_user;")
        user_name_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        user_name_result = user_name_result[0]
        user_name.setText(f"welcome {user_name_result}")
        user_name.setFont(QFont(families[0], 10))
        user_name.setStyleSheet("color: #009933;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(5)
        user_name.setGraphicsEffect(shadow)
        
        user_id = QLabel()
        db_connect.USER_POSTGRES_CURSOR.execute(f"SELECT user_id FROM users WHERE user_name = '{user_name_result}'")
        user_id_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        user_id_result = user_id_result[0]
        user_id.setText(f"user id: {user_id_result}")
        user_id.setFont(QFont(families[0], 10))
        user_id.setStyleSheet("color: #009933;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(5)
        user_id.setGraphicsEffect(shadow)
        
        user_rank = QLabel()
        db_connect.USER_POSTGRES_CURSOR.execute(f"SELECT user_rank FROM users WHERE user_name = '{user_name_result}'")
        user_rank_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        user_rank_result = user_rank_result[0]
        user_rank.setText(f"rank: {user_rank_result}")
        user_rank.setFont(QFont(families[0], 10))
        user_rank.setStyleSheet("color: #009933;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(5)
        user_rank.setGraphicsEffect(shadow)      

        total_games = QLabel()
        db_connect.USER_POSTGRES_CURSOR.execute(f"SELECT total_games FROM users WHERE user_name = '{user_name_result}'")
        total_games_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        total_games_result = total_games_result[0]
        total_games.setText(f"total games played: {total_games_result}")
        total_games.setFont(QFont(families[0], 10))
        total_games.setStyleSheet("color: #009933;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(5)
        total_games.setGraphicsEffect(shadow)

        total_points = QLabel()
        db_connect.USER_POSTGRES_CURSOR.execute(f"SELECT total_points FROM users WHERE user_name = '{user_name_result}'")
        total_points_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        total_points_result = total_points_result[0]
        total_points.setText(f"total points: {total_points_result}")
        total_points.setFont(QFont(families[0], 10))
        total_points.setStyleSheet("color: #009933;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(5)
        total_points.setGraphicsEffect(shadow)
        
        
        
        
        # Add items to the first line on the left side
        user_stats_content_layout.addWidget(user_name)
        user_stats_content_layout.addWidget(user_id)
        user_stats_content_layout.addWidget(user_rank)
        user_stats_content_layout.addWidget(total_games)
        user_stats_content_layout.addWidget(total_points)
        # Add items to the left side
        user_stats_layout.addLayout(user_stats_content_layout)


        # Main Layout Init
        main_layout = QHBoxLayout()
        main_layout.addLayout(user_stats_layout)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)
        self.show()
        
        def open_logout():
            login.start_app()
            win.hide()

def init_window():
    app = QApplication(sys.argv)
    window = start_app()
    app.exec_()

#app = QApplication(sys.argv)
#window = start_app()
#app.exec_()

