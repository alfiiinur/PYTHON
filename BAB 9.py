################## 7. FUNCTIONAL PROGRAMING ##########################
#1. Buatlah sebuah list yang berisi kumpulan tahun, lalu filter list tersebut untuk mengambil daftar tahun kabisat. (List Comprehension)
tahun = [
    2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021
]

filter_tahun = [x for x in tahun if x % 4 == 0]

print(filter_tahun)

# list2 = [x for x in tahun]
# print(list2)

#2. Buatlah sebuah inputan bilangan bulat, lalu tampilkan nilai faktorial bilangan tersebut. (Recursive)

n = int(input('Masukkan nilai n: '))


def hitung_faktorial(n):
    if n > 2:
        return n * hitung_faktorial(n - 1)

    return 2


faktorial = hitung_faktorial(n)
print(f'{n}! = {faktorial}')

#3. Buatlah sebuah dictionary dengan atribut nama, hobi, umur, dan status. Lalu tampilkan pada sebuah fungsi. (Packing Argument)


def data(nama, hobi, umur, status):
    print(f"{nama},{hobi},{umur}tahun,{status}")


my_data = ["alfi", "makan", 21, "mahasiswa"]
my_data1 = ["alfi", "makan", 21, "mahasiswa"]
data(*my_data)
data(*my_data)
