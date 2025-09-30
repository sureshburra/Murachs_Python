class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def add(self, num2: int):
        return Complex(self.real + num2.real, self.img + num2.img)

    def __add__(self, num2):
        return Complex(self.real + num2.real, self.img + num2.img)

    def __sub__(self, num2):
        return Complex(self.real - num2.real, self.img - num2.img)


comp1 = Complex(1, 2)
comp1.showNumber()
comp2 = Complex(3, 4)
comp2.showNumber()
# comp3 = comp1.add(comp2)
comp3 = comp1 + comp2
comp3.showNumber()

comp3 = comp1 - comp2
comp3.showNumber()
