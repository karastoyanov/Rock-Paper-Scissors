#!/usr/bin/python3
import random
import game


player_wins_messages = [
        "Good job, soldier!",
        "Keep the good work, private!",
        "Keep fraging soldier!"
        ]

ai_wins_messages = [
        "Better luck next time!",
        "Common soldier, the fate of the humanity is in your hands!"
        ]

tie_messages = [
        "You get another chance, private!"
        ]


def return_message(player_result, ai_result):
    if player_result == True and ai_result == False:
        round_result = random.choice(player_wins_messages)
        print(round_result)
        #return random.choice(player_wins_messages)
    elif player_result == False and ai_result == True:
        round_result = random.choice(ai_wins_messages)
        print(round_result)
        #return random.choice(ai_wins_messages)
    elif player_result == False and ai_result == False:
        round_result = random.choice(tie_messages)
        print(round_result)
        #return random.choice(tie_messages)
    return round_result

