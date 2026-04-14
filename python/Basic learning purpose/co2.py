class teacher():
    def __init__(self,name,experiance):
        self.name=name
        self.experiance=experiance
    def display(self):
        print("name:",self.name)
        print("experiance:",self.experiance,"years")
t1=teacher("yalni","4")
t2=teacher("baby","5")
t1.display()
t2.display()
