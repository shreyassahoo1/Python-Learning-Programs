n = 7

#top
for i in range(1, n):
    for j in range(1, i):
        print(' ', end='')
    for k in range(i, n):
        print("* ", end='')
    print()



#bottom
for i in range(n-1, 0, -1):
    for j in range(1, i):
        print(' ', end='')
    for k in range(i, n):
        print("* ", end='')
    print()