class a():#<----------------------------
    def top():                          # 
        print("topper in 45%")          # single inheritances
                                        #
class b(a):#<---------------------------
    def avg():                          #
        print("avarege in 45%")         #
                                        #
class c():#<----------------------------# multiple inheritance
    def slow():                         #
        print("slow in 8%")             #
                                        #
class d(c,b):#<-------------------------
    def waste():
        print("waste in 2%")

sch=d
sch.waste()
sch.slow()
sch.avg()
sch.top()
############################[^ellamey irruntha athu hybrid inheritance]#######################################################

class school():#<-------------------------
    def __init__(self):                   #
        self.stu1="p"                     #
        self.stu2="a"                     #    school has common parameter call     
        self.stu3="p"                     #    class.
    def dis(self):                        #    so its "heriarical inheritance" 
        print("stu1;",self.stu1)          #
        print("stu2;",self.stu2)          #
        print("stu3;",self.stu3)          #
                                          #      
class stu1(school):#<---------------------
    def s1(self):                         #
        print("topper")                   #  declare stu2 and stu1 is  
                                          #  "multi level inheriance"      
class stu2(stu1,school):#<----------------
    def s2(self):                         #
        print("avarege")                  #
                                          #        
class stu3(stu2,school):#<----------------
    def s3(self):
        print("slow learners")
        
s=stu3()
s.dis()
s.s1()
s.s2()
s.s3()

        
