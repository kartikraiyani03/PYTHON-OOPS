# Multilevel Inheritence

class Processor:
    processor = "11th Gen"
    
    def ProInfo(self):
        print(f"Processor is {self.processor}")
        
class RAM(Processor):
    ram = "8 GB LPDDR"
    
    def RamInfo(self):
        print(f"RAM is {self.ram}")

class Specification(RAM):
    
    def SpeInfo(self):
        print("All Specifications")


s = Specification()
s.SpeInfo()
s.RamInfo()
s.ProInfo()
