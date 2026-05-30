n = 8
i=0
while i < n:
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        if k==0 or k==2*i:
            print("*", end=" ")   
        else:
            print(" ",end=" ")
    print()

n=n-1

for i in range(n-1,-1,-1):
    for j in range(n-i-1+1):
        print(" ", end=" ")
    
    for k in range(2*i+1):
        if k==0 or k==2*i: 
            print("*", end=" ")   
        else:
            print(" ",end=" ")
    
    print()