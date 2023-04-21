class student:
    def info(self):
        university = "GTU"
        print("Name :",self.name)
        print("CGPA :",self.cgpa)
        print("University :",university,"\n")
        

s1 = student()
s2 = student()
s3 = student()

s1.name = "Alpha"
s1.cgpa = 9.0

s2.name = "Beta"
s2.cgpa = 9.8


s3.name = "Gamma"
s3.cgpa = 9.7

s1.info()
s2.info()
s3.info()
                                        