import math
print(math.gcd(30,24,18,12))



##################### no build-in function ###########################
print()

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print(gcd(num1,num2))
