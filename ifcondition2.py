#Exam Grades Calculator
print("Check your grades here!")
grades=float(input("Enter your percentage here: "))
if grades>=90:
    print("Excellent, your grade is an A")
elif grades>=70:
    print("Decent, your grade is a B")
elif grades>=55:
    print("You must work hard, your grade is a C")
else:
    print("Unfortunately, you have failed. Your grade is an F")

