class Calculator:

    def game(self, x, operation, y):
        if type(x) is not int or type(y) is not int:
            return "Wrong x/y type"
        elif operation == "+":
            return x + y
        elif operation == "-":
            return x - y
        elif operation == "*":
            return x * y
        elif operation == "/":
            return x / y
        else:
            return "Wrong operation type"
