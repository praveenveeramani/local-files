####################### 123 SERIES ########################### 
for i in range(1,4):
    print()
    for j in range(1,i+1):
        print(j, end = "")

print()

for i in range(1,6):
    print()
    for j in range(i,6):
        print(j, end = "")

#####################  STAR SERIES ############################
print()

for i in range(1,6):
    print()
    for j in range(1,i+1):
        print("*",end="")

#####################  HOLLOW STAR SERIES ############################
print()

n=int(input("enter the no of rows you want:"))
for row in range(n):
    for col in range(n):
        if col==0 or row==(n-1) or row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()
