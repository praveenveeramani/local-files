class phone():
    def __init__(self,modle):#--------------instance method--------------#
        self.modle=modle
        self.price="avg price;25000"
    def setprice(self,price):
        self.price=price
        print("price updated")
    def display(self):
        print("modle name;",self.modle)
        print("price is;",self.price)
    @classmethod#---------------------------class method-----------------#
    def newversion(cls):
        cls.new="latest version is upcoming"
        print(cls.new)
    @staticmethod#--------------------------static method----------------#
    def date():
        print("update coming tommorow ")
mob=phone("iqz7")
mob.setprice(31000)
mob.display()
phone.newversion()# use(class or object)with the call func
phone.date()#...... use(class or object)with the call func
        
