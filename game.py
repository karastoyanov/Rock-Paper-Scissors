#!/usr/bin/python3
import random

def game_round(player_choice):
    possible_ai_choice = ["rock", "paper", "scissors"]
    ai_choice = random.choice(possible_ai_choice)

    if player_choice == "rock":
        if ai_choice == "rock":
            print("Tie!")
        elif ai_choice == "paper":
            print("Computer wins!")
        elif ai_choice == "scissors":
            print("Player wins!")

    if player_choice == "paper":
        if ai_choice == "rock":
            print("Player wins!")
        elif ai_choice == "paper":
            print("Tie!")
        elif ai_choice == "scissors":
            print("Computer wins!")

    if player_choice == "scissors":
        if ai_choice == "rock":
            print("Computer wins!")
        elif ai_choice == "paper":
            print("Player wins!")
        elif ai_choice == "scissors":
            print("Tie!")
        

print(game_round("rock"))
