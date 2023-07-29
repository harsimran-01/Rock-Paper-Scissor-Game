# Rock-Paper-Scissor-Game

import random
while True:
    def gameWinnner(comp, User):
        if comp == User:
            return None
        elif comp == "ROCK":
            if User == "SCISSOR":
                return False
            elif User == "PAPER":
                return True
        elif comp == "PAPER":
            if User == "ROCK":
                return False
            elif User == "SCISSOR":
                return True
        elif comp == "SCISSOR":
            if User == "PAPER":
                return False
            elif User == "ROCK":
                return True
                


    print("         ***** Welcome to ROCK-PAPER-SCISSOR Game*****  \n")
    randno = random.randint(1, 3)
    # print(randno)
    if randno == 1:
        comp = "ROCK"
    elif randno == 2:
        comp = "SCISSOR"
    elif randno == 3:
        comp = "PAPER"

    User = input("What do you want to Choose (Rock, Scissor, Paper): ").upper()
    print(f"\nComputer Has choosed {comp}.")
    print(f"You have Choosed {User}.")
    a = gameWinnner(comp, User)

    if a == None:
        print("\nIt's a Tie..")
    elif a == True:
        print("\nYou have Won the Game.")
    else:
        print("\nYou have Loose The Game.")  

    ask = input("Do you want to Continue Playimg: ") 
    if ask == "no":
        print("Game is Closed ...")
        break



