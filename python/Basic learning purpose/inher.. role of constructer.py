class a():
    def __init__(self):
        print("A")
class b():
    def display(self):
        print(" class b")
obj=b()
print()
#############################object "b" call onevarala

class a():
    def __init__(self):
        print("A")
class b(a):
    def display(self):
        print(" class b")
obj=b()
print()
############################# "b" la "a" inherit panna, "a" consecter call aakuthu

class a():
    def __init__(self):
        print("A")
class b(a):
    def __init__(self):
        print("B")
    def display(self):
        print(" class b")
obj=b()
print()
############################# "b" la consecter create pannitu call panna "b" consecter call aakuthu

class a():
    def __init__(self):
        print("A")
class b(a):
    def __init__(self):
        print("B")
class c(b,a):
    def __init__(self):
        super().__init__() #keyword " super().__init__() " use to call " 1st " parameter of b consecter
        print("C")
obj=c()
