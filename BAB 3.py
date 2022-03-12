#Latihan ================== 1 . variabel dan tipe data ================================================

#1. Masukkan sebuah variabel dengan fungsi input dimana tipe data yang dimasukkan adalah tipe data integer lalu tampilkan.
#  Contoh: Input: 10
#  Expected Output : Nilai yang anda masukkan adalah 10

bil = int(input("Masukan Bilangan : "))

print("Nilai yang ada masukan adalah : ", bil)

#2. Buatlah sebuah list berisi 10 bilangan asli pertama. Hapus tiga elemen terakhir dan tambahkan bilangan 11 dan 12.

con_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

con_list.pop(7)
con_list.pop(8)
con_list.pop()

con_list.append(11)
con_list.append(12)

print(con_list)

#3. Buatlah sebuah dictionary dengan key berupa nama kelas dan valuenya berupa list yang berisikan nama siswa pada kelas tersebut.

dict_nama_kelas = {
    "kelas_06": "alfi",
    "kelas_08": "dani",
    "kelas_09": "alin",
}

print(dict_nama_kelas)

#4. Buatlah sebuah tuple yang berisikan dict yang memiliki key nama, kelas, dan umur.

tuple_coba = ({"nama": "alfi", "kelas": "12", "umur": "17 tahun"})

print(tuple_coba)

#5. Cobalah untuk merubah (casting) sebuah variabel pada nomor 2 menjadi tuple dan nomor 4 menjadi list.

#nomor 2 menjadi tuple menggunkan casting
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = tuple(angka)

print(data)

# #nomor 4 menjadi list menggunakn casting

list_coba1 = str(input("MASUKAN NAMA : "))
list_coba2 = str(input("MASUKAN KELAS : "))
list_coba3 = str(input("MASUKAN UMUR : "))

list_coba = [
    "Nama : ", list_coba1, "Kelas : ", list_coba2, "Umur : ", list_coba3,
    "tahun"
]

print(list_coba)