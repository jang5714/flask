class Calculator(object):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(selfs):
        return selfs.num1 + selfs.num2

    def subtract(self):
        return self.num1 - self.num2

    def mulitple(self):
        return self.num1 * self.num2

    def divice(self):
        return self.num2 / self.num2

    @staticmethod
    def main():
        while 1:
            num1 = int(input('first number'))
            num2 = int(input('second number'))
            calc = Calculator(num1, num2)
            menu = input('0-Exit 1: + 2: - 3: * 4: /\n')
            if menu == '0':
                return
            elif menu == '1':
                print(f'{calc.num1} + {calc.num2} = {calc.add()}')
                break
            elif menu == '2':
                print(f'{calc.num1} - {calc.num2} = {calc.subtract()}')
                break
            elif menu == '3':
                print(f'{calc.num1} * {calc.num2} = {calc.mulitple()}')
                break
            elif menu == '4':
                print(f'{calc.num1} / {calc.num2} = {calc.divice()}')
                break
            else:
                print('Wrong Selected Number')
                break

Calculator.main()

