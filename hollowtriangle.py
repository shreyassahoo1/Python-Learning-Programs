n = 10
i=0
while i < n:
    j=0
    while j < i + 1:
        if j==0 or i==n-1 or j==i:
            print("*", end=" ")
            j=+1
        else:
            print(" ", end=" ")
            
            j=+1
    print()
    i+=1
