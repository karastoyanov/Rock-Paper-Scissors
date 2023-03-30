#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout, QGroupBox, QGridLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A game of Rock-Paper-Scissors")
        self.setWindowIcon(QIcon(r'images/console.png'))
        self.setGeometry(300, 300, 650, 400)

        font = QFontDatabase.addApplicationFont(r'fonts/ElementalEnd.ttf')
        if font < 0: print("Error in fonts.")
        families = QFontDatabase.applicationFontFamilies(font)


        # Main Window Layout containing all objects
        main_layout = QGridLayout()
        self.setLayout(main_layout)


        one_text_layout = QVBoxLayout() # Horizontal layout for central_text variable
        two_text_layout = QVBoxLayout() # Horizontal layout for central_text_sec_line variable
        player_buttons = QHBoxLayout()


        # Central Text
        central_text = QLabel(self)
        central_text.setText("A game of")
        central_text.setFont(QFont(families[0], 12))
        central_text_sec_line = QLabel(self)
        central_text_sec_line.setText("Rock-Paper-Scissors")
        central_text_sec_line.setFont(QFont(families[0], 24))
        one_text_layout.addWidget(central_text)
        two_text_layout.addWidget(central_text_sec_line)
        main_layout.addLayout(one_text_layout, 0, 0)
        main_layout.addLayout(two_text_layout, 1, 0)

        # Rock Button
        rock_button = QPushButton(self)
        rock_button.setIcon(QIcon(r'images/stone.png'))
        rock_button.setIconSize(QSize(30, 30))
        rock_button.setText("Rock")
        rock_button.setFont(QFont(families[0], 8))
        rock_button.setGeometry(90, 170, 120, 50)
        rock_button.show()
        # Paper Button
        paper_button = QPushButton(self)
        paper_button.setIcon(QIcon(r'images/file.png'))
        paper_button.setIconSize(QSize(30, 30))
        paper_button.setText("Paper")
        paper_button.setFont(QFont(families[0], 8))
        paper_button.setGeometry(240, 170, 120, 50)
        paper_button.show()
        # Scissor Button
        scissors_button = QPushButton(self)
        scissors_button.setIcon(QIcon(r'images/scissors.png'))
        scissors_button.setIconSize(QSize(30, 30))
        scissors_button.setText("Scissors")
        scissors_button.setFont(QFont(families[0], 8))
        player_buttons.addWidget(rock_button)
        player_buttons.addWidget(paper_button)
        player_buttons.addWidget(scissors_button)
        main_layout.addLayout(player_buttons, 2, 0)



        self.show()






app = QApplication(sys.argv)
window = MainMenu()
window.show()
app.exec()


