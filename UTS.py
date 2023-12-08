# bus_parking=[]

# bus_parking = []
# bus = [ 3, "H", 1]

# bus_parking.append(bus)

# print(bus_parking)

# def parking():
#     print (bus)

# plat=input("masukkan plat: ")

# parking()
# bus = [ 3, "H", 1]
# def parking(x):
#     bus.append(x)
#     print(bus)
# plat = input("masukkan plat: ")
# parking(plat) 
# def parking(x):
#     bus.insert(0, x)
#     bus_parking.append(bus.copy())
#     print(bus_parking)
bus_parking = [['AL 5657 BG', 'H', 1], ['AI 6178 YT', 'H', 0]]

def is_blok_terisi(blok, nomor):
    for mobil in bus_parking:
        print(mobil[1],str(mobil[2]))
        if mobil[1] == blok and mobil[2] == nomor:
            print("terisi")
            return True
    print("ini kosong")
    return False

def parkirbus(plat):
    for huruf in range(ord('H'), ord('J') + 1):
        huruf_str = chr(huruf)
        for angka in range(6):
            print("yang di cek",huruf_str,str(angka))
            if not is_blok_terisi(huruf_str, angka):
                bus_parking.append([plat, huruf_str, angka])
                print(f"Mobil dengan plat {plat} berhasil diparkir di blok {huruf_str}, nomor {angka}.")
                return  # Keluar dari fungsi setelah parkir berhasil

plat = "BG 5346 AZ"
parkirbus(plat)
print(bus_parking)



# def cekbus(plat):
#     for bus in bus_parking:
#         if plat in bus[0]:
#             return f"Plat nomor {plat} ditemukan di dalam blok {bus[1]}, nomor {bus[2]}."
#     return f"Plat nomor {plat} tidak ditemukan di dalam bus_parking."

# plat = input("Masukkan plat nomor yang ingin dicek: ")
# result = cekbus(plat)
# print(result)

# parking(plat)