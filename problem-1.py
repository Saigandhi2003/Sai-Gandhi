class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "addition":
            return self.a + self.b
        elif self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "division":
            if self.b == 0:
                return "Error: Division by zero is not allowed"
            return self.a / self.b
        else:
            return "Invalid operation type"
          
if __name__ == "__main__":
    a = float(input("Enter first number : "))
    b = float(input("Enter second number : "))
    operation = input("Enter operation (addition, subtraction, multiplication, division): ")

    calc = Calculator(a, b, operation)
    result = calc.calculate()
    print("Result:", result)
