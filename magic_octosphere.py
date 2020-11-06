# THE MYSTICAL OCTOSPHERE! by Andrea Crain
# http://www.codeskulptor.org/iipp-practice-experimental/#user47_H9cClROSZa60fnQ.py

import random


def number_to_fortune(number):
    return {
        0: "Yes, for sure!",
        1: "Probably yes.",
        2: "Seems like yes...",
        3: "Definitely not!",
        4: "Probably not.",
        5: "I really doubt it...",
        6: "Not sure, check back later!",
        7: "I really can't tell"
    }[number]


def mystical_octosphere(question):
    print(question)
    print("You shake the mystical otosphere.")
    answer_number = random.randrange(0, 8)
    answer_fortune = number_to_fortune(answer_number)
    print("The mystical octosphere says..." + answer_fortune)
    print


mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")
