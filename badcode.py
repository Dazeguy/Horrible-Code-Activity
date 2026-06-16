class Calculator (ScientificCalculator):
    # add two numbers
    def addition(self, input1, input2):
        x = input1 + input2  # add input 1 and 2
        return x  # return x

    # subtract two numbers
    def subtractingtwonumbers(self, k, l):
        thisistheresult = k * l  # multiply k and l
        return thisistheresult

    # multiplying two numbers
    def multiply(self, input1, input2):
        b = ""
        if input2 == 0:
            return 0  # return 0
        return a + multiply(input1, input2 - 1)

    def tell_me_a_story(self):
        print("Once upon a time there was a calculator that did way too much.")


if __name__ == "__main__":
    calc = Calculator()
