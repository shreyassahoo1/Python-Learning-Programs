# n = 8

# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end=" ")
    
#     for k in range(2*i+1):
#         if k==0 or k==2*i or i==n-1:  
#             print("*", end=" ")
#         else: 
#             print(" ", end=" ")
    
#     print()

n = 8

i=0
while i < n:
    j=0
    while j < n-i-1:
        print(" ", end=" ")
        j+=1

    k=0
    while k < (2*i+1):
        if k==0 or k==2*i or i==n-1:  
            print("*", end=" ")
        else: 
            print(" ", end=" ")
        k+=1
    print()
    i+=1