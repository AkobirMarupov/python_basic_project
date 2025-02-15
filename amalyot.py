'''
#1. Fibonacci qatorini berilgan N gacha chiqarish.
def fabionce(n):
  a,b = 0,1
  fabionce_a = []

  while a <= n:
    fabionce_a.append(a)
    a,b = b,a+b
  return fabionce_a

N = int(input("Son kiriting: "))
result = fabionce(N)
print("Natija: ",result)
'''
from ctypes import HRESULT
from idlelib.debugger_r import restart_subprocess_debugger
from idlelib.debugobj_r import remote_object_tree_item
from tkinter.font import families

'''
from venv import create


#2. Berilgan sonning tub bo'lishini tekshirish, lekin 2 dan N gacha bo'lgan barcha tub sonlarni chiqarish.

def tub(n):
  if n <= 1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

D = int(input("Son kiriting: "))
if tub(D):
  print("Tub son: ",D)
else:
  print("Tub emas: ",D)

'''

# 4. Foydalanuvchidan raqamlar qabul qilib, ularni o'zaro almashtirish (birinchi va ikkinchi raqamlar).
'''
#1-usul
while True:
  try:
    a = float(int(input("1- Sonni kiriting: ")))
    b = float(int(input("2- Sonni kiriting: ")))
    break

  except ValueError:
    print("Iltimos, raqam kiriting.")

a,b = b,a

print(a,b)

'''
'''
#2-usul
numbers = []

for i in range(2):

  while True:
      n = float(input(f'{i + 1}- sonni kiriting: '))
      numbers.append(n)
      break

numbers[0], numbers[1] = numbers[1], numbers[0]
print(f'Natija: {numbers[0],numbers[1]}')
'''

# 5. Berilgan raqamlar ro'yxatidagi eng katta va eng kichik raqamlarni aniqlash.
'''
#1-usul:
numbers = []

for i in range(5):
    sonlar = float(input(f'{i + 1}-sonni kiriting: '))
    numbers.append(sonlar)

max= max(numbers)
min = min(numbers)

print(f"Max qiymat: {max}")
print(f"Min qiymat: {min}")
'''
# 2-usul:
'''
numbers = []
creat = 0

while creat < 5:
  num = input(f'{creat+1}-sonni kiritig: ')
  numbers.append(num)
  creat += 1

max = max(numbers)
min = min(numbers)

print("Katta son: ",max)
print("Kichik son: ",min)

'''

# 6. Berilgan so'zning palindrom ekanligini tekshirish.
'''
def palendrom(word):
  text = ''.join(word.lower().split())
  return text == text[::-1]

tex = input("Suz kiriting: ")

if palendrom(tex):
  print(tex,"-> Palendtrom...")
else:
  print(tex,"-> Palendrom emas...")
'''

# 7. Berilgan ro'yxatdagi juft sonlarni chiqarish.
'''
#1-usul for orqali
numbers = []

for i in range(5):
  son = int(input(f'{i + 1}-sonni kiriting: '))
  numbers.append(son)

juft_sonlar = []

for son in numbers:
  if son % 2 == 0:
    juft_sonlar.append(son)

print("Juft sonlar -> ",juft_sonlar)

'''

# 2-usul while orqali:
'''
sonlar = []
summa = 0

while summa < 5:
  son = int(input(f'{summa + 1}-sonni kiriting: '))
  sonlar.append(son)
  summa += 1

juftlar = []
k = 0

while k < len(sonlar):
  if sonlar[k] % 2 == 0:
    juftlar.append(sonlar[k])
  k += 1

print("Juft sonlar: ",juftlar)
'''

# 8. Foydalanuvchidan raqamlar qabul qilib, ularning yig'indisini va o'rtacha qiymatini hisoblash.
'''
#1-usul:

raqamlar = []
i = 0

while True:
  kiritilgan = input(f"{i + 1}-raqamni kiriting: ")
  if kiritilgan.lower() == 'exit':
    break
  try:
    raqam = float(kiritilgan)
    raqamlar.append(raqam)
    i += 1
  except ValueError:
    print("To`xtatish uchun 'exit' deb yozing.")

if raqamlar:
  yigindi = sum(raqamlar)
  ortacha = yigindi / len(raqamlar)

  print("Yig'indi:", yigindi)
  print("O'rtacha qiymat:", ortacha)
else:
  print("Hech qanday raqam kiritilmadi.")
'''

