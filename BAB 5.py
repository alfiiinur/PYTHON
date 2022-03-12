#==================== 3. PERCABANGAN ========================

#1. 1. Tampilkan "Waktunya makan" jika belum makan, lapar, dan sudah jam 7 malam atau lebih. Tampilkan "Sebentar lagi"
# jika yang sebelumnya tidak terpenuhi, belum makan, lapar, dan jam di antara 5 sampai 7 malam. Jika yang sebelumnya
# tidak terpenuhi, tampilkan "Belum waktunya"

bil = int(input("MASUKKAN JAM: "))
if bil == 17 or 18:
    if bil == 19:
        print("JAM", bil, "WAKTUNYA MAKAN")
        lapar = True
        print("USER LAPAR = ", lapar)
    else:
        print("JAM", bil, "BELUM MAKAN")
        lapar = True
        print("USER LAPAR = ", lapar)
else:
    print("JAM", "BELUM WAKTUNYA MAKAN")
    lapar = False
    print(lapar)

#2. Bisakah kode pada nomor pertama dibuat lebih sederhana menggunakan nested if?
