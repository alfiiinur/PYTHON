############ 4. PERULANGAN ============

# 1. Buatlah sebuah input sebagai batas akhir sebuah perulangan (misal: 20),
# lalu tampilkan bilangan dari 1 sampai bilangan ke-n tersebut. Namun jika bilangan
# berkelipatan 3, cetak kata Fizz . Jika bilangan berkelipatan 5, cetak kata Buzz. Dan jika bilangan berkelipatan 3 dan 5, cetak kata Fizz Buzz.

#2. Buatlah sebuah inputan bilangan, lalu tampilkan seperti berikut, menggunakan nested loop.

#3. Buatlah sebuah inputan bilangan, lalu tampilkan seperti berikut menggunakan nested loop.

#
string = ""

x = int(input("Masukkan angka :"))
bar = x
# Looping Baris
while bar >= 0:
    # Looping Kolom Spasi Kosong
    kol = bar
    while kol > 0:
        string = string + "   "
        kol = kol - 1
    # Looping Kolom Bintang Sisi Kiri
    kiri = 1
    while kiri < (x - (bar - 1)):
        string = string + " * "
        kiri = kiri + 1
    # Looping Kolom Bintang Sisi Kanan
    kanan = 1
    while kanan < kiri - 1:
        string = string + " * "
        kanan = kanan + 1

    string = string + "\n"
    bar = bar - 1

print(string)