#Checking leap year
year=int(input("Enter the year: "))
##approach1
# if year%100==0:
#     if year%400==0:
#         print("This year is a leap year")
#     else:   
#         print("This year is not a leap year")
# elif year%4==0:
#     print("This year is a leap year")
# else:
#     print("This year is not a leap year")

##approach2
# if (year % 100== 0) and (year % 400== 0):
#     print("This year is a leap year")
# elif (year % 4== 0) and (year % 100!= 0):
#     print("This year is a leap year")
# else:
#     print("This year is not a leap year")

##approach3
if (year % 400== 0) or ((year % 4== 0) and (year % 100!= 0)):
    print("This year is a leap year")
else:
    print("This year is not a leap year")