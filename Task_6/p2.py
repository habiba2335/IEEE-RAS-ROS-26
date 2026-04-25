class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print("Add:", calc.add(5, 3))
print("Subtract:", calc.subtract(10, 4))
print("Multiply:", calc.multiply(6, 2))