
class student():
    def __init__(self):
        self.name="praveen"
        self.rollno=4226
    def display(self):
        print("name:",self.name)
        print("rollno:",self.rollno)

class student1(student):
    def __init__(self):
        self.name="prvn"
        self.rollno=4227
    
s1=student1()
print(s1.name)
print(s1.rollno)
s1.display()
