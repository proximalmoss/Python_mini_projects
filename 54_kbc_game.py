questions=[["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],       
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4],
["which langauge was used to create facebook?" , "python", "French", "Javascript", "php", "None", 4]]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"question for Rs.{levels[i]}")
    print(f"{question[0]}")
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    reply=int(input("enter you answer(1-4) or press 0 to quit"))
    if (reply=="0"):
        money=levels[i-1]
        break
    if (reply==question[-1]):
        print(f"correct answer, you have won Rs. {levels[i]}")
        if (i==4):
            money=10000
        elif (i==9):
            money=320000
        elif (i==14):
            money=10000000
    else:
        print("wrong answer, you are out")
        break
print(f"you are taking home Rs. {money}")