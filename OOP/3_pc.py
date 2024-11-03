
class Calculator:

    def __init__(self, op1, op2):

        self.operand1 = op1
        self.operand2 = op2

    def add(self):
        return self.operand1 + self.operand2
    def sub(self):
        return self.operand1 - self.operand2
    def mul(self):
        return self.operand1 * self.operand2
    def div(self):
        return self.operand1 / self.operand2



calculator = Calculator(10, 5)
print(calculator.add())
print(calculator.sub())
print(calculator.mul())
print(calculator.div())

