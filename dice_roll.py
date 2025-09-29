import random
min_val=1
max_val=6
roll_again="yes"
while roll_again=="yes" or roll_again=="y":
    print("rolling dice....")
    print("the values are: ")
    print (random.randint(min_val,max_val))
    print(random.randint(min_val, max_val))

    roll_again=input("do you want to roll dice again?")