for i in range(1,6):
    for j in range(0,6-i):
        print("*",end=" ")
    print(" ")

for j in range(0,6):
    for i in range(0,j+1):
        print("*",end="")
    print(" ")


n=int(input("enter the no:"))
for i in range(0,n+1):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()    


n=int(input("enter the no:"))
for i in range(0,n+1):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end=" ")
    print()


