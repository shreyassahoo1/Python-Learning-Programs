n = 10

i=0 
while i < n:
    j=0
    while j < (n-i):
        print(" ", end=" ")
        j+=1
        
    k=0
    while k < n:
        print("*", end=" ")
        k+=1
    print()
    i+=1