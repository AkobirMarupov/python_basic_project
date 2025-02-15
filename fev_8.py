# class User:
#     def __init__(self, name, last_name, username,password):
#         self.name = name
#         self.last_name =last_name
#         self.username = username
#         self.password = password
#
#     def __repr__(self):
#         return self.username
#
#     def __str__(self):
#         return self.username
#
# class Auth:
#     def __init__(self):
#         self.users = []
#
#     def register_user(self, user: User):
#         username = user.username
#
#         if len(self.users) == 0:
#             self.users.append(user)
#             return ('User Added')
#
#         for u in self.users:
#             print(self.users)
#
#             if username == u.username:
#                raise Exception
#
#             self.users.append(user)
#             break
#
# user1 = User(name = 'Akobir', last_name='Marupov', username='akobir123', password='1234')
# user2 = User(name = 'Ali', last_name='Suyunov', username='jdorsey1', password='4321')
# user3 = User(name = 'Imron', last_name='Dilmurodov', username='imron3', password='4300')
# user4 = User(name = 'Xushnud', last_name='Marupov', username='xushnud12', password='4311')
#
#
# auth = Auth()
# auth.register_user(user=user1)
# auth.register_user(user=user2)
# print(auth.users)


class Car:

    wheels = 4

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print(self.name)
        print("instance method called", self)

    @staticmethod
    def static_method(word):
        print(f"word is {word}")

    @classmethod
    def class_method(cls, wheels):
        cls.wheels = wheels
        print("class method called", cls)

#
# print(Car.wheels)
# audi = Car(name='audi')
# merc = Car(name='merc')
#
# print(Car.class_method(wheels=5))
# print(Car.wheels)
# print(audi.wheels)
# print(merc.wheels)
# print("===="*10)
# print(audi.class_method(wheels=6))
# print(Car.wheels)
# print(audi.wheels)
# print(merc.wheels)
# print('instance class method', audi.class_method())
# print('class method', Car.class_method())

# print('instance method', audi.instance_method())
# print('static method', audi.static_method(word="hello"))


import random


class User:
    def __init__(self, name, username, password, age):
        self.name = name
        self.username = username
        self.__password = password
        self.age = age
        self.__account_number = None

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_account_number(self):
        return self.__account_number

    def get_password(self):
        return self.__password


class Bank:
    def __init__(self):
        self.users = []  # [User(name='a', username='u', password='pass', age=19), User(name='b', username='t', password='1234', age=34)...]

    def create_account(self, u: User):
        if u.age >= 18:
            self.users.append(u)
            account_id = random.randint(1000, 9999)
            u.set_account_number(account_number=account_id)
            print("Your account has been created")
            return account_id
        else:
            print("You are not eligible to create an account")
            return None

    def show_account_number(self):
        username = input("Enter your username: ")  # t
        password = input("Enter your password: ")  # 1234

        for user in self.users:
            if user.username == username and user.get_password() == password:
                print(f"Your account number is {user.get_account_number()}")
                break
            else:
                print("Invalid credentials")


u1 = User(name='a', username='u', password='pass', age=19)
u2 = User(name='b', username='t', password='1234', age=34)
u3 = User(name='c', username='v', password='pass', age=13)

bank = Bank()

print(bank.create_account(u1))
# print(bank.create_account(u2))
# print(bank.create_account(u3))
print("=="*10)
print(u1.get_account_number())
# print(u2.get_account_number())
# print(u3.get_account_number())
print("=="*10)

bank.show_account_number()
