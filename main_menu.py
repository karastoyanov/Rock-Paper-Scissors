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
        play_button.setText("play new game")
        play_button.setFont(QFont(families[0], 12))
        play_button.setFixedWidth(300)

        all_players_ranklist = QPushButton(self)
        all_players_ranklist.setText("players ranklist")
        all_players_ranklist.setFont(QFont(families[0], 12))
        all_players_ranklist.setFixedWidth(300)

        edit_user_button = QPushButton(self)
        edit_user_button.setText("edit user")
        edit_user_button.setFont(QFont(families[0], 12))
        edit_user_button.setFixedWidth(300)

        logout = QPushButton(self)
        logout.clicked.connect(lambda : open_logout())
        logout.setText("logout")
        logout.setFont(QFont(families[0], 12))
        logout.setFixedWidth(300)

        buttons_layout.addWidget(play_button)
        buttons_layout.addWidget(all_players_ranklist)
        buttons_layout.addWidget(edit_user_button)
        buttons_layout.addWidget(logout)
        buttons_layout.setAlignment(Qt.AlignLeft)
        buttons_layout.addStretch()
        buttons_layout.addSpacing(5)




        # Create separate group box for the right section
        group_two = QGroupBox(self)
        group_two.setFixedWidth(500)
        group_two.setFixedHeight(400)
        
        # User View Menu
        user_layout = QHBoxLayout()
        user_layout.addStretch()
        user_layout.addSpacing(5)

        # Create new vertical layout and insert it in the right section(group_two)
        user_name_info = QHBoxLayout(self)
        user_name_info.addStretch()
        user_name_info.addSpacing(5)
        
        # Create separate object inside the user_name_info vertical layout
        user_name = QLabel(self)
        db_connect.USER_POSTGRES_CURSOR.execute("SELECT current_user;")
        user_name_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        user_name_result = user_name_result[0]
        db_connect.USER_POSTGRES_CURSOR.execute(f"SELECT user_id FROM users WHERE user_name = '{user_name_result}'")
        user_id_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        user_id_result = user_id_result[0]
        db_connect.USER_POSTGRES_CURSOR.execute(f"SELECT user_rank FROM users WHERE user_name = '{user_name_result}'")
        user_rank_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        user_rank_result = user_rank_result[0]
        user_name.setText(f"hello {user_name_result}\nid: {user_id_result}\nrank: {user_rank_result}")
        user_name.setFont(QFont(families[0], 10))
        user_name.setAlignment(Qt.AlignLeft)
        
        # Create User Avatar
        image = QImage()
        url_image = r'https://github.com/karastoyanov/Rock-Paper-Scissors/blob/dev/images/avatars/soldier2.png?raw=true'
        image.loadFromData(requests.get(url_image).content)
        user_avatar_label = QLabel(self)
        user_avatar_label.setPixmap(QPixmap(image))
        user_avatar_label.setMaximumHeight(150)
        user_avatar_label.setMaximumWidth(150)
        user_avatar_label.setAlignment(Qt.AlignLeft)
        
        total_games_played = QLabel(self)
        db_connect.USER_POSTGRES_CURSOR.execute(f"SELECT total_games FROM users where user_name = '{user_name_result}'")
        total_games_played_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        total_games_played_result = total_games_played_result[0]
        total_games_played.setText(f'total games played: {total_games_played_result}\n')
        total_games_played.setFont(QFont(families[0], 10))
        total_games_played.setAlignment(Qt.AlignLeft)
        
        total_points = QLabel(self)
        db_connect.USER_POSTGRES_CURSOR.execute(f"SELECT total_points FROM users WHERE user_name = '{user_name_result}'")
        total_points_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        total_points_result = total_points_result[0]
        total_points.setText(f"total points: {total_points_result}")
        total_points.setFont(QFont(families[0], 10))
        total_points.setAlignment(Qt.AlignLeft)

        user_name_info.addWidget(user_name)
        user_name_info.addWidget(user_avatar_label)
        user_name_info.addWidget(total_games_played)
        user_name_info.addWidget(total_points)
        group_two.setLayout(user_name_info)

        # Add right section to the user layout and allign it to right(left is reserved for buttons)
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
