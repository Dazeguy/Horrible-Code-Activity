#Simple clean calculator

#adding a single repsonsiblity

class Calculator(Calculator):
    def add(self, input1, input2):
        return input1 + input2
    def substract(self, input1, input2):
        return input1 - input2
    def multiply(self, input1, input2):
        return input1 * input2
    def divide(self, input1, input2):
        return input1 / input2


print(Calculator().add(1, 2))