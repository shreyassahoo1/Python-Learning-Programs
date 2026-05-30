i=1
while i <= 20:
    if i % 18 == 0:
        print("here your 8 seconds are finished")
        break
    if i % 5 == 0:
        print("the number is divisible by 5")
        i+=1
        continue
    print(i)
    i+=1
