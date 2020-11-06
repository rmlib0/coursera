# Rock-paper-scissors-lizard-Spock
# http://www.codeskulptor.org/#user47_KLRTDWmOaE0uJEM.py
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
    print(f"Player chooses: {player_choice}")
    print(f"Computer chooses: {computer_choice}")
    if who == "player":
        print(f"Player wins!")
    elif who == "computer":
        print(f"Computer wins!")
    else:
        print(f"No winners. Draw!")


def rpsls(_player_choice):
    computer_choice = number_to_name(random.randrange(0, 5, 1))
    player_choice = _player_choice

    if computer_choice == player_choice:
        game_winner(player_choice, computer_choice, "draw")
    elif player_choice == "rock":
        if computer_choice == "lizard" or computer_choice == "scissors":
            game_winner(player_choice, computer_choice, "player")
        else:
            game_winner(player_choice, computer_choice, "computer")
    elif player_choice == "Spock":
        if computer_choice == "rock" or computer_choice == "scissors":
            game_winner(player_choice, computer_choice, "player")
        else:
            game_winner(player_choice, computer_choice, "computer")
    elif player_choice == "paper":
        if computer_choice == "rock" or computer_choice == "Spock":
            game_winner(player_choice, computer_choice, "player")
        else:
            game_winner(player_choice, computer_choice, "computer")
    elif player_choice == "lizard":
        if computer_choice == "paper" or computer_choice == "Spock":
            game_winner(player_choice, computer_choice, "player")
        else:
            game_winner(player_choice, computer_choice, "computer")
    elif player_choice == "scissors":
        if computer_choice == "paper" or computer_choice == "lizard":
            game_winner(player_choice, computer_choice, "player")
        else:
            game_winner(player_choice, computer_choice, "computer")
    else:
        print("no way!")
