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
        self.initUI()
    

    def initUI(self):
        font = QFontDatabase.addApplicationFont(r'fonts/ElementalEnd.ttf')
        if font < 0: print("Error in fonts.")
        families = QFontDatabase.applicationFontFamilies(font)
        
        top_text = QVBoxLayout()
        top_text.addStretch(10)

        # Central Text
        central_text = QLabel(self)
        central_text.setText("A game of")
        central_text.setFont(QFont(families[0], 12))
        central_text.setAlignment(Qt.AlignCenter)
        central_text_sec_line = QLabel(self)
        central_text_sec_line.setText("Rock-Paper-Scissors")
        central_text_sec_line.setFont(QFont(families[0], 24))
        central_text_sec_line.setAlignment(Qt.AlignCenter)
        top_text.addWidget(central_text)
        top_text.addWidget(central_text_sec_line)
 




        main_layout = QVBoxLayout()
        main_layout.addStretch(1)
        main_layout.addLayout(top_text)

        self.setLayout(main_layout)
        

        self.setGeometry(300, 300, 300, 150)
        self.show()



app = QApplication(sys.argv)
window = MainMenu()
window.show()
app.exec()


