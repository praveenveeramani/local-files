a=int(input("enter a;"))
b=int(input("enter b;"))
class calculater():
    def __init__(self,add,sub,multi,div):
        self.add=add
        self.sub=sub
        self.multi=multi
        self.div=div
    def display(self):
        print("add:",self.add)
        print("sub:",self.sub)
        print("multi:",self.multi)
        print("div:",self.div)
cal=calculater(a+b,a-b,a*b,a/b)
cal.display()#init la func mention parameter pannathevalilla



#program 2
a=int(input("enter a;"))
b=int(input("enter b;"))
class calculater():
    def display(self,a,b):
        print("add:",a+b)
        print("sub:",a-b)
        print("multi:",a*b)
        print("div:",a/b)
cal=calculater()
cal.display(a,b)# def func la mention parameter pannanum
