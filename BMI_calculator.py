height=float(input("Enter you height in cm: "))
weight=float(input("Enter you weight in Kg: "))
height=height/100
BMI=weight/(height*height)
print(f"Your Body Mass Index is: {BMI}")
if (BMI>0):
    if(BMI<=16):
        print("you are severely underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("you are healthy")
    elif(BMI<=30):
        print("you are overweight")
    else:
        print("you are severely overweight")
else:("enter valid details")