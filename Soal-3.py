print("Cek Status Kelulusan Ujian")
print("===========================")
print(" ")
print("Masukkan data Anda!")
nama = str(input("Nama: "))
nilai_teori = float(input("Nilai Ujian Teori: "))
nilai_praktek = float(input("Nilai Ujian Praktek: "))
print(" ")
print("Status:")
if nilai_teori >= 70 and nilai_praktek >= 70:
    print("Selamat, Anda lulus!")
elif nilai_teori >= 70 and nilai_praktek < 70:
    print("Anda harus mengulang ujian praktek!")
elif nilai_teori < 70 and nilai_praktek >= 70:
    print("Anda harus mengulang ujian teori!")
else:
    print("Anda harus mengulang ujian teori dan praktek!")
print(" ")
print("===========================")