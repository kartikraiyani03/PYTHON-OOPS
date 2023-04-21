class car:
    brand = "Rplls Royce"
    color = "Coffee"

    # @staticmethod
    def info(self):
        print(self.brand)
        print(self.color)

c = car()
# c.info()
car.info(c)

