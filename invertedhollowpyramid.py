# n = 8

# for i in range(n):
#     for j in range(i):
#         print(" ", end=" ")
    
#     for k in range(n-i):
#         if k==0 or k==n-i-1 or i==0:
#             print("*", end=" ")
#         else:
#             print(" ", end= " ")
    
#     print()

n = 8
i=0 
while i < n:
    j=0
    if j < i:
        print(" ", end="")
    j+=1
    k=0
    while k < (2*(n-i)-1):
        if k==0 or k==2*(n-i)-2 or i==0: 
            print("*", end="")
        else:
            print(" ", end="")
        k+=1
    
    print()
    i+=1