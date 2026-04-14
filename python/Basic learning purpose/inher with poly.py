class stu():
    def __init__(self,name):
        self.name=name

class teach(stu):
    def __init__(self,grate,name):
        self.grate=grate
        super().__init__(name)
    def dis(self):
        print(self.name,self.grate)
t=teach("b","prvn")
t.dis()
