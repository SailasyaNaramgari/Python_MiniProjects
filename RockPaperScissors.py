import random

options = ("rock" , "paper" , "scissors")
playing = True

while playing :

    player = None
    computer = random.choice(options)

    while player not in options :
        player = input("Enter a choice (rock,paper,scissors) :")

    print(f"Player choice : {player}")
    print(f"Computer choice : {computer}")

    if player == computer :
        print("That's a TIE")
    elif player == "rock" and computer == "scissors" :
        print("Cogratulations! YOU WIN")
    elif player == "paper" and computer == "rock" :
        print("Cogratulations! YOU WIN")
    elif player == "scissors" and computer == "paper" :
        print("Cogratulations! YOU WIN")
    else:
        print("Sorry! YOU LOST")


    #to escape the while loop

    play_again = input("Do you want to play again? (yes/no) :").lower()
    if not play_again == "yes":
        playing = False

print("Thanks for playing!")



