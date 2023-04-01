#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout, QGroupBox, QGridLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import game

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A game of Rock-Paper-Scissors")
        self.setWindowIcon(QIcon(r'images/console.png'))
        self.setGeometry(650, 300, 650, 400)
        self.setMaximumWidth(650)
        self.setMaximumHeight(400)
        self.initUI()
    

    def initUI(self):
        font = QFontDatabase.addApplicationFont(r'fonts/ElementalEnd.ttf')
        if font < 0: print("Error in fonts.")
        families = QFontDatabase.applicationFontFamilies(font)
        

        #-----------------------------------------
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
        weapon_text.setFont(QFont(families[0], 8))
        weapon_text.setAlignment(Qt.AlignCenter)
        top_text.addWidget(central_text)
        top_text.addWidget(central_text_sec_line)
        top_text.addWidget(weapon_text)
        #top_text.addStretch(0)
        top_text.addSpacing(15)
        #-----------------------------------------

        #-----------------------------------------
        # Player Buttons
        virt_player_buttons = QVBoxLayout()
        player_buttons = QHBoxLayout()
        player_buttons.addStretch()
        player_buttons.addSpacing(0)

        # Rock Button
        rock_button = QPushButton(self)
        rock_button.setIcon(QIcon(r'images/stone.png'))
        rock_button.setIconSize(QSize(30, 30))
        rock_button.setText("Rock")
        rock_button.setFont(QFont(families[0], 8))
        # Paper Button
        paper_button = QPushButton(self)
        paper_button.setIcon(QIcon(r'images/file.png'))
        paper_button.setIconSize(QSize(30, 30))
        paper_button.setText("Paper")
        paper_button.setFont(QFont(families[0], 8))
        # Scissor Button
        scissors_button = QPushButton(self)
        scissors_button.setIcon(QIcon(r'images/scissors.png'))
        scissors_button.setIconSize(QSize(30, 30))
        scissors_button.setText("Scissors")
        scissors_button.setFont(QFont(families[0], 8))

        player_buttons.addWidget(rock_button)
        player_buttons.addWidget(paper_button)
        player_buttons.addWidget(scissors_button)
        player_buttons.addSpacing(0)
        player_buttons.addStretch()
        virt_player_buttons.addStretch()
        #-----------------------------------------
         
        #-----------------------------------------
        # Current Round Message
        round_message = QVBoxLayout()
        round_message.addSpacing(20)

        round_message_label = QLabel(self)
        round_message_label.setText("[]")
        round_message_label.setFont(QFont(families[0], 12))
        round_message_label.setAlignment(Qt.AlignCenter)
        round_message.addWidget(round_message_label)
        #-----------------------------------------

        #-----------------------------------------
        # Result Counter
        result_counter = QVBoxLayout()
        result_counter.addSpacing(50)

        result_counter_player = QLabel(self)
        result_counter_player.setText("PLAYER: ")
        result_counter_player.setFont(QFont(families[0], 10))
        result_counter_player.setAlignment(Qt.AlignCenter)
        result_counter_ai = QLabel(self)
        result_counter_ai.setText("AI: ")
        result_counter_ai.setFont(QFont(families[0], 10))
        result_counter_ai.setAlignment(Qt.AlignCenter)
        result_counter.addWidget(result_counter_player)
        result_counter.addWidget(result_counter_ai)




        main_layout = QVBoxLayout()
        main_layout.addLayout(top_text)
        main_layout.addLayout(player_buttons)
        main_layout.addLayout(round_message)
        main_layout.addLayout(result_counter)
        main_layout.addStretch()

        self.setLayout(main_layout)
        self.show()



app = QApplication(sys.argv)
window = MainMenu()
window.show()
app.exec()