# 2-usul:
'''
sonlar = []

for i in range(5):
    while True:
      try:
        num = int(input(f'{i + 1}-sonni kiriting: '))
        sonlar.append(num)
        break
      except ValueError:
        print("To`g`ri son kiriting...")

if sonlar:
  yigindi = sum(sonlar)
  urtacha = yigindi/len(sonlar)

  print("Yig`indi ->", yigindi)
  print("O`rtacha ->", urtacha)

else:
  print("Hechqanday raqam son kiritilmagan")
'''

# 9. N gacha bo'lgan sonlarning kvadratlari va kubini chiqarish.
'''
n = int(input('Son kiriting: '))

for i in range(1,n):
  kvadrat = i**2
  kub = i**3

  print("Kvadratlari: ",kvadrat)
  print("Kublari: ",kub)
'''

# 10. Berilgan raqamning faktorialini hisoblash.
'''
n = int(input("Faktorialini hisoblash uchun raqamni kiriting: "))

def factorial(x):
  if x == 0 or x == 1:
    return 1
  else:
    return x * factorial(x-1)

result = factorial(n)
print("Natija: ", result)
'''
# 11. N gacha bo'lgan tub sonlarni chiqarish va ularning yig'indisini hisoblash.
'''
n = int(input("Son kiriting: "))
summa = 0
for i in range(1,n+1):
  summa += i
  print(i)
print(f'1 dan {n} gacha bo`lgan sonlarning yig`indisi: {summa}')
'''

# 12. Foydalanuvchidan so'zlar qabul qilib, ularni teskari tartibda chiqarish.
'''
sozlar = input("So'zlarni kiriting (bo'sh joy bilan ajratilgan): ")

sozlar_royxati = sozlar.split()

teskari_sozlar = sozlar_royxati[::-1]

print("Teskari tartibda so'zlar:")
print(" ".join(teskari_sozlar))
'''
'''
sozlar = input("So'zlarni kiriting (bo'sh joy bilan ajratilgan): ")

sozlar_royxati = sozlar.split()

teskari_sozlar = []

for i in range(len(sozlar_royxati) - 1, -1, -1):
    teskari_sozlar.append(sozlar_royxati[i])

print("Teskari tartibda so'zlar:")
print(" ".join(teskari_sozlar))

'''
'''
class Dog:
    species = "Canis familiaris"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def malumot(self):
        return f'Itning nomi: {self.name}, # Itning yoshi: {self.age}'

    def speak(self,ovozi):
        return f'{self.name} tovushi {ovozi}'

miles = Dog("Miles", 4)

print(miles.malumot())

#bob = Dog("Bobik", 11)
#budy = Dog("Budy", 4)
'''
'''
car = {'model': 'Mers', 'rang': 'Qora'}
print('Modeli: ',car['model'])
print('Rangi: ',car['rang'])
'''
'''
talaba = {}

talaba['ism'] = 'akobir marupov'
talaba['yosh'] = 21
talaba['kurs'] = 3

#print(talaba)
#print(f'{talaba['ism'].title()} {talaba['yosh']} yoshda {talaba['kurs']}-kursda uqiydi')

talaba['kurs'] = 4
print(f'{talaba['ism'].title()} {talaba['yosh']} yoshda {talaba['kurs']}-kursda uqiydi')
'''
'''
talaba = {'Akobir': 'Marupov', 'Ali': 'Quvvatov',
          'Ahror': 'Akobirov', 'Pulat': 'Suyunov',
          }
for key,valeu in talaba.items():
    print(f'Ism: {key}')
    print(f'Familiya: {valeu} \n')
'''
'''
mahsulotlar = {'apilsin': 30000,'uzum': 20000, 'olma': 18000, 'non': 5000, 'nok': 45000}
print('Dukondagi mahsulotlar.')

#bozorlik = ['olma','non','nok','urik','kulcha']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f'{mahsulot.title()} {mahsulotlar[mahsulot]} so`m')

#for tovar in bozorlik:
#    if tovar not in mahsulotlar:
#        print(f'Iltimos, dukoningizga {tovar}ni ham olib keling!')

for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())
'''
'''
list = ['juma','kun','boy','yil','juma','kun','juma']

print(list)
'''
'''
from collections import Counter

def element(input_list):
    return dict(Counter(input_list))

# Misol
my_list = ['juma','kun','boy','yil','juma','kun','juma']
result = element(my_list)
print(result)
'''

