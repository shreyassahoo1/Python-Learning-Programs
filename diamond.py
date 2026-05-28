n = 8

for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        if k==0 or k==2*i or i==n-1: 
            print("*", end=" ")
        else:  
            print(" ", end=" ")

    print()

n=n-1

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    
    for k in range(2*(n-i)-1):
        if k==0 or k==2*(n-i-1): 
            print("*", end=" ")
        else: 
            print(" ", end=" ")
    
    print()
