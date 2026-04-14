num=int(input("enter the how many number you want fibonacci:"))
first=0
second=1
for i in range(num):
    print(first, end=" ") #---------> only print the frist and calculate second; after sec would fix that frist
    temp=first
    first=second
    second=temp+first
