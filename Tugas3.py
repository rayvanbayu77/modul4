print("\n", "Kelompok 12 ".center(47, "="), "\n")
print("Daftar aksi", "\n")

Kode = {
 1: "Tarik Tunai",
 2: "Transfer",
 3: "Setor Tunai",
}

for x in Kode:
    print("(", x, ")", Kode[x])

print("\n")
userInput = int(input("Masukkan kode aksi yang ingin dilakukan: "))

if userInput == 1:
    print("Anda akan melakukan Tarik Tunai")
    tarikTunai = int(input("Masukkan nominal uang penarikan: "))
    konfirmasi = input("Konfirmasi tindakan (ketik \"y\" jika setuju, \"t\" untuk batal): ")
    if konfirmasi == "y":
        print("Penarikan senilai Rp.", tarikTunai, "berhasil !!!", "\n")
    elif konfirmasi == "t":
        print("Penarikan dibatalkan", "\n")
    else:
        print("Input tidak valid, silahkan coba kembali", "\n")
elif userInput == 2:
    print("Anda akan melakukan Transfer")
    tujuanTransfer= int(input("Masukkan nomor rekening tujuan: "))
    transfer = int(input("Masukkan nominal transfer: "))
    konfirmasi = input("Konfirmasi tindakan (ketik \"y\" jika setuju, \"t\" untuk batal): ")
    if konfirmasi == "y":
        print("Transfer senilai Rp.", transfer, "ke rekening", tujuanTransfer, "berhasil !!!", "\n")
    elif konfirmasi == "t":
        print("Transfer dibatalkan", "\n")
    else:
        print("Input tidak valid, silahkan coba kembali", "\n")
elif userInput == 3:
    print("Anda akan melakukan Setor Tunai")
    tujuanSetor = int(input("Masukkan nomor rekening tujuan: "))
    nominalSetor = int(input("Masukkan nominal transfer: "))
    print("Setor tunai Rp.", nominalSetor, "ke rekening", tujuanSetor)
    konfirmasi = input("Konfirmasi tindakan (ketik \"y\" jika setuju, \"t\" untuk batal): ")
    if konfirmasi == "y":
        print("Setor tunai senilai Rp.", nominalSetor, "ke rekening", tujuanSetor, "berhasil !!!", "\n")
    elif konfirmasi == "t":
        print("Setor tunai dibatalkan", "\n")
    else:
        print("Input tidak valid, silahkan coba kembali", "\n")
else:
    print("Kode item tidak terdaftar, silahkan pilih kode yang lain", "\n")


