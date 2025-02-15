class Talaba:
    print("Malumotlar\n")
    def __init__(self, name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.bosqich = 1

    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.last_name

    def full_name(self):
        return f'{self.name} {self.last_name}'

    def get_age(self):
        return self.age

    def kurs(self):
        return self.bosqich

    def update_bosqich(self):
        self.bosqich += 1

    def get_info(self):
        return f'{self.name} {self.last_name} {self.bosqich}-bosqich talabasi'

    def information(self):
        return f'Ism: {self.name}\nFamiliya: {self.last_name}\nYosh: {self.age}\nBosqich: {self.bosqich}'



tala = Talaba('Akobir', 'Marupov', 21)


class Fan:
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_nome(self):
        return self.nomi

    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]

    def get_students_num(self):
        return self.talabalar_soni

matematika = Fan('Oliy matematika')
talaba1 = Talaba('Ali','Sayfiyev', 21)
talaba2 = Talaba('Komil', 'Isakov', 20)
talaba3 = Talaba('Sardor', 'Isomov', 24)

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

print(matematika.get_nome())
