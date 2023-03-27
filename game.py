#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout, QGroupBox)
from PyQt5.QtGui import (QIcon, QPixmap, QFont, QFontDatabase)
from PyQt5.QtCore import (QSize, Qt)
import sys


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A Game of Rock-Paper-Scissors")
        self.setWindowIcon(QIcon(r'images/console.png'))
        self.setFixedSize(600, 300)
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

        # Icons
        






if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = MainMenu()
    win.show()
    app.exec_()
