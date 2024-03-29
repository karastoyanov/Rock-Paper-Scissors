#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout, QGroupBox)
from PyQt5.QtGui import (QIcon, QPixmap, QFont, QFontDatabase)
from PyQt5.QtCore import (QSize, Qt)
import sys


class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A Game of Rock-Paper-Scissors")
        self.setWindowIcon(QIcon(r'images/console.png'))
        self.setFixedSize(600, 350)
        self.show
        
        font = QFontDatabase.addApplicationFont(r'fonts/ElementalEnd.ttf')
        if font < 0: print("Error in fonts.")
        families = QFontDatabase.applicationFontFamilies(font)


        # Central Text
        self.central_text = QLabel(self)
        self.central_text.setText("A game of")
        self.central_text.setFont(QFont(families[0], 12))
        self.central_text.setGeometry(240, 10, 200, 100)
        self.central_text_sec_line = QLabel(self)
        self.central_text_sec_line.setText("Rock-Paper-Scissors")
        self.central_text_sec_line.setFont(QFont(families[0], 24))
        self.central_text_sec_line.setGeometry(52, 50, 600, 100)
        self.central_text.show()
        self.central_text_sec_line.show()

        # Player choice text
        self.player_choice_text = QLabel(self)
        self.player_choice_text.setText("Choose your weapon")
        self.player_choice_text.setFont(QFont(families[0], 8))
        self.player_choice_text.setGeometry(215, 140, 170, 10)
        self.player_choice_text.show()

        # Player Buttons
        # Rock Button
        self.rock_button = QPushButton(self)
        self.rock_button.setIcon(QIcon(r'images/stone.png'))
        self.rock_button.setIconSize(QSize(30, 30))
        self.rock_button.setText("Rock")
        self.rock_button.setFont(QFont(families[0], 8))
        self.rock_button.setGeometry(90, 170, 120, 50)
        self.rock_button.show()

        # Paper Button
        self.paper_button = QPushButton(self)
        self.paper_button.setIcon(QIcon(r'images/file.png'))
        self.paper_button.setIconSize(QSize(30, 30))
        self.paper_button.setText("Paper")
        self.paper_button.setFont(QFont(families[0], 8))
        self.paper_button.setGeometry(240, 170, 120, 50)
        self.paper_button.show()

        # Scissor Button
        self.scissors_button = QPushButton(self)
        self.scissors_button.setIcon(QIcon(r'images/scissors.png'))
        self.scissors_button.setIconSize(QSize(30, 30))
        self.scissors_button.setText("Scissors")
        self.scissors_button.setFont(QFont(families[0], 8))
        self.scissors_button.setGeometry(390, 170, 120, 50)
        self.scissors_button.show()

        # Exit Button
        self.exit_button = QPushButton(self)
        self.exit_button.setIcon(QIcon(r'images/exit.png'))
        self.exit_button.setIconSize(QSize(20, 20))
        self.exit_button.setText("Exit")
        self.exit_button.setFont(QFont(families[0], 8))
        self.exit_button.setGeometry(520, 10, 60, 20)
        self.exit_button.show()
        
        # Result Stats
        self.player_result = QLabel(self)
        self.player_result.setText("Player: ")
        self.player_result.setFont(QFont(families[0], 8))
        self.player_result.setGeometry(480, 300, 80, 20)
        self.player_result.show()

        self.ai_result = QLabel(self)
        self.ai_result.setText("AI: ")
        self.ai_result.setFont(QFont(families[0], 8))
        self.ai_result.setGeometry(480, 320, 80, 20)
        self.ai_result.show()


if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = Game()
    win.show()
    app.exec_()
