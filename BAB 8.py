################## 6. TUPPLE AND LIST ####################

#1. Buat tuple berisi 10 angka acak.
bil = (1, 3, 5, 2, 7, 4, 6, 8, 10, 9)

#2. Urutkan tuple tersebut dan simpan ke dalam variabel tuple yang baru.
bil_baru = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#3. Ambil elemen-elemen dari tuple tersebut yang memiliki indeks ganjil dan masukkan ke variabel baru.
bil_ganjil = (1, 3, 5, 7, 9)

#4. Buat sebuah set dan list berisi 5 elemen berbeda.
bil_set = {1, "alfi", 2.2, False, 20}

bil_list = [1, "alfi", 2.2, False, 20]

#5. Apa yang akan terjadi jika kita menambahkan elemen yang sudah ada ke dalam set?
bil_set = {1, "alfi", 2.2, False, 20}

bil_set.add("nur")
print(bil_set)

#6. Apa yang akan terjadi jika kita menambahkan elemen yang sudah ada ke dalam list?
bil_list = [1, "alfi", 2.2, False, 20]

bil_list.append("nur")
print(bil_list)
