tup1 = (20, "Hello", "Sky", 14, 33.5)
print("This is Tuple 1: ", tup1)

tup2 = (9, "Red", 25)
print ("This is Tuple 2: ", tup2)

tup1+=tup2

print("This is a combined tuple: ", tup1)

print(len(tup1))
print(len(tup2))
print(tup2[2])
print(tup1[6])

print(tup1)

del(tup2)

print(tup1[0:4])
print(tup1[1:6])
print(tup1[:4])
print(tup1[2:])

print("Thank you")