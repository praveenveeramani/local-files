########################### public ########################

class stratup():
    def __init__(self):
        self.cname="prvn"
    def changename(self,cname):
        self.cname=cname
    def dis(self):
        print("company name;",self.cname)
s=stratup()
s.dis()
s.changename("praveen")
s.dis()
print()#for space
############################ protecter ####################
class stratup():
    def __init__(self):
        self._cname="google"
    def changename(self,_cname):
        self._cname=_cname
    def dis(self):
        print("company name;",self._cname)
s=stratup()
s.dis()
s.changename("prvn")
s.dis()

print()#for space

########################### private ########################

class stratup():
    def __init__(self):
        self.__cname="google"
    def changename(self,__cname):
        self.__cname=__cname
    def dis(self):
        print("company name;",self.__cname)
s=stratup()
s.dis()
s.changename("prvn")
s.dis()

print()#for space

        
        
