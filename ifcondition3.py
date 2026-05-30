realnumber=50
num1=int(input("Guess the lucky number: "))
if num1>50:
    print("Your number is too high, try again!")
elif num1<50:
    print("Your number is too less, try again!")
else:
    print("Yay, you chose the correct number!")