n = 6

i=0 
while i < n:
    j=0
    if j < (n-i-1):
        print(" ", end=" ")
    j+=1

    k=0
        
    while k < i+1:
        print("*", end=" ")
        k+=1
    
    print()
    i+=1