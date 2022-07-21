# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:58:23 2022

@author: Administrator
"""

from random import randint

t = ["Rock", "Paper", "Scissors"]


computer = t[randint(0,2)]
computer = computer.lower()

while 1:
#set player to True
    player = input("Rock, Paper, Scissors?")
    player = player.lower()
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    computer = t[randint(0,2)]
    computer = computer.lower()
