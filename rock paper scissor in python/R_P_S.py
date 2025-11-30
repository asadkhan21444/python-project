"""
WORKFLOW 
1 - input user (rock, paper, scissors)
2 - computer random choice (computer  choice random not conditional)
3 - print results(who is winner)

---------logic-------------

A - Rock
Rock - Rock = tie
Rock - Paper = Paper wins
Rock - Scissors = Rock win

B - Paper
Paper - Paper = tie
Paper - Rock = Paper wins
Paper - Scissors = Scissors wins

C -Scissors
Scissors - Scissors = tie
Scissors - Rock = Rock wins
Scissors - Paper = Scissors wins
"""

import random 

items_list =["Rock", "Paper", "Scissors"]
user_choice = input("Enter your choice (Rock, Paper, Scissors):")
computer_choice = random.choice(items_list)
print(f" User choice is = {user_choice}, Computer choice is = {computer_choice}")
if user_choice == computer_choice:
    print("It,s a tie")
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper wins")
    else:
        print("Rock wins")
elif user_choice == "Paper":
    if computer_choice == "Scissors":
        print("Scissors wins")
    else:
        print("Paper wins")

elif user_choice == "Scissors":
    if computer_choice == "Rock":
        print("Rock wins")
    else:
        print("Scissors wins")

else:
    print("Invalid input, please choose Rock, Paper, Or Scissors")


        