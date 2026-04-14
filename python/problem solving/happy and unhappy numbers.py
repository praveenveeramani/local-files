def squarefun(n):
    result=0
    while n>0:
        rem=n%10
        result=result+rem*rem
        n=n//10
    return result

n=int(input("enter the numbers:"))
result=n
while result!=1 and result!=4:
    result=squarefun(result)
    print(result) #---------->refrence
if result==1:
    print("happy number")
else:
    print("unhappy numbers")
