print("please enter two number")
n1 = int(input("first number :"))
n2 = int(input("second number :"))

def simple_calculater(n1,n2):
    print("choose the opration you need ?")
    print("1.addition")
    print("2.subration")
    print("3.multipilcation")
    print("4.division")
    option = int(input("enter the option :"))
    if option == 1:
        add = n1 + n2
        print("addition of ",n1," + ",n2," : Answer is ",add)
    if option == 2:
        sub = n1 - n2
        print("subration of ",n1," - ",n2," : Answer is ",sub)
    if option == 3:
        multi = n1 * n2
        print("mutipilcation of ",n1," * ",n2," : Answer is ",multi)
    if option == 4:
        div = n1 / n2
        print("division of ",n1," / ",n2," : Answer is ",div)
    print("Do you want contine ?")
    print("yes (or) no")
    repeat = input("")
    if repeat.lower() == "yes":
        print("Do you contine with same number or new number")
        print("1. same number")
        print("2. new number")
        req=int(input("enter the option :"))
        if req==1:
            return simple_calculater(n1,n2)
        if req==2:
            print("please enter two number")
            m1 = int(input("first number :"))
            m2 = int(input("second number :"))
            return simple_calculater(m1,m2)
simple_calculater(n1,n2)
    
    
