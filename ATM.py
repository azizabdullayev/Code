from random import randrange

global a, b, c


def balans():
    a = randrange(1000, 10000000)
    print("Karta balansi: ", a)


def naqd_pul():
    a = randrange(1000, 10000000)
    print("1.10.000", "2. 50.000")
    print("3.100.000", "4. 500.000")
    print("5. Boshqa summa")
    b2 = int(input())
    if b2 == 1:
        print("Naqd pul yechildi: 10.000")
    elif b2 == 2:
        print("Naqd pul yechildi: 50.000")
    elif b2 == 3:
        print("Naqd pul yechildi: 100.000")
    elif b2 == 4:
        print("Naqd pul yechildi: 500.000")
    elif b2 == 5:
        print("Summani kiriting: ")
        h = int(input())
        if h <= a:
            print("Kartadan naqd pul yechildi: ", h, "Qoldi: ", a - h)
        elif h > a:
            print("Mablag' yetarli emas")
    else:
        print("Bunday funksiya mavjud emas!")


def sms_xabar():
    g = input("SMS Xabar funksiyasini ulash uchun o'z telefon raqamingizni kiriting: ")
    if len(g) == 9 or len(g) == 13 or len(g) == 12:
        print(g, "raqamiga tasdiqlovchi kod yuborildi")
        print("Diqqat 3 marotaba kiritish imkoniyatiga egasiz!")
        print("Shu kodni kiriting: ")
        d = input()
        i = 1
        u = True
        while u:
            if i <= 3:
                if len(d) == 6:
                    print(g, "raqamiga SMS Xabar muvaffaqiyatki ulandi!")
                    u = False
                else:
                    print("Tekshirib qaytadan kiriting: ")
                    d = input()
                i += 1
            else:
                print("Ma'lumorlar xato kiritildi!")
                u = False


def parol_ozgartirish():
    q = input("Hozirda ishlatayotgan parolingizni kiriting: ")
    f = input("O'zgartirmoqchi bolgan parolni kiriting: ")
    print("Diqqat 3 marotaba kiritish imkoniyatiga egasiz!")
    j = 1
    r = True
    while r:
        if j <= 3:
            if len(q) == 4 and len(f) == 4:
                print("Parol o'zgartirildi!")
                r = False
            else:
                print("Parollarda xatolik mavjud!")
                print("Iltimos tekshirib qaytadan tering: ")
                q = input("Hozirda ishlatayotgan parolingizni kiriting: ")
                f = input("O'zgartirmoqchi bolgan parolni kiriting: ")
            j += 1
        else:
            print("Urinishlar soni tugadi!")
            r = False


def telefon_raqam():
    a = randrange(1000, 10000000)
    k = input("Telefon raqamini kiriting: ")
    print("Diqqat 3 marotaba kiritish imkoniyatiga egasiz!")
    z = 1
    v = True
    while v:
        if z <= 2:
            if len(k) == 9 or len(k) == 13 or len(k) == 12:
                l = input("Summani kiriting")
                if len(l) >= 4 and len(l) <= 8:
                    print(k, "raqamiga ", l, " muvaffaquyatli o'tkazildi!")
                    print("Ballans: ", a)
                    v = False
                else:
                    print("Mablag' yetarli emas")
                    v = False
            else:
                print("Raqamni tekshirib qaytadan tering: ")
            z += 1
        else:
            print("Ma'lumotlar xato kiritildi!")
            v = False


print("Kartani kiriting: ha/yoq")
f = input()
if f == "ha" or f == "Ha" or f == "HA" or f == "hA":
    print("Parolni kiriting: ")
    c = input()
    if len(c) == 4:
        print("1.Balans", "2.Naqt Pul")
        print("3.Sms Xabar", "4. Parolni o'zgartirish")
        print("5. Telefon hisobini to'ldirish")
        b = int(input())
        if b == 1:
            balans()
        elif b == 2:
            naqd_pul()
        elif b == 3:
            sms_xabar()
        elif b == 4:
            parol_ozgartirish()
        elif b == 5:
            telefon_raqam()
        else:
            print("Bunday funksiya mavjud emas!")
    else:
        print("Parol xato kiritilgan!")
else:
    print("Iltimos Kartani kiriting yoki yoqoling:")