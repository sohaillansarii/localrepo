import random

options = ("rock", "paper","scissors")
running =  True

while running:
        
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock,paper,scissors):")

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player == computer:
        print("Its a Tie")

    elif player =="rock" and computer == "paper":
        print("COMPUTER WINS")
    elif player == "paper" and computer =="scissors":
        print("COMPUTER WINS")
    elif player == "scissors" and computer == "rock":
        print("COMPUTER WINS")
    else:
        print("YOU WIN!!")

    if not input("Play Again?(y/n):").lower() == "y":
               running= False
    
print("THANKS FOR PLAYING")