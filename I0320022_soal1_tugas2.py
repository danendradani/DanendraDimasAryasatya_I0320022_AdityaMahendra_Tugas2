#menampilkan informasi program
print("Menghitung Luas Persegi Panjang, Lingkaran, Kubus, dan Konversi Suhu Reamur ke Kelvin")
print("---------------------------------------------------------------------------------------")

#menampilkan informasi program
print("Luas Persegi Panjang")

#input nilai panjang dan lebar persegi panjang
panjang = float(input("Panjang persegi panjang : "))
lebar = float(input("Lebar persegi panjang : "))

#menghitung luas persegi panjang
luas_persegi_panjang = panjang * lebar

#menampilkan hasil perhitungan
print("Luas persegi panjang : ", luas_persegi_panjang)
print("---------------------------------------------")

#menampilkan informasi program
print("Luas Lingkaran")

#input nilai jari-jari lingkaran
r = float(input("Jari-jari lingkaran : "))

#menghitung luas lingkaran
luas_lingkaran = 3.14 * (r ** 2)

#menampilkan hasil perhitungan
print("Luas Lingkaran : ", luas_lingkaran)
print("---------------------------------------------")

#menampilkan informasi program
print("Luas Kubus")

#input nilai sisi kubus
s = float(input("Sisi kubus : "))

#menghitung luas kubus
luas_kubus = 6 * (s ** 2)

#menampilkan hasil perhitungan
print("Luas kubus : ", luas_kubus)
print("---------------------------------------------")

#menampilkan informasi program
print("Konversi Suhu Reamur ke Kelvin")

#input nilai suhu reamur
r = float(input("Suhu dalam reamur : "))

#konversi suhu ke celcius
c = 5/4 * r

#konversi suhu ke kelvin
k = c +273

#menampilkan hasil perhitungan
print("Suhu dalam kelvin : ", k)
print("---------------------------------------------")