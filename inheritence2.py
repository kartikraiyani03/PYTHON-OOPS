# Multiple Inheritence

class RAM:
    ram = "4 GB LPDDR4"
    
    def RAMinfo(self):
        print(f"The RAM is {self.ram}")
    
class ROM:
     rom = "64 GB"
     
     def ROMinfo(self):
         print(f"The Size of ROM is {self.rom}")
         
class Android(RAM,ROM):
    
    android = "RMX1925"
    
    def specifications(self):
        print(f"Model Number is {self.android}")
        print(f"The Size of ROM is {self.rom}")
        print(f"The RAM is {self.ram}")


        
a = Android()
# a.RAMinfo()
# a.ROMinfo()
a.specifications()