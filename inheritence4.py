# Multilevel Inheritence
# Super Works In Methods And Constructor In Python
# Super Works In Constructor In JAVA

class Processor:
    processor = "11th Gen"
    
    def __init__(self):
        print("Processor Counstructor")
        
        
    def ProInfo(self):
        print(f"Processor is {self.processor}")

class RAM(Processor):
    ram = "8 GB LPDDR"
    
    def __init__(self):
        super().__init__()
        print("RAM Counstructor")
        

    def RamInfo(self):
        print(f"RAM is {self.ram}")

class Specification(RAM):
    
    def __init__(self):
        super().__init__()
        print("Specification Counstructor")
        

    
    def SpeInfo(self):
        print("All Specifications")
        
    def RamInfo(self):
        super().RamInfo()
        print("RAM is 4 GM LPDDR")

    def ProInfo(self):
        super().ProInfo()
        print("Processor is Qualcomm Snapdragon 665")
        

print("\n")
s = Specification()
print("")
r = RAM()
print("")
p = Processor()

print("")
print("----------------------------")
print("")

s.RamInfo()
print("")
s.ProInfo()

print("\n")

