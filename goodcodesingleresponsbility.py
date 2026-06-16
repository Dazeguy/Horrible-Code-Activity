#Simple clean calculator

#adding a single repsonsiblity


#creating calculations for only arithmetic
class Calculator:
    #addition
    def add(self, input1, input2):
        return input1 + input2
    #subtraction
    def subtract(self, input1, input2):
        return input1 - input2
    #multiplication
    def multiply(self, input1, input2):
        return input1 * input2
    #division
    def divide(self, input1, input2):
        return input1 / input2

#creating a single responsbility for user input
class UserInput:
    def get_numbers(self):
        input1 = float(input("Enter first number: "))
        input2 = float(input("Enter second number: "))
        return input1, input2

    def get_operation(self):
        return input("Enter operation (add, subtract, multiply, divide): ")


# Calling the functions and running a demo
calc = Calculator()
ui = UserInput()

input1, input2 = ui.get_numbers()
operation = ui.get_operation()

if operation == "add":
    print(calc.add(input1, input2))
elif operation == "subtract":
    print(calc.subtract(input1, input2))
elif operation == "multiply":
    print(calc.multiply(input1, input2))
elif operation == "divide":
    print(calc.divide(input1, input2))
else:
    print("Unknown operation")