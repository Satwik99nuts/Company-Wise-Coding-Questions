class Calc():
    def add(self, a,b,c=0):
        return a+b+c
calc = Calc()
print(calc.add(1,2,3))
print(calc.add(1,2))