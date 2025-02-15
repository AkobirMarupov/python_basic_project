user = {}

caunt = int(input('Nechta foydalanuvchi qo`shasan: '))

def counter_character(word):
    sign = ['@', '$', '%', '&', '*', '_', '(', ')']
    c = 0
    for letter in word:
        if letter in sign:
            c += 1
    return c

def counter_number(pey):
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    k = 0
    for numbers in pey:
        if numbers in number:
            k += 1
    return k

def check_password(password):
    if " " in password:
        return False
    return True

for i in range(caunt):
    username = input(f"{i+1}-Login kiriting: ")

    if len(username):
        password = input('Password kiriting: ')
        if len(password) >= 6 and counter_character(password) > 0 and counter_number(
                password) > 0 and check_password(password):
            user[username] = password
        else:
           print('Xatolik...')

def show_username():
    if user:
        print('Foydalanuvchilar ro`yxati!')
        for username in user.keys():
            print(username)
    else:
        print('Foydalanuvchilar mavjud emas..!')

def update_password(username,old_password,new_password):
    if username in user and user[username] == old_password:
        if len(password) >= 6 and counter_character(password) > 0 and counter_number(
                password) > 0 and check_password(password):
            user[username] = new_password
            return f'Parol muvofaqqiyatli o`zgartirildi..'
        return 'Yangi parol shartlarga javob bermaydi..'
    return 'Xatolik: Eski parol yoki login xato..'

def update_username(old_username,new_username,password):
    if old_username in user and user[old_username] == password:
        if new_username in user:
            return 'Bunday login bazada allaqachon mavjud..'
        else:
            user[new_username] =password
            return 'Login muvaffaqiyatli o`zgartirildi..'

def delete_username(username):
    if username in user:
        del user[username]
        return 'Login muvaffaqiyatli uchirildi..'
    else:
        return 'Bunday login bazada yuq..'

def regestratsiya(username):
    if username in user:
        return f'Foydalanuvchi, {username} bazada mavjud..'
    else:
        return f'Foydalanuvchi, {username} bazaga kiritilmagan..'

def entrance(username,password):
    if username in user and user[username] == password:
        return 'Tizimga kirishingiz mumkin..!'
    else:
        return 'Parol yoki Login xato..!'

def main():
    while True:
        print('\n__Login va Password tizimi__')
        print('1) Parolni o`zgartiris: ')
        print('2) Loginini o`zgartirish ')
        print('3)  Foydalanuvchini o`chirish ')
        print('4) Foydalanuvchi ro`yxatda mavjudligini tekshirish ')
        print('5) Foydalanuvchilar ruyxati')
        print('6) Tizizmga kirish')
        print('q -> Chiqish ')
        choice = input("Tanlovni kiriting (1-4): ")

        if choice == '1':
            username = input('Login kiriting: ')
            old_password = input('Eski parol kiriting: ')
            new_password = input('Yangi parol kiriting')
            print(update_password(username,old_password,new_password))

        elif choice == '2':
            old_username = input('Eski login kiriting: ')
            new_username = input('Yangi login kiriting: ')
            password = input('Parol kiriting: ')
            print(update_username(old_username,new_username,password))

        elif choice == '3':
            username = input('Login kiriting: ')
            print(delete_username(username))

        elif choice == '4':
            username = input('Login kiriting: ')
            print(regestratsiya(username))

        elif choice == '5':
            print(show_username())

        elif choice == '6':
            username = input('Login kiriting: ')
            password = input('Parol kiriting: ')
            print(entrance(username,password))

        elif choice == 'q':
            print('Tizimdan chiqish..')
            break

        else:
            print("Noto'g'ri tanlov. Iltimos, 1 dan 7 gacha bo'lgan raqamni tanlang.")

if __name__== "__main__":
    main()

