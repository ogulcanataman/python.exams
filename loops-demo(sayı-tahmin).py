'''
* 1-100 arasında rastgele üretilecek bir sayıyı
  aşağı yukarı ile buldurmaya çalış
* "random modülü" için python random şeklinde arama yapın
* 100 üzerinden puanlama yap. Her cevap 20 puan
* Hak bilgisini kullanıcıdan al ve her cevap kullanıcı hakkından düşsün

'''

import random

sayi = random.randint(1,50)
can =int(input('kaç deneme yapmak istersin:'))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. denemede bildiniz. Puanınız: {100 - (100/can) * (sayac-1)}')
        break
    elif sayi > tahmin:
        print('YUKARI')
    else:
        print('AŞAĞI')

    if hak == 0:
        print(f'Hakkınız Bitti. Tutulan sayı: {sayi}')