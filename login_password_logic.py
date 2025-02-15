
class User:
    def __init__(self):
        self.user = {}

    def counter_character(self,word):
        cater = ['@', '$', '%', '&', '*', '_', '(', ')']
        c = 0
        for letter in word:
            if letter in cater:
                c += 1
        return c

    def couter_number(self,num):
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        k = 0
        for numbers in num:
            if numbers in number:
                k += 1
        return k

    def check_password(self, password):
        if " " in password:
            return False
        return True

    def user_password(self,username,password):
        if len(password) >= 6 and self.counter_character(password) > 0 and self.couter_number(
                password) > 0 and self.check_password(password):
            self.user[username] = password

    def add_user(self,username,password):
        if len(password) >= 6 and self.counter_character(password) > 0 and self.couter_number(password) > 0 and self.check_password(password):
            self.user[username] = password
            return f'Foydalanuvchi {username} muvaffaqiyatli qo`shildi..'
        return 'Xatolik..'

    def shoe_user(self,username):
        if self.user:
            return f'{username} nomli foydalanuvchi bazada mavjud..'
        return f'{username} nomli fpydalanuvchi bazada yuq..'

    def update_password(self,username,old_password,new_password):
        if username in self.user and self.user[username] == old_password:
            if len(new_password) >= 6 and self.counter_character(new_password) > 0 and self.couter_number(new_password) > 0 and self.check_password(new_password):
                self.user[username] = new_password
                return 'Prol yangilandi..'
            return 'Login yoki parolda xatolik bor..'

    def uptade_username(self,old_username,new_username,password):
        if old_username in self.user and self.user[old_username] == password:
            if new_username in self.user:
                return f'{new_username} nomli login allqachon mavjud..'
            else:
                self.user[new_username] = password
                del self.user[old_username]
                return 'Login muvaffaqiyatli o`zgartirildi..'
        return 'Login yoki Parol xato..'

    def delete_user(self,username):
        if username and self.user:
            del self.user[username]
            return 'Foydalanuvchi muvofaqqqiyatli uchirildi..'
        return 'Bunday foydalanuvchi mavjud emas..'

    def show_user(self):
        if self.user:
            print('Foydalanuvchilar ro`yxati\n')
            for username in self.user.keys():
                print(username)
        else:
             print('Foydalanuvchilar mavjud emas..!')

    def regestratsiya(self,username):
        if username in self.user:
            return f'Foydalanuvchi, {username} bazada mavjud..'
        return 'Xatolik. Bundan login mavjud emas..'

    def get_users(self,username,password):
        if username in self.user and self.user[username] == password:
            return 'Tizimga kirishingiz mumkin..'
        return 'Xatolik. Bundan login mavjud emas..'

    def main(self):
        while True:
            print('\n__Login va Password tizimi__')
            print('1) Parolni o`zgartiris: ')
            print('2) Loginini o`zgartirish ')
            print('3)  Foydalanuvchini o`chirish ')
            print('4) Foydalanuvchi ro`yxatda mavjudligini tekshirish ')
            print('5) Foydalanuvchilar ruyxati')
            print('6) Tizimga kirish')
            print('q -> Chiqish ')
            choice = input("Tanlovni kiriting (1-4): ")

            if choice == '1':
                username = input('Login kiriting: ')
                old_password = input('Eski parol kiriting: ')
                new_password = input('Ynagi parol kiriting: ')
                print(self.update_password(username,old_password, new_password))

            elif choice == '2':
                old_username = input('Eski login kiriting: ')
                new_username = input('Yangi login kiriting: ')
                passwoed = input('Parol kiriting: ')
                print(self.uptade_username(old_username,new_username,passwoed))

            elif choice == '3':
                username = input('Login kiriting: ')
                print(self.delete_user(username))

            elif choice == '4':
                username = input('Login kiriting: ')
                print(self.regestratsiya(username))

            elif choice == '5':
                print(self.show_user())

            elif choice == '6':
                username = input('Login kiriting: ')
                password = input('Parol kiriting: ')
                print(self.get_users(username, password))

            elif choice == 'q':
                print('Tizimdan chiqish..')
                break

if __name__=='__main__':
    system = User()
    count = int(input('Nechta foydalanuvchi qo`shasiz: '))
    for i in range(count):
        username = input(f'{i+1}- foydalanuvchi: ')
        password = input('Parol: ')
        print(system.user_password(  username,password))
    system.main()
