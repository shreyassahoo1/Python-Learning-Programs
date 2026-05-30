n=12

for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i==n-1:
            print("*", end=" ")
        elif j==n//2 or i==n//2: 
             print("*", end=" ")
        elif n%2==0 and j==(n//2)-1 or i==(n//2)-1:
             print("*", end=" ")
        else:
            print(" ", end=" ")
    print()