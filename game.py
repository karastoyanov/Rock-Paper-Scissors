#!/usr/bin/python3
import random
import game_message


def game_round(player_choice):
        possible_ai_choice = ["rock", "paper", "scissors"]
        ai_choice = random.choice(possible_ai_choice)
        player_wins = False
        ai_wins = False
        result = ""

        if player_choice == "rock":
            if ai_choice == "rock":
                print("Tie!")
                player_wins, ai_wins = False, False
            elif ai_choice == "paper":
                print("Computer wins!")
                player_wins, ai_wins = False, True
                # main.MainMenu.AI_POINTS += 1
            elif ai_choice == "scissors":
                print("Player wins!")
                player_wins, ai_wins = True, False
                # main.MainMenu.PLAYER_POINTS += 1

        if player_choice == "paper":
            if ai_choice == "rock":
                print("Player wins!")
                player_wins, ai_wins = True, False
                # main.MainMenu.PLAYER_POINTS += 1
            elif ai_choice == "paper":
                print("Tie!")
                player_wins, ai_wins = False, False
            elif ai_choice == "scissors":
                print("Computer wins!")
                player_wins, ai_wins = False, True
                # main.MainMenu.AI_POINTS += 1

        if player_choice == "scissors":
            if ai_choice == "rock":
                print("Computer wins!")
                player_wins, ai_wins = False, True
                # main.MainMenu.AI_POINTS += 1
            elif ai_choice == "paper":
                print("Player wins!")
                player_wins, ai_wins = True, False
                # main.MainMenu.PLAYER_POINTS += 1
            elif ai_choice == "scissors":
                print("Tie!")
                player_wins, ai_wins = False, False
        # QApplication.processEvents()
    
        if player_wins == True and ai_wins == False:
            return 1
        elif player_wins == False and ai_wins == True:
            return 2
        elif player_wins == False and ai_wins == False:
            return 3



        
