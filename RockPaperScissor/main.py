
from random import randint

play_options = ["rock","paper","scissor"]

while True:

    computer_play = play_options[randint(0,2)]
    user_play = input("Rock,Paper,Scissor? ").lower()

    if computer_play == user_play:
        print("It's Tie")

    elif user_play == "rock":
        if computer_play =="paper":
            print("you lose!",computer_play,"beats",user_play)
        else:
            print("you win!", user_play,"beats",computer_play)

    elif user_play == "paper":
        if computer_play == "scissor":
            print("you lose!", computer_play, "beats", user_play)
        else:
            print("you win!", user_play, "beats", computer_play)

    elif user_play == "scissor":
        if computer_play == "rock":
            print("you lose!", computer_play, "beats", user_play)
        else:
            print("you win!", user_play, "beats", computer_play)
    else:
        print("Not a valid play options, Try again!")