lt = [ 1, 2, 3, 5, 6, 7, 8 ]

lt1 = []
print(lt1)
for i in lt:
    if i%2:
        temp = i ** 3
    else:
        temp = i ** 2
    lt1.append(temp)
    print(lt1)
print(lt)
print(lt1)

print("*" * 60)
lt2 = [i**3 if i%2 else i ** 2 for i in lt]
print(lt2)

print("*" * 60)
lt1 = []
print(lt1)
for i in lt:
    if i%2:
        lt1.append(i ** 3)
    else:
        lt1.append(i ** 2)
    print(lt1)
print(lt)
print(lt1)