lowest=int(input("enter the low num:"))
highest=int(input("ener the high num:"))
for num in range(lowest,highest+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)

####################################
                
n=21
for i in range(2,n):
    if (n%i==0):
        break
    else:
        print("not prime")
else:
    print("prime")
