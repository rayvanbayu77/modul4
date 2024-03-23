print("\n", "Kelompok 12 ".center(47, "="), "\n")
print("List items :", "\n")

Kode = {
 1: "11 diamonds",
 2: "55 diamonds",
 3: "165 diamonds",
 4: "275 diamonds",
 5: "565 diamonds",
 6: "1155 diamonds",
 7: "1765 diamonds",
 8: "2975 diamonds",
 9: "6000 diamonds",
 10: "Weekly Diamond pass",
}
Harga = {
 1: "3 ribu",
 2: "15 ribu",
 3: "45 ribu",
 4: "75 ribu",
 5: "149 ribu",
 6: "299 ribu",
 7: "439 ribu",
 8: "739 ribu",
 9: "1.5 juta",
 10: "29 ribu",
}

for x in Kode and Harga:
    print("(", x, ")", Kode[x], ":", Harga[x])

print("\n")
userInput = int(input("Masukkan kode item yang akan dibeli: "))

if userInput in Kode:
    print("Anda akan membeli %s" %Kode.setdefault(userInput), "dengan harga %s" %Harga.setdefault(userInput), "\n")
    konfirmasi = input("Konfirmasi pembelian (ketik \"y\" jika setuju, \"t\" untuk batal): ")
    if konfirmasi == "y":
            print("Pembelian %s" %Kode.setdefault(userInput), "berhasil !!!", "\n")
    elif konfirmasi == "t":
        print("Pembelian dibatalkan", "\n")
    else:
        print("Input tidak valid, silahkan coba kembali", "\n")
else:
    print("Kode item tidak terdaftar, silahkan pilih kode yang lain", "\n")


