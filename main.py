from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import db_connect
import login, main_menu, register

#admin_client = db_connect.database_connect()
#player_client = db_connect.user_connect(register.user_name_text_field.text(), register.user_name_text_field.text())


login.LoginMenu()