'''
def count_elements(input_list):
    element_count = {}
    for element in input_list:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

# Misol
my_list = ['juma','kun','boy','yil','juma','kun','juma']
result = count_elements(my_list)
print(result)
'''
'''
def takrorlanishlar(kunlar):
    elementlar = {}
    for kun in kunlar:
        if kun in elementlar:
            elementlar[kun] += 1

        else:
            elementlar[kun] = 1

    return elementlar

my_list = ['juma','kun','boy','yil','juma','kun','juma']
result = takrorlanishlar(my_list)
print(result)
'''
'''
class Car:
    def __init__(self,model,yil,kg):
        self.model = model
        self.yil = yil
        self.kg = kg

    def malumotlar(self):
        return f'Modeli: {self.model}, Yil: {self.yil}, Og`irligi: {self.kg} kg'

found = Car('Mersedes Bens', 2024, 1200)

print(Car.malumotlar(found))
'''
'''
def two_sum(nums, target):
    num_to_index = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

nums1 = [2, 7, 11, 15]
target1 = 18
print(two_sum(nums1, target1))
'''

'''
def two_sum(nums, target):
    num_index = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_index:
            return [num_index[complement], index]
        num_index[num] = index

nums1 = [1,2,3,7,9]
project = int(input('Son kiriting: '))
print(two_sum(nums1,project))
'''
'''
def two_sum(nums, target):
    num_index = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_index:
            return [num_index[complement], index]
        num_index[num] = index

nums1 = [1, 2, 3, 7, 9, 8]
project = 10
print(two_sum(nums1, project))
'''

'''
print('Dustlaringizni ruyxatini tuzamiz: ')

ismlar = []

n = 1
while True:
    savol = f'{n}-dustingizni kiriting: '
    ism = input(savol)
    ismlar.append(ism)
    tarkrorlash = input('Yana ism kiritasizmi (ha/yuq) ? ')
    n += 1
    if tarkrorlash != 'ha':
        break

print('Dustlaringizning ruyxati')
for ism in ismlar:
    print(ism.title())
'''
'''
dostlar = {}
n = 1
shart = True

while shart:
    ism = input(f'{n}-dustingizni ismini kiriting: ')
    yosh = input(f'{n}-dustingizni yoshini kiriting: ')
    dostlar[ism] = int(yosh)

    javob = input('Yana dustingizni kiritaszmi (ha / yuq) ?: ')
    n += 1
    if javob == 'yuq':
        shart = False
print(' ')
print('Dustlaringizning Malumotlari')

for ism, yosh in dostlar.items():
#    print(f'{ism.title()} {yosh} yoshga teng')
    print(dostlar)
'''
'''
def palendrom(word):
    return word.lower() == word[::-1].lower()

suz = 'aka'

if palendrom(suz):
    print(f'{suz} -> palendrom!')

else:
    print('Palendrom emas...')
'''

'''
class Palendrom:
    def is_palindrom(self,word):
        return word.lower() == word[::-1].lower()

tex = 'aka'
chacke = Palendrom()

if chacke.is_palindrom(tex):
    print(f'{tex} -> palindrom suz!')

else:
    print('Palindrom emas!')

'''
'''
def Textr(tex_list):
    return len([string for string in tex_list if string])

tex_list = ['apple', '', 'banana', 'kfc', '']
result = Textr(tex_list)
print('Natija: ', result)

'''

'''
def uzunlik(text):
    return len(text)

suz = input("Suz kiritinng: ")
result = uzunlik(suz)
print('Natija: ', result)
'''

'''
def Palindrom(son):
    str_number = str(son)
    return str_number == str_number[::-1]

number = 121
result = Palindrom(number)
print('Natija: ', result)
'''

'''
def belgilar(tex):
    if len(tex) > 1:
        return tex[0]+'$' * (len(tex)-1)
    return tex

k = input("Suz kiriting: ")
result = belgilar(k)
print(result)
'''

