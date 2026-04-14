##################### recursion ##########################
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter number:"))
reslut = fact(n)
print("factorial of",n,"is",reslut)

##################### for loop #############################
print()

result=1
for i in range(n,0,-1):
    result=result*i

print("factorial of",n,"is",result)
