#=============== 2.  aritmatika ======================

#1 .Cobalah melakukan operasi aritmatika menggunakan contoh soal diatas, lakukan dengan operator yang ada diatas
#OPERTAOR ARITMATIKA
#PENJUMLAHAN
X = 10
Y = 15
jumlah = X + Y
print(jumlah)

# #PENGURANGAN
X = 10
Y = 15
jumlah = X - Y
print(jumlah)

# #PERKALIAN
X = 10
Y = 15
jumlah = X * Y
print(jumlah)
# #PEMBAGIAN
X = 10
Y = 15
jumlah = X / Y
print(jumlah)
# #MODULO
X = 10
Y = 15
jumlah = X % Y
print(jumlah)
# #PANGKAT
X = 10
Y = 15
jumlah = X**Y
print(jumlah)
# #PEMBAGIAN BULAT
X = 10
Y = 15
jumlah = X // Y
print(jumlah)

#2. Buatlah 2 input program yang terdiri atas bilangan bulat dan bilangan pangkat, misal Bilangan 1 = 10 dan Bilangan 2 = 3 maka outputnya adalah 10 pangkat 3 = 1000.

bil1 = int(input("MASUKKAN BILANGAN = "))
bil2 = int(input("MASUKKAN PANGKAT BILANGAN = "))

hasil = bil1**bil2
print("MAKA HASIL DARI BILANGAN ", bil1, "DAN PANGKAT", bil2, "ADALAH = ",
      hasil)

#3.Buatlah sebuah inputan tahun yang terdiri dari 4 digit, jika inputan tersebut berkelipatan 4, maka cetak Bilangan tersebut adalah tahun kabisat.

bil = int(input("MASUKKAN BILANGAN 4 DIGITS = "))

if bil % 4 == 0:
    print("TAHUN KABISAT ")
else:
    print("BUKAN TAHUN KABISAT")