'''
def almashtirish(text1,text2):
    k1 = text1[:2]
    k2 = text2[:2]

    l1 = text1[2:]
    l2 = text2[2:]

    qush1 = k1 + l2
    qush2 = k2 + l1
    return qush1 + " " + qush2

suz1 = 'Hello'
suz2 = 'World'

result  = almashtirish(suz1,suz2)
print('Natija: ',result)
'''
'''
def kesma(satr, n):
    return satr[:n] + satr[n+1:]

satrlar = input('Satr kiriting: ')
n = 7
result = kesma(satrlar,n)
print('Natija: ', result)
'''

'''
def Almashtirish(text):

    if len(text) <= 1:
        return text

    return text[-1] + text[1:-1] + text[0]

t = input("Suz kiriting: ")
result = Almashtirish(t)
print('Natija: ', result)
'''

# def text(satr):
#
#     return satr.replace(' ','')
#
# suz = 'Akobir Marupov'
# result = text(suz)
# print(result)

#
# def birlashma(suz):
#     sev = ''
#     for char in suz:
#         if char not in sev:
#             sev += char
#     return sev
#
# k = 'akobir marupov'
# result = birlashma(k)
# print(result)
#
# def speace(text):
#     return text.replace(' ','')
#
# s = 'Akobir Marupov'
# result  =  speace(s)
# print(result)

# def ranglar(rang):
#     return rang[0],rang[-1]
#
# color = ['oq','qora', 'yashil', 'sariq']
# k1,k2 = ranglar(color)
# print(f'Birinchi rang - {k1}')
# print(f'oxirgi rang - {k2}')
#

# class Talaba:
#     def __init__(self,ism,familiya,yil):
#         self.ism = ism
#         self.familiya = familiya
#         self.yil = yil
#
#     def last_name(self):
#         return self.familiya
#
#     def get_name(self):
#         return self.ism
#
#     def ful_name(self):
#         return f'{self.ism} {self.familiya}'
#
#     def get_age(self,yosh):
#         return yosh - self.yil
#
#     def malumotlar(self):
#         return f'Talaba {self.ism} {self.familiya} {self.yil} yilda tugilgan! '
#
# student = Talaba('Akobir', 'Marupov', 2004)
# result = student.last_name()
# print(result)

# class User:
#     def __init__(self, first_name, last_name, age, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = email
#
#     def information(self):
#         return f'Ism: {self.first_name}\nFamiliya: {self.last_name}\nYosh: {self.age}\nEmail: {self.email}'
#
# print("Malumotlar kiritish:")
# first = input("Ism: ")
# last = input("Familiya: ")
# agea = int(input("Yosh: "))
# emaila = input("Email: ")
#
# user = User(first, last, agea, emaila)
#
# print("\nKiritilgan ma'lumotlar:")
# print(user.information())

'''
class Shaxs:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        return self.ism

    def get_lastname(self):
        return self.familiya

    def get_ful_name(self):
        return f'{self.ism} {self.familiya}'

    def get_age(self,yil):
        return yil - self.tyil

    def get_info(self):
        return f'{self.ism} {self.familiya}, {self.tyil}-yilda tug`ilgan!!!'


class Talaba(Shaxs):
    def __init__(self,ism,familiya,tyil,idraqam,manzi):
        super().__init__(ism,familiya,tyil)
        self.idraqam = idraqam
        self.manzil = manzi
        self.bosqich = 1

    def get_idraqam(self):
        return self.get_idraqam

    def get_bosqich(self):
        return self.bosqich

    def get_info(self):
        info = f'{self.ism} {self.familiya}, {self.tyil}-yilda tug`ilgan'
        info += f' {self.bosqich}-bosqich talabasi, {self.idraqam} ID raqamda turadi!'
        return info


class Manzil:
    def __init__(self,viloyat,kucha,uy):
        self.viloyat = viloyat
        self.kucha = kucha
        self.uy = uy

    def get_manzil(self):
        return f'{self.viloyat} viloyati, {self.kucha} kuchasi, {self.uy}-uy'

manzil = Manzil('Samarqand', 'Guzalkent', 27)
talaba1 = Talaba('Akobir', 'Marupov', 2004, 'BC098789', manzil)
print(talaba1.manzil.get_manzil())

'''

#
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#
#     else:
#         print(car.title())


# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#
#     else:
#         print(car.upper())

# ism = input('Tuliq ismingizni kiriting: ')
# login = input('Loginni kiriting: ')
#
# if login == 'Admin':
#     print(f'Xush kelibsiz {ism}. Foydalanuvchilar ro`yxatini ko`rasizmi?')
#
# else:
#     print(f'Xush kelibsiz {ism}')

