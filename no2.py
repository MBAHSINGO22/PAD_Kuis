# Blok ini berfungsi untuk apa ?
# mengambil input dari pengguna, memisahkan input tersebut berdasarkan spasi, 
# dan mengubah setiap elemen yang dipisahkan menjadi integer.
data = input("Masukkan dataset (pisahkan dengan spasi): ")
data = data.split()
data = [int(x) for x in data]

# Blok ini berfungsi untuk apa ?
# menghitung frekuensi dari setiap nilai dalam list data. 
# Ini dilakukan dengan menggunakan sebuah dictionary freq_dict di mana kunci adalah nilai dari list data,
# dan nilai adalah jumlah kemunculan dari nilai tersebut dalam list.
freq_dict = {}
for val in data:
    if val in freq_dict:
        freq_dict[val] += 1
    else:
        freq_dict[val] = 1

# Blok ini berfungsi untuk apa ?
# mencari nilai (modus) yang paling sering muncul dalam dataset yang telah dianalisis sebelumnya. 
# Ini dilakukan dengan menggunakan dictionary freq_dict yang berisi frekuensi dari setiap nilai dalam dataset.
max_freq = 0
for val in freq_dict:
    if freq_dict[val] > max_freq:
        max_freq = freq_dict[val]
        mode = val

data.sort()
# Mencetak data yang telah diurutkan
print("Data yang terurut:", data)

# Mencetak nilai yang paling sering muncul (modus) dan jumlah kemunculannya
print("Nilai yang paling sering muncul (mode):", mode)
print("Jumlah kemunculan mode:", max_freq)
