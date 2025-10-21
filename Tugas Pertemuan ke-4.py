print(7*"=" + "Program hitung Gaji Karyawam" + "="*7)

nama_karyawan = input("Nama Karyawan  \t : ")
golongan_jabatan = input("Golongan Jabatan : ")
pendidikan = input("Pendidikan  \t : ")
jumlah_jamkerja = int(input("Jumlah Jam Kerja : "))

gaji_pokok = 300000

if golongan_jabatan == "1":
    tunjangan_j = 0.05
elif golongan_jabatan == "2":
    tunjangan_j = 0.10
elif golongan_jabatan == "3":
    tunjangan_j = 0.15
else:
    tunjangan_j = 0

TJ = gaji_pokok * tunjangan_j

if pendidikan.upper() == "SMA":
    tunjangan_p = 0.025
elif pendidikan.upper() == "D1":
    tunjangan_p = 0.05
elif pendidikan.upper() == "D3":
    tunjangan_p = 0.20
elif pendidikan.upper() == "S1":
    tunjangan_p = 0.30
else:
    tunjangan_p = 0

TP = gaji_pokok * tunjangan_p

if jumlah_jamkerja > 8:
    lembur = (jumlah_jamkerja - 8) * 3500
else:
    lembur = 0

total_gaji = gaji_pokok + TP + TJ + lembur

print(42*"=") 
print(f"Karyawan yang bernama : {nama_karyawan}")
print(f"""Honor yang diterima :
      Tunjangan Jabatan    : Rp {TJ:,}
      Tunjangan Pendidikan : Rp {TP:,}
      Honor lembur         : Rp {lembur:,}""")
print(f"total gaji adalah : Rp {total_gaji:,}")
print(42*"=") 
