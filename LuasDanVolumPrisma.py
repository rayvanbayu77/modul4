import math
print("\n","Rayvan Bayu Abhinowo_21120123130053_Kelompok12_Shift2" )
print("Bambang Irawan_21120123120011_Kelompok12_Shift2")
print("Naufal Abdullah Kafa Bihi_21120122120032_Kelompok12_Shift2")
print("Muhammad Arif Maulana_21120123130111_Kelompok12_Shift2", "\n")


panjang = 20
lebar = 8
tinggi = 4
a = (lebar/2)**2
b = tinggi**2
sisi_miring = math.sqrt(a+b)
luas_permukaan = 2*(lebar*tinggi/2) + sisi_miring*panjang*2 + lebar*panjang
volume = panjang*lebar*tinggi/2

print("Luas permukaan prisma : ", luas_permukaan, 'cm^2')
print('Volume prisma :', volume, 'cm^3', "\n")