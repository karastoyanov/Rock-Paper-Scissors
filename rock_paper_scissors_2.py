import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from PIL import ImageTk
import sys
import random


computer_wins = 0
player_wins = 0



class App:
    root = Tk()
    root.title("Game of Rock, Paper, Scissors.")
    root.iconbitmap("F:\Python_Projects\Personal Projects\Rock,Paper,Scissors\Rock-Paper-Scissors\controller.png")
    root.geometry("620x500")

    
    

    def rockButton_command():
        global computer_wins 
        global player_wins 
        player_choice = "rock"
        possible_actions = ['rock', 'paper', 'scissors']
        computer_action = random.choice(possible_actions)
        if computer_action == "rock":
            print('Tie!')         
        elif computer_action == "paper":
            computer_wins += 1
            result_label.config(text = f"Player wins: {player_wins}\nComputer wins: {computer_wins}")
            print(f"Computer wins! {computer_wins}")
        elif computer_action == "scissors":
            player_wins +=1
            result_label.config(text = f"Player wins: {player_wins}\nComputer wins: {computer_wins}")
            print(f"Player wins! {player_wins}")         
        return App
    
    
    def paperButton_command():
        global computer_wins 
        global player_wins
        player_choice = 'paper'
        possible_actions = ['rock', 'paper', 'scissors']
        computer_action = random.choice(possible_actions)
        if computer_action == "rock":
            player_wins +=1
            result_label.config(text = f"Player wins: {player_wins}\nComputer wins: {computer_wins}")
            print(f"Player wins! {player_wins}")
        elif computer_action == "paper":
            print("Tie!")
        elif computer_action == "scissors":
            computer_wins +=1
            result_label.config(text = f"Player wins: {player_wins}\nComputer wins: {computer_wins}")
            print(f"Computer wins! {computer_wins}")
        return App
    
    
    def scissorsButton_command():
        global computer_wins 
        global player_wins
        player_choice = 'paper'
        possible_actions = ['rock', 'paper', 'scissors']
        computer_action = random.choice(possible_actions)
        if computer_action == "rock":
            player_wins +=1
            result_label.config(text = f"Player wins: {player_wins}\nComputer wins: {computer_wins}")
            print(f"Player wins! {player_wins}")
        elif computer_action == "paper":
            print("Tie")
        elif computer_action == "scissors":
            computer_wins += 1
            result_label.config(text = f"Player wins: {player_wins}\nComputer wins: {computer_wins}")
            print(f"Computer wins! {computer_wins}")
        return App
    
    
    

    
    
    exit_btn = PhotoImage(file = "F:\Python_Projects\Personal Projects\Rock,Paper,Scissors\Rock-Paper-Scissors\exit.png")
    exit_img_label = Label(image = exit_btn)
    exit_button = Button(root, image=exit_btn, command = sys.exit, borderwidth = 0)
    exit_button.pack(pady=20)
    exit_button.place(x = 530, y = 450, width = 100, height = 50)
    my_label = Label(root, text = '')
    my_label.pack()

    top_label = PhotoImage(file = "F:\Python_Projects\Personal Projects\Rock,Paper,Scissors\Rock-Paper-Scissors\/videogame.png")
    top_img_label = Label(image = top_label)
    top_img_label.place(x = 80, y = 60, width = 500, height = 80)
    
    
    rock_btn = PhotoImage(file = "F:\Python_Projects\Personal Projects\Rock,Paper,Scissors\Rock-Paper-Scissors\stone.png")
    rock_btn_label = Label(image = rock_btn)
    rock_button = Button(root, image = rock_btn, command = rockButton_command, borderwidth = 0, text = "Hit him with a rock!")
    rock_button.place(x = 20, y = 200)
    
    
    paper_btn = PhotoImage(file = "F:\Python_Projects\Personal Projects\Rock,Paper,Scissors\Rock-Paper-Scissors\/toilet-paper.png")
    paper_btn_label = Label(image = paper_btn)
    paper_button = Button(root, image = paper_btn, command = paperButton_command, borderwidth = 0)
    paper_button.place(x = 220, y = 200)
    
    scissors_btn = PhotoImage(file = "F:\Python_Projects\Personal Projects\Rock,Paper,Scissors\Rock-Paper-Scissors\scissors.png")
    scissors_btn_label = Label(image = scissors_btn)
    scissors_button = Button(root, image = scissors_btn, command = scissorsButton_command, borderwidth = 0)
    scissors_button.place(x = 420, y = 200)

    last_game_label = Label(root,
                            font = ("Bahnschrift 13"),
                            justify = CENTER,
                            text = "LAST GAME MESSAGE",
                            padx = 0)
    last_game_label.place(x = 220, y = 380)
    
    global result_label
    result_label = Label(root, 
                         text = f"Player wins: {player_wins}\nComputer wins: {computer_wins}",  
                         font = ("Verdana 10 bold"), 
                         justify = LEFT, 
                         padx = 20)
    result_label.pack()

    
mainloop()