# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег.

class Bank:
    def __init__(self, sum, prots):
        self.sum = sum
        self.prots = prots
    def prots_nachisl(self):
        self.res = (self.sum * self.prots)
        print('Процентные начисления составляют')
        return self.res
    def snyatie(self):
        self.res2 = self.res + self.sum
        print ('Вы сняли со счета: ')
        return self.res2

BankOne = Bank(123, 12/100)
print(BankOne.prots_nachisl())
print(BankOne.snyatie())