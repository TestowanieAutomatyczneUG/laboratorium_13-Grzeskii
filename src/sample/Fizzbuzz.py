class FizzBuzz:

    def game(self, num):
        if type(num) is not int:
            return "TypeError"
        if int(num) % 15 == 0:
            return "FizzBuzz"
        elif int(num) % 3 == 0:
            return "Fizz"
        elif int(num) % 5 == 0:
            return "Buzz"
        else:
            return "Indivisible number"
