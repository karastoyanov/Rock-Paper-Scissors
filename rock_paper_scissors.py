import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import sys
import random

computer_wins = 0
player_wins = 0

class App:
    def __init__(self, root):
        #setting title
        root.title("Game of Rock, Paper, Scissors")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        
        exitButton=tk.Button(root)
        exitButton["image"] = "F:\Python_Projects\Personal Projects\Rock,Paper,Scissors\Rock-Paper-Scissors\exit.jpg"
        exitButton["activebackground"] = "#ff5722"
        exitButton["activeforeground"] = "#000000"
        exitButton["bg"] = "red"
        ft = tkFont.Font(family='Times',size=10)
        exitButton["font"] = ft
        exitButton["fg"] = "#000000"
        exitButton["justify"] = "center"
        exitButton["text"] = "Quit Game"
        exitButton.place(x=500,y=450,width=70,height=25)
        exitButton["command"] = self.exitButton_command
        

        topLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        topLabel["font"] = ft
        topLabel["fg"] = "#333333"
        topLabel["justify"] = "center"
        topLabel["text"] = "Compete against the machines and do not allow them to take over the world!\nThe humanity is counting on you soldier!"
        topLabel.place(x=40,y=30,width=524,height=119)

        rockButton=tk.Button(root)
        rockButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        rockButton["font"] = ft
        rockButton["fg"] = "#000000"
        rockButton["justify"] = "center"
        rockButton["text"] = "Try hit them with a rock!"
        rockButton.place(x=40,y=160,width=142,height=128)
        rockButton["command"] = self.rockButton_command

        paperButton=tk.Button(root)
        paperButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        paperButton["font"] = ft
        paperButton["fg"] = "#000000"
        paperButton["justify"] = "center"
        paperButton["text"] = "Who said the pen is\nmightier than the sword?!"
        paperButton.place(x=230,y=160,width=143,height=127)
        paperButton["command"] = self.paperButton_command

        scissorsButton=tk.Button(root)
        scissorsButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        scissorsButton["font"] = ft
        scissorsButton["fg"] = "#000000"
        scissorsButton["justify"] = "center"
        scissorsButton["text"] = "Ok, time to\ncut some cabels."
        scissorsButton.place(x=420,y=160,width=140,height=126)
        scissorsButton["command"] = self.scissorsButton_command

        lastGameLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lastGameLabel["font"] = ft
        lastGameLabel["fg"] = "#333333"
        lastGameLabel["justify"] = "center"
        lastGameLabel["text"] = "Print the result"
        lastGameLabel.place(x=40,y=300,width=519,height=52)

        lastGameMessage=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lastGameMessage["font"] = ft
        lastGameMessage["fg"] = "#333333"
        lastGameMessage["justify"] = "center"
        lastGameMessage["text"] = "Here the player will get a message as result from the last round."
        lastGameMessage.place(x=100,y=360,width=400,height=30)

        currentResult=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        currentResult["font"] = ft
        currentResult["bg"] = 'white'
        currentResult["fg"] = "#333333"
        currentResult["justify"] = "center"
        currentResult["text"] = "Current result"
        currentResult.place(x=10,y=390,width=150,height=83)

    def exitButton_command(self):
        return sys.exit()

    def rockButton_command(self):
        global computer_wins 
        global player_wins 
        player_choice = "rock"
        possible_actions = ['rock', 'paper', 'scissors']
        computer_action = random.choice(possible_actions)
        if computer_action == "rock":
            print('Tie!')         
        elif computer_action == "paper":
            computer_wins += 1
            print(f"Computer wins! {computer_wins}")
        elif computer_action == "scissors":
            player_wins +=1
            print(f"Player wins! {player_wins}")      
        return App

    def paperButton_command(self):
        global computer_wins 
        global player_wins
        player_choice = 'paper'
        possible_actions = ['rock', 'paper', 'scissors']
        computer_action = random.choice(possible_actions)
        if computer_action == "rock":
            player_wins +=1
            print(f"Player wins! {player_wins}")
        elif computer_action == "paper":
            print("Tie!")
        elif computer_action == "scissors":
            computer_wins +=1
            print(f"Computer wins! {computer_wins}")
        return App

    def scissorsButton_command(self):
        global computer_wins 
        global player_wins
        player_choice = 'paper'
        possible_actions = ['rock', 'paper', 'scissors']
        computer_action = random.choice(possible_actions)
        if computer_action == "rock":
            player_wins +=1
            print(f"Player wins! {player_wins}")
        elif computer_action == "paper":
            print("Tie")
        elif computer_action == "scissors":
            computer_wins += 1
            print(f"Computer wins! {computer_wins}")
        return App


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
