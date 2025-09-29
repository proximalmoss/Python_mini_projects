import random
choices=["Rock","Paper","Scissors"]
computer=random.choice(choices)
comp_score=0
player_score=0
while True:
    player = input("Rock, Paper or Scissors?").capitalize()
    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="Paper":
            print(f"computer chose {computer}")
            print("You loose!")
            comp_score+=1
        else:
            print("You win!")
            player_score+=1
    elif player=="Paper":
        if computer=="Scissors":
            print(f"computer chose {computer}")
            print("You loose!")
            comp_score+=1
        else:
            print("You win!")
            player_score+=1
    elif player=="Scissors":
        if computer=="Rock":
            print(f"computer chose {computer}")
            print("You loose!")
            comp_score+=1
        else:
            print("You win!")
            player_score+=1
    elif player=="End":
        print("Final scores")
        print (f"computer:{comp_score}")
        print(f"player:{player_score}")
        break