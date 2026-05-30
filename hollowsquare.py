n = 10

i=0
while i < n:
    j=0
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    
    print()
    i+=1