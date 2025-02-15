'''
1. Mahsulotlar (Products) CRUD operatsiyalari:
Mahsulotni qo'shish (Add): Yangi mahsulot qo'shish uchun foydalanuvchi mahsulot nomi, narxi, ta'rifi va kategoriya
 haqida ma'lumotlar kiritadi. Bu ma'lumotlar dictionary (lug'at) sifatida saqlanadi. Har bir mahsulotga noyob
 identifikator (ID) beriladi.

Mahsulotni tahrirlash (Edit): Mahsulotni tahrirlash uchun foydalanuvchi mahsulotni tanlab, yangi qiymatlarni
(masalan, nomini, narxini yoki ta'rifini) kiritadi. Mahsulotdagi ma'lumotlar yangilanadi.

Mahsulotni o'chirish (Delete): Mahsulotni o'chirishda, foydalanuvchi mahsulotning ID yoki nomi orqali uni
tizimdan butunlay o'chiradi.

Mahsulotni olish (Get): Foydalanuvchi barcha mahsulotlarni ko'rish yoki maxsus ID orqali bitta mahsulotni
olish imkoniyatiga ega bo'ladi.

2. Kategoriya (Categories) CRUD operatsiyalari:
Kategoriya qo'shish (Add): Yangi kategoriya qo'shiladi. Kategoriya nomi va unga tegishli mahsulotlar ro'yxati
 saqlanadi. Har bir kategoriya o'ziga tegishli mahsulotlarni o'z ichiga oladi.

Kategoriya tahrirlash (Edit): Foydalanuvchi mavjud kategoriya nomini o'zgartirishi mumkin.

Kategoriya o'chirish (Delete): Agar kategoriya o'chirilsa, unga tegishli barcha mahsulotlar ham tizimdan o'chiriladi.
 Bu juda muhim, chunki kategoriya va mahsulotlar o'rtasida bog'lanish mavjud.

Kategoriya olish (Get): Foydalanuvchi barcha kategoriyalarni ko'rish yoki maxsus kategoriya ID bo'yicha bitta
kategoriya haqida ma'lumot olish imkoniyatiga ega bo'ladi.

3. Filtrlash va Qidirish:
Nom bo'yicha qidirish: Foydalanuvchi mahsulotlarni nomi bo'yicha qidirishi mumkin. Misol uchun, "laptop",
"smartfon" kabi nomlar bilan mahsulotlar qidiriladi.

Narx bo'yicha filtrlash: Foydalanuvchi mahsulotlarni narxiga qarab filtrlashi mumkin. Misol uchun, 1000 so'mdan
yuqori yoki 5000 so'mdan past mahsulotlar.

Kategoriya bo'yicha filtrlash: Mahsulotlar faqat ma'lum bir kategoriya bo'yicha ko'rsatilishi mumkin. Masalan,
"elektronika" kategoriyasidagi mahsulotlar.

4. Tizimdan Chiqish (Exit):
Tizimdan chiqish: Foydalanuvchi tizimdan chiqish uchun maxsus buyruqni tanlaydi, bu tizimni to'xtatadi.
'''

product = {}
category = {}



