import random


class HiddenNumber:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.result = self._perform_operation()

    def _perform_operation(self):
        operations = [lambda x, y: x + y,
                      lambda x, y: x - y,
                      lambda x, y: x * y,
                      lambda x, y: x / y if y != 0 else None]  #
        operation = random.choice(operations)
        return operation(self.num1, self.num2)

    def __str__(self):
        return str(self.result)


num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

hidden_number = HiddenNumber(num1, num2)

print(hidden_number)
