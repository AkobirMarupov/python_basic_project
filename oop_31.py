'''
class Found:
    def __init__(self,brend,the_product,year,state):
        self.brend = brend
        self.the_product = the_product
        self.year = year
        self.state = state

    def show_obj(self):
        return f'Brendi: {self.brend}, The product: {self.the_product}, Year: {self.year}, State: {self.state}'

result = Found('GM', 'Malibu', '2024', 'Uzbekistan')
print(result.show_obj())

class Employee:
    bonus = 0.1

    def __init__(self,fist_name,last_name,salary,position):
        self.firs_name = fist_name
        self.last_name = last_name
        self.salary = salary
        self.position = position

    def full_name(self):
        return f'{self.firs_name}, {self.last_name}'

    def salarys(self):
        return self.salary

    def positions(self):
        return self.position

'''
from datetime import datetime


class Shaxs:
    def __init__(self, ism, mamlakat, tugilgan_sana):
        self.ism = ism
        self.mamlakat = mamlakat
        self.tugilgan_sana = datetime.strptime(tugilgan_sana,
                                               "%Y-%m-%d")  # Tug'ilgan sanani datetime formatiga o'tkazamiz

    def yoshini_hisobla(self):
        bugungi_kun = datetime.now()
        yosh = bugungi_kun.year - self.tugilgan_sana.year

        if (bugungi_kun.month, bugungi_kun.day) < (self.tugilgan_sana.month, self.tugilgan_sana.day):
            yosh -= 1

        return yosh

'''
ism = input("Ismingizni kiriting: ")
mamlakat = input("Mamlakatingizni kiriting: ")
tugilgan_sana = input("Tug'ilgan sanangizni YYYY-MM-DD formatida kiriting: ")

shaxs = Shaxs(ism, mamlakat, tugilgan_sana)

print(f"Ism: {shaxs.ism}")
print(f"Mamlakat: {shaxs.mamlakat}")
print(f"Tug'ilgan sana: {shaxs.tugilgan_sana.strftime('%Y-%m-%d')}")
print(f"Sizning yoshiz: {shaxs.yoshini_hisobla()} yoshda.")
'''

