
'''
#XANOY O`YINI____
#2**n -1
def xanoy(n):
    for i in range(n):
        i = 2**n -1
        return i

n = int(input("Nechta aylana borligini kiriting: "))
print(f'{n} ta aylanani {xanoy(n)} ta harakatda joylash mumkin...!')
'''

'''
#input orqali kiritilgan sonlarni qo`shish:
sonlar =[]

for i in range(4):
    son = float(input(f'{i + 1}-son kiriting: '))
    sonlar.append(son)

natija = sum(sonlar)
print("Natija:",natija)
'''
'''
#Input orqali kiritilgan sonlar ichidan faqat toq sonlarni chiqaruvchi dastur 
sonlar = []

for i in range(5):
    son = float(input(f'{i+1}-sonni kiriting: '))
    sonlar.append(son)

toq_son = []
for son in sonlar:
    if son % 2 != 0:
        toq_son.append(son)
print("Natija: ",toq_son)

'''
'''

# Bitta matnda necha marta <men> so`zi qatnashganini aniqlash...!
tex = input("Mtn kiriting: ")
sanoq = 0

for matn in tex.split():
    if matn.lower() == "men":
        sanoq += 1

print(f'Natija: {sanoq}')

'''
'''
#1 dan 20 gacha bo`lgan sonlar ichida 3 va 5 ga bo`linadigan sonni topish:
for i in range(1,20):
    if i % 5 == 0 and i % 3 == 0:
        print(i)
'''
''''
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Fibonacci ketma-ketligining nechta elementini chiqarishni xohlaysiz? "))
fib_elements = fibonacci(n)

print(f"Fibonacci ketma-ketligi: {fib_elements}")
'''

'''
def raqamlar_yigindisi(n):
    yigindi = 0

    while n > 0:
        raqam = n % 10
        yigindi += raqam
        n //= 10

    return yigindi

son = int(input("Sonni kiriting: "))
natija = raqamlar_yigindisi(son)

print(f"Natija: {natija}")
'''
'''
def raqamlar_yigindisi(n):
    yigindi = 0

    raqamlar = [int(raqam) for raqam in str(n)]

    for raqam in raqamlar:
        yigindi += raqam

    return yigindi
son = int(input("Sonni kiriting: "))
natija = raqamlar_yigindisi(son)

print(f"Natija: {natija}")
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 29
if is_prime(number):
    print(f"{number} tub son.")
else:
    print(f"{number} tub son emas.")






























