# single Level Ingheritence

class University:
    univeristy = "GTU"
    
    def info(self):
        print(f"University is {self.univeristy}")
        
class Student(University):
    Student = "Regular"
    univeristy = "DU"  
      
    def data(self):
        print(f"Student is {self.Student} Student")
        print(f"University is {self.univeristy}")


u = University()
s = Student()
u.info()
print("************")
s.data()