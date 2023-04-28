#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout, QGroupBox, QGridLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, random
import db_connect


def start_app():
    global win
    win = Game()
    win.show()

class Game(QWidget):
    
    # Global variables for keeping the score and displaying a message at the end of each round
    PLAYER_POINTS = 0 
    AI_POINTS = 0
    ROUND_MESSAGE = ''
    ROUND_RESULT = ''
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A game of Rock-Paper-Scissors")
        self.setWindowIcon(QIcon(r'images/console.png'))
        self.setGeometry(650, 300, 800, 400)
        self.setMaximumWidth(800)
        self.setMaximumHeight(400)
        self.initUI()

    # Initialize the User Interface
    def initUI(self):
        font = QFontDatabase.addApplicationFont(r'fonts/ElementalEnd.ttf')
        if font < 0: print("Error in fonts.")
        families = QFontDatabase.applicationFontFamilies(font)
        
        # Central Text
        top_text = QVBoxLayout()
        top_text.addStretch()
        top_text.addSpacing(10)
        
        central_text = QLabel(self)
        central_text.setText("A game of")
        central_text.setFont(QFont(families[0], 12))
        central_text.setAlignment(Qt.AlignCenter)
        central_text_sec_line = QLabel(self)
        central_text_sec_line.setText("Rock-Paper-Scissors")
        central_text_sec_line.setFont(QFont(families[0], 24))
        central_text_sec_line.setAlignment(Qt.AlignCenter)
        
        weapon_text = QLabel(self)
        weapon_text.setText("Choose Your Weapon")
        weapon_text.setFont(QFont(families[0], 12))
        weapon_text.setAlignment(Qt.AlignCenter)
        
        top_text.addWidget(central_text)
        top_text.addWidget(central_text_sec_line)
        top_text.addWidget(weapon_text)
        top_text.addSpacing(15)
        

        
        

        # Player Buttons Layout Initialization
        virt_player_buttons = QVBoxLayout()
        player_buttons = QHBoxLayout()
        player_buttons.addStretch()
        player_buttons.addSpacing(0)

        # Rock Button
        rock_button = QPushButton(self)
        rock_button.clicked.connect(lambda : Game.game_round("rock"))
        rock_button.clicked.connect(lambda : result_counter_player.setText(f'PLAYER POINTS: {Game.PLAYER_POINTS}'))
        rock_button.clicked.connect(lambda : result_counter_ai.setText(f'AI POINTS: {Game.AI_POINTS}'))
        rock_button.clicked.connect(lambda : round_message_label.setText(f'[{Game.ROUND_MESSAGE}]'))
        rock_button.clicked.connect(lambda : round_result_text.setText(Game.ROUND_RESULT))
        rock_button.setIcon(QIcon(r'images/stone.png'))
        rock_button.setIconSize(QSize(30, 30))
        rock_button.setText("Rock")
        rock_button.setFont(QFont(families[0], 10))
        
        # Paper Button
        paper_button = QPushButton(self)
        paper_button.clicked.connect(lambda : Game.game_round("paper"))
        paper_button.clicked.connect(lambda : result_counter_player.setText(f'PLAYER POINTS: {Game.PLAYER_POINTS}'))
        paper_button.clicked.connect(lambda : result_counter_ai.setText(f'AI POINTS: {Game.AI_POINTS}'))
        paper_button.clicked.connect(lambda : round_message_label.setText(f'[{Game.ROUND_MESSAGE}]'))
        paper_button.clicked.connect(lambda : round_result_text.setText(Game.ROUND_RESULT))
        paper_button.setIcon(QIcon(r'images/file.png'))
        paper_button.setIconSize(QSize(30, 30))
        paper_button.setText("Paper")
        paper_button.setFont(QFont(families[0], 10))
        
        # Scissor Button
        scissors_button = QPushButton(self)
        scissors_button.clicked.connect(lambda : Game.game_round("scissors"))
        scissors_button.clicked.connect(lambda : result_counter_player.setText(f'PLAYER POINTS: {Game.PLAYER_POINTS}'))
        scissors_button.clicked.connect(lambda : result_counter_ai.setText(f'AI POINTS: {Game.AI_POINTS}'))
        scissors_button.clicked.connect(lambda : round_message_label.setText(f'[{Game.ROUND_MESSAGE}]'))
        scissors_button.clicked.connect(lambda : round_result_text.setText(Game.ROUND_RESULT))
        scissors_button.setIcon(QIcon(r'images/scissors.png'))
        scissors_button.setIconSize(QSize(30, 30))
        scissors_button.setText("Scissors")
        scissors_button.setFont(QFont(families[0], 10))
        
        # Add buttons to widget
        player_buttons.addWidget(rock_button)
        player_buttons.addWidget(paper_button)
        player_buttons.addWidget(scissors_button)
        player_buttons.addSpacing(0)
        player_buttons.addStretch()
        virt_player_buttons.addStretch()
        


        # Round Message
        round_message = QVBoxLayout()
        round_message.addSpacing(20)
        round_message_label = QLabel(self)
        round_message_label.setText(f'[]')
        round_message_label.setFont(QFont(families[0], 10))
        round_message_label.setAlignment(Qt.AlignCenter)
        round_message.addWidget(round_message_label)
        
        # Result result
        round_result = QVBoxLayout()
        round_result.addSpacing(10)
        round_result_text = QLabel(self)
        round_result_text.setText(Game.ROUND_RESULT)
        round_result_text.setFont(QFont(families[0], 10))
        round_result_text.setAlignment(Qt.AlignCenter)
        round_result.addWidget(round_result_text)
        
        


        # Result Counter
        result_counter = QVBoxLayout()
        result_counter.addSpacing(50)
        result_counter_player = QLabel(self)
        result_counter_player.setText(f'PLAYER POINTS: {Game.PLAYER_POINTS}') 
        result_counter_player.setFont(QFont(families[0], 10))
        result_counter_player.setAlignment(Qt.AlignCenter)
        result_counter_ai = QLabel(self)
        result_counter_ai.setText(f'AI POINTS: {Game.AI_POINTS}')
        result_counter_ai.setFont(QFont(families[0], 10))
        result_counter_ai.setAlignment(Qt.AlignCenter)
        result_counter.addWidget(result_counter_player)
        result_counter.addWidget(result_counter_ai)

        # Main Layout Setup
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_text)
        main_layout.addLayout(player_buttons)
        main_layout.addLayout(round_result)
        main_layout.addLayout(round_message)
        main_layout.addLayout(result_counter)
        main_layout.addStretch()
        self.setLayout(main_layout)
        self.show()

    # Main Game Funcionality and Message Handling
    def game_round(player_choice):
        db_connect.database_connect() # Init connection to the database(Admin access needed to update the result)
        # Each time when the player wins, 1 point should be added to his `total_points` column in PostgreSQL users table
        
        # Get the current logged-in player
        db_connect.USER_POSTGRES_CURSOR.execute("SELECT current_user;")
        user_name_result = db_connect.USER_POSTGRES_CURSOR.fetchone()
        user_name_result = user_name_result[0]
        
        possible_ai_choice = ["rock", "paper", "scissors"]
        ai_choice = random.choice(possible_ai_choice)
        player_wins = False
        ai_wins = False

        if player_choice == "rock":
            if ai_choice == "rock":
                print("Tie!")
                player_wins, ai_wins = False, False
                Game.ROUND_RESULT = "It's a tie!"
            elif ai_choice == "paper":
                print("Computer wins!")
                player_wins, ai_wins = False, True
                Game.AI_POINTS += 1
                Game.ROUND_RESULT = 'You have lost!'
            elif ai_choice == "scissors":
                print("Player wins!")
                db_connect.POSTGRES_CURSOR.execute(f"UPDATE users SET total_points = total_points + 1 WHERE user_name = '{user_name_result}'")
                db_connect.POSTGRES_CONNECTION.commit()
                player_wins, ai_wins = True, False
                Game.PLAYER_POINTS += 1
                Game.ROUND_RESULT = 'You have won!'

        if player_choice == "paper":
            if ai_choice == "rock":
                print("Player wins!")
                db_connect.POSTGRES_CURSOR.execute(f"UPDATE users SET total_points = total_points + 1 WHERE user_name = '{user_name_result}'")
                db_connect.POSTGRES_CONNECTION.commit()
                player_wins, ai_wins = True, False
                Game.PLAYER_POINTS += 1
                Game.ROUND_RESULT = 'You have won!'
            elif ai_choice == "paper":
                print("Tie!")
                player_wins, ai_wins = False, False
                Game.ROUND_RESULT = "It's a tie!"
            elif ai_choice == "scissors":
                print("Computer wins!")
                player_wins, ai_wins = False, True
                Game.AI_POINTS += 1
                Game.ROUND_RESULT = 'You have lost!'

        if player_choice == "scissors":
            if ai_choice == "rock":
                print("Computer wins!")
                player_wins, ai_wins = False, True
                Game.AI_POINTS += 1
                Game.ROUND_RESULT = 'You have lost!'
            elif ai_choice == "paper":
                print("Player wins!")
                db_connect.POSTGRES_CURSOR.execute(f"UPDATE users SET total_points = total_points + 1 WHERE user_name = '{user_name_result}'")
                db_connect.POSTGRES_CONNECTION.commit()
                player_wins, ai_wins = True, False
                Game.PLAYER_POINTS += 1
                Game.ROUND_RESULT = 'You have won!'
            elif ai_choice == "scissors":
                print("Tie!")
                player_wins, ai_wins = False, False
                Game.ROUND_RESULT = "It's a tie!"
        
        player_wins_messages = [
            "Good job, soldier!",
            "Keep the good work, private!",
            "Keep fraging soldier!"
            ]
        ai_wins_messages = [
            "Better luck next time!",
            "Common soldier, the fate of the humanity is in your hands!"
        ]
        tie_messages = [
            "It's a Tie! You get another chance, private!"
        ]
        
        round_message = ''
    
        if player_wins == True and ai_wins == False:
            round_message = random.choice(player_wins_messages)
        elif player_wins == False and ai_wins == True:
            round_message = random.choice(ai_wins_messages)
        elif player_wins == False and ai_wins == False:
            round_message = random.choice(tie_messages)
        Game.ROUND_MESSAGE = round_message

def init_window():
    app = QApplication(sys.argv)
    window = start_app()
    app.exec_()
