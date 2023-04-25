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
                             QTableWidget,
                             QTableWidgetItem) 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import db_connect

def start_app():
    global win
    win = PlayersRanklist()
    win.show()


class PlayersRanklist(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A game of Rock-Paper-Scissors - Players Ranklist")
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

        # Table Widget
        ranklist_table = QTableWidget(self)
        ranklist_table.setRowCount(4)
        ranklist_table.setColumnCount(4)
        #ranklist_table.setItem(0, 0 , QTableWidgetItem("Cell 1, 1"))
        ranklist_table.move(0, 0)
        

        header = ranklist_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        
        horizontal_layout.setStretch(0, 0)
        horizontal_layout.addWidget(ranklist_table)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(horizontal_layout)
        self.setLayout(main_layout)
        self.show()



def init_window():
    app = QApplication(sys.argv)
    window.start_app()
    app.exec_()


app = QApplication(sys.argv)
window = start_app()
app.exec_()

