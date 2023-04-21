class Student:
    name = "Alpha"
    CGPA = 9.23
    University = "GTU"
    
    # It can Change Instance Name
    def changeName(self,name):
        self.name = name
    
    # It can Change Class name 
    @classmethod
    def ChangeName(cls,name):
        cls.name = name
        

s = Student()
print("Class Name : "+Student.name)
print("Name : "+s.name)    
print("CGPA : ",s.CGPA)    
print("University : "+s.University)  
print("")
s.ChangeName("Beta")  
print("Class Name : "+Student.name)
print("Name : "+s.name)    
print("CGPA : ",s.CGPA)    
print("University : "+s.University)    
    