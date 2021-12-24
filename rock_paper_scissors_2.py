import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import sys
import random


computer_wins = 0
player_wins = 0

wins_player_list = ["Good job, solider!", 
                    "Keep going, soldier! The world is counting on you!"
                    ]
wins_computer_list = ["Try harder, soldier!",
                      "Bad luck, private!",
                      "What are you doing? Shoot the metal heads now!!!"
                      ]


class App:
    root = Tk()
    root.title("Game of Rock, Paper, Scissors.")
    root.iconbitmap(r"Rock-Paper-Scissors\images\controller.png")
    root.geometry("620x500")


    def rockButton_command():
        global computer_wins 
        global player_wins 
        player_choice = "rock"
        possible_actions = ['rock', 'paper', 'scissors']
        computer_action = random.choice(possible_actions)
        win_player_message = random.choice(wins_player_list)
        win_computer_message = random.choice(wins_computer_list)
        if computer_action == "rock":
            print('Tie!')         
        elif computer_action == "paper":
            computer_wins += 1
            result_label.config(text = f"Player wins: {player_wins}\nComputer wins: {computer_wins}")
            last_game_label.config(text = win_computer_message)
            print(f"Computer wins! {computer_wins}")
        elif computer_action == "scissors":
            player_wins +=1
            result_label.config(text = f"Player wins: {player_wins}\nComputer wins: {computer_wins}")
            last_game_label.config(text = win_player_message)
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
    
    
    exit_btn = PhotoImage(file = r"Rock-Paper-Scissors\images\exit.png")
    exit_img_label = Label(image = exit_btn)
    exit_button = Button(root, image=exit_btn, command = sys.exit, borderwidth = 0)
    exit_button.pack(pady=20)
    exit_button.place(x = 530, y = 450, width = 100, height = 50)
    my_label = Label(root, text = '')
    

    top_label = PhotoImage(file = r"Rock-Paper-Scissors\images\videogame.png")
    top_img_label = Label(image = top_label)
    top_img_label.pack()
    top_img_label.place(x = 80, y = 60, width = 500, height = 80)
    
    
    rock_btn = PhotoImage(file = r"Rock-Paper-Scissors\images\stone.png")
    rock_btn_label = Label(image = rock_btn)
    rock_button = Button(root, image = rock_btn, command = rockButton_command, borderwidth = 0, text = "Hit him with a rock!")
    rock_button.place(x = 20, y = 200)
    
    
    paper_btn = PhotoImage(file = r"Rock-Paper-Scissors\images\toilet-paper.png")
    paper_btn_label = Label(image = paper_btn)
    paper_button = Button(root, image = paper_btn, command = paperButton_command, borderwidth = 0)
    paper_button.place(x = 220, y = 200)
    
    scissors_btn = PhotoImage(file = r"Rock-Paper-Scissors\images\scissors.png")
    scissors_btn_label = Label(image = scissors_btn)
    scissors_button = Button(root, image = scissors_btn, command = scissorsButton_command, borderwidth = 0)
    scissors_button.place(x = 420, y = 200)

    global last_game_label
    last_game_label = Label(root,
                            font = ("Bahnschrift 13"),
                            text = "Prepare for battle, soldier!",
                            padx = 0)
    last_game_label.pack()
    last_game_label.place(x = 220, y = 380)
    
    global result_label
    result_label = Label(root, 
                         text = f"Player wins: {player_wins}\nComputer wins: {computer_wins}",  
                         font = ("Verdana 10 bold"), 
                         justify = LEFT, 
                         padx = 0, pady = 0)
    result_label.pack()
    result_label.place(x = 50, y = 450)
    
mainloop()