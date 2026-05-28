lt = [ 1, 2, 3, 5, 6, 7, 8 ]

for i in range(len(lt)):
    print(i, lt[i], sep=". ")

print("*" * 50)
for index, value in enumerate(lt, start=101):
    print(index, value, sep=".) ")

print("*" * 50)
i = 0
while i < len(lt):
    print(i, lt[i], sep=".) ")
    i += 1
