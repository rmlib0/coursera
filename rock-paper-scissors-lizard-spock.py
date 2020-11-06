# Rock-paper-scissors-lizard-Spock
# http://www.codeskulptor.org/#user47_YOLUvuCncZXQyji.py
import random


def number_to_name(number):
    return {0: "rock",
            1: "Spock",
            2: "paper",
            3: "lizard",
            4: "scissors"}[number]


def name_to_number(name):
    return {"rock": 0,
            "Spock": 1,
            "paper": 2,
            "lizard": 3,
            "scissors": 4}[name]


def game_winner(player_choice, computer_choice, who):
    print(f"Player chooses: {number_to_name(player_choice)}")
    print(f"Computer chooses: {number_to_name(computer_choice)}")
    if who == "player":
        print(f"Player wins!")
    elif who == "computer":
        print(f"Computer wins!")
    else:
        print(f"No winners. Draw!")


def rpsls(_player_choice):
    computer_choice = random.randint(0, 4)
    player_choice = name_to_number(_player_choice)

    difference = (computer_choice - player_choice) % 5

    if difference == 1 or difference == 2:
        game_winner(player_choice, computer_choice, "computer")
    elif difference == 4 or difference == 3:
        game_winner(player_choice, computer_choice, "player")
    elif difference == 0:
        game_winner(player_choice, computer_choice, "draw")


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
