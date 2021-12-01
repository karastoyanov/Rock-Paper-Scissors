import random

user_action = input("Player choice: rock, paper, scissors:\n")
possible_actions = ['rock', 'paper', 'scissor']
computer_action = random.choice(possible_actions)
player_wins = 0
computer_wins = 0


print(f"\nYou chose {user_action}.\nComputer chose {computer_action}.\n")
game_on = True

while game_on:
    if user_action == computer_action:
        print(f"Both player selected {user_action}. It's a tie!\n")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! Player wins!\n")
            player_wins += 1
        elif computer_action == "paper":
            print("Paper covers rock! Computer wins!\n")
            computer_wins += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! Player wins!\n")
            player_wins += 1
        elif computer_action == "paper":
            print("Scissors cuts paper! Computer wins!\n")
            computer_wins += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! Player wins!\n")
            player_wins += 1
        elif computer_action == "rock":
            print("Rock smashes scissors! Computer wins!\n")
            computer_wins += 1
    elif user_action == "X":
        print(f"Final result: Player points: {player_wins}\nComputer points: {computer_wins}")
        break        
    user_action = input("\nChose one: rock, paper, scissors or Press 'X' to exit the game.\n")