# son1 = int(input('1-sonni kiriting: '))
# son2 = int(input('2-sonni kiriting: '))
#
# kattasi = max(son1, son2)
# kichigi = min(son1, son2)
#
# if son1 == son2:
#     print(f'{son1} = {son2} Ikkala son ham teng')
#
# else:
#     print(f'{kattasi} katta, {kichigi} kichik')

# mahsulotlar = ['olma','urik','gilos','kola','non','osh','nok','olcha','pishloq','anor']
#
# savat = []
#
# for i in range(5):
#     mahsulot = input(f'{i+1}-mahsulotni kirting: ')
#     savat.append(mahsulot)
#
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} - Mahsulot do'konimizda bor")
#     else:
#         print(f"{mahsulot} - Mahsulot do'konimizda yo'q")

# mahsulotlar = ['olma','urik','gilos','kola','non','osh','nok','olcha','pishloq','anor']
#
# savat = []
#
# for i in range(5):
#     mahsulot = input(f'{i+1}-mahsulotni qo`shing: ')
#     savat.append(mahsulot)
#
# bor_mah = []
# yuq_mah = []
#
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mah.append(savat)
#     else:
#         yuq_mah.append(mahsulot)
#
# if len(yuq_mah) == 0:
#     print('Siz so`ragan barcha mahsulotlar dukonimizda bor!')
#
# else:
#     print('Quidagi mahsulotlar dukonimizda yuq!')
#     for mahsulot in yuq_mah:
#         print(mahsulot)


# mahsulotlar = ['olma','urik','gilos','kola','non','osh','nok','olcha','pishloq','anor']
#
# savat = []
#
# for i in range(5):
#     mahsulot = input(f'{i+1} mahsulot kiriting: ')
#     savat.append(mahsulot)
#
# bor_mahahsulotlar = []
# yuq_mahsulotlar = []
#
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahahsulotlar.append(mahsulot)
#
#     else:
#        yuq_mahsulotlar.append(mahsulot)
#
# if bor_mahahsulotlar:
#     print('Quidagi mahsulotlar dukonda bor:')
#     for mahsulot in bor_mahahsulotlar:
#         print(mahsulot)
#
# if yuq_mahsulotlar:
#     print('Quidagi mahsulotlar dukonda yuq:')
#     for mahsulot in yuq_mahsulotlar:
#         print(mahsulot)
#
# else:
#     print('Siz so`ragan barcha mahsulotlar dukonda bor:')
'''
fwefraefraed
'''
# p = [{"Aziz": "Qwerty_123@"}, {"Akobir": "Akobir_2004"}]
#
# people = []
# count = int(input("nechta foydalanuvchi kiritmoqchisiz? : "))
# for i in range(0, count):
#     f = input(f"{i + 1}-foydalanuvchi nomi:")
#     people.append(f)
#
# print("[1] - foydalanuvchilarni nomini korsatish\n[2] - login qilinganligini check qilish\n")
# choice = int(input("qaysi amalni bajarasiz?:"))
# if choice == 1:
#     for person in people:
#         print(person)
# elif choice == 2:
#     input_person = input('Foydalanuvchi loginini kiriting: ').lower().replace(" ", "")
#
#     found = False
#
#     for person in people:
#         cleaned_person = person.lower().replace(" ", "")
#
#         if cleaned_person == input_person or input_person.find(cleaned_person) != -1:
#             print("Ro'yxatdan o'tilgan..")
#             found = True
#             break
#
#     if not found:
#         print("Xush kelibsiz..")
# else:
#     print("xato amaliyot..")
from uuid import uuid4
class Car:

    __num_avto = 0
    def __init__(self,model,year,color,km = 0):
        self.model = model
        self.year = year
        self.color = color
        self.__km = km
        self.__id = uuid4()
        Car.__num_avto += 1

    @classmethod
    def get_num_car(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self,km):
        if km > 0:
            self.__km += km
        else:
            print('Mashinaning km kamaymaydi:')

avto1 = Car("Malibu",2020,"Qora",100)
avto2 = Car("Mers",2025,"Qora",300)
avto3 = Car("BMW",2024,"Qora",400)
avto = Car("BMW",2024,"Qora",400)
avto1.add_km(1500)
print(avto1.get_num_car())

























