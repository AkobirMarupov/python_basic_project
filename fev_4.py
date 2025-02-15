'''
class Shakllar:
    def __init__(self,a):
        self.a = a

    def yuza(self):
        return f'Yuzasi: {self.a**2}'

    def peremtr(self):
        return f'Peremetri: {self.a*4}'

f1  = Shakllar(6)
print(f1.yuza())
print(f1.peremtr())

'''
'''
class BancAccaunt:
    def __init__(self,name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount
        return self.__balance

    def withdrav(self,amount):
        self.__balance -= amount
        return self.__balance

    def chec_balance(self):
        return self.__balance

p1 = BancAccaunt("Ali", 200)

print(p1.deposit(10))
print(p1.withdrav(30))
print(p1.chec_balance())

'''

class Damine:
    def __init__(self, name, age):  # __int__ o'rniga __init__ bo'lishi kerak
        self.name = name
        self.age = age

    def malumotlar(self):
        return f'Itning laqabi: {self.name}, Itning yoshi: {self.age}'

bob1 = Damine('Bobik', 20)  # 20 raqam sifatida kiritilgan

print("Natija: ", bob1.malumotlar())



















