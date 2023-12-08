UserPassword = [
    ["cakboyo","pangerantampan"],["konoha","selaludihati"],["cakjukir","ahlinyaahli"]
]
bus_parking = []
car_parking = []
motorcycle_parking = []
pendapatan=0


def login(user,password) :
    for log in UserPassword:
        if log == [user,password]:
            return True
    return False
def percobaanlogin():
    stop = False
    percobaan = 0
    while (not stop):
        user=str(input("masukkan nama: "))
        password=str(input("masukkan password: "))
        if login(user,password):
            return True
            stop= True
        elif not login(user,password) and percobaan < 2 :
            print("login gagal coba lagi")
            percobaan += 1
        elif not login(user,password) and percobaan == 2:
            return False
            stop = True
def cektempatbus(x):
    for bus in bus_parking:
        if bus[1:] == x :
            return False
    return True
def ParkirBusUrut(plat):
    global bus_parking
    for huruf in range(ord('H'), ord('K')):
        for i in range(6):
            tempat=[chr(huruf),i]
            if cektempatbus(tempat):
                bus_parking.append([plat,chr(huruf),i])
                print("bus parkir di: lantai 3 ",chr(huruf),str(i) )
                return
    print("parkir bus penuh")
def cektempatmobil(x):
    for car in car_parking:
        if car[1:] == x:
            return False
    return True
def ParkirMobilUrut(plat):
    global car_parking
    for i in range(3,0,-1):
        if i == 3:
            for huruf in range(ord('A'),ord('H')):
                for j in range(6):
                    tempat=[i,chr(huruf),j]
                    if cektempatmobil(tempat):
                        car_parking.append([plat,i,chr(huruf),j])
                        print("mobil parkir di: lantai",i,chr(huruf),j )
                        return
        elif i == 2:
            for huruf in range(ord('D'),ord('K')):
                for j in range(9):
                    tempat=[i,chr(huruf),j]
                    if cektempatmobil(tempat):
                        car_parking.append([plat,i,chr(huruf),j])
                        print("mobil parkir di: lantai",i,chr(huruf),j )
                        return
        elif i == 1:
            for huruf in range(ord('A'),ord('K')):
                for j in range(3,9):
                    tempat=[i,chr(huruf),j]
                    if cektempatmobil(tempat):
                        car_parking.append([plat,i,chr(huruf),j])
                        print("mobil parkir di: lantai",i,chr(huruf),j )
                        return
    print("parkir mobil penuh")
def cektempatmotor(x):
    for motorcycle in motorcycle_parking:
        if motorcycle [1:] == x:
            return False
    return True
def ParkirMotorUrut(plat):
    global motorcycle_parking
    for i in range(1,4):
        if i == 1:
            for huruf in range(ord('A'),ord('K')):
                for j in range(4):
                    tempat=[i,chr(huruf),j]
                    if cektempatmotor(tempat):
                        motorcycle_parking.append([plat,i,chr(huruf),j])
                        print("motor parkir di: lantai",i,chr(huruf),j )
                        return
        elif i == 2:
            for huruf in range(ord('A'),ord('D')):
                for j in range(9):
                    tempat=[i,chr(huruf),j]
                    if cektempatmotor(tempat):
                        motorcycle_parking.append([plat,i,chr(huruf),j])
                        print("motor parkir di: lantai",i,chr(huruf),j )
                        return
        elif i == 3:
            for huruf in range(ord('A'),ord('k')):
                for j in range(6,9):
                    tempat=[i,chr(huruf),j]
                    if cektempatmotor(tempat):
                        motorcycle_parking.append([plat,i,chr(huruf),j])
                        print("motor parkir di: lantai",i,chr(huruf),j )
                        return
    print("parkir motor penuh")
def cekparkiranmotor():
    for i in range(1,4):
        if i == 1:
            for huruf in range(ord('A'),ord('K')):
                for j in range(4):
                    tempat=[i,chr(huruf),j]
                    if cektempatmotor(tempat):
                        print("tempat parkir untuk motor masih ada")
                        return
        elif i == 2:
            for huruf in range(ord('A'),ord('D')):
                for j in range(9):
                    tempat=[i,chr(huruf),j]
                    if cektempatmotor(tempat):
                        print("tempat parkir untuk motor masih ada")
                        return
        elif i == 3:
            for huruf in range(ord('A'),ord('k')):
                for j in range(6,9):
                    tempat=[i,chr(huruf),j]
                    if cektempatmotor(tempat):
                        print("tempat parkir untuk motor masih ada")
                        return
    print("parkir motor sudah penuh semua")
def cekparkiranmobil():
    for i in range(1,4):
        if i == 1:
            for huruf in range(ord('A'),ord('K')):
                for j in range(3,9):
                    tempat=[i,chr(huruf),j]
                    if cektempatmotor(tempat):
                        print("tempat parkir untuk mobil masih ada")
                        return
        elif i == 2:
            for huruf in range(ord('D'),ord('K')):
                for j in range(9):
                    tempat=[i,chr(huruf),j]
                    if cektempatmotor(tempat):
                        print("tempat parkir untuk mobil masih ada")
                        return
        elif i == 3:
            for huruf in range(ord('A'),ord('H')):
                for j in range(6):
                    tempat=[i,chr(huruf),j]
                    if cektempatmotor(tempat):
                        print("tempat parkir untuk mobil masih ada")
                        return
    print("parkir mobil sudah penuh semua")
def cekparkiranbus():
    for huruf in range(ord('H'), ord('K')):
        for i in range(6):
            tempat=[chr(huruf),i]
            if cektempatbus(tempat):
                print("tempat parkir untuk bus masih ada")
                return
    print("parkir bus sudah penuh semua")
def hitung(x):
    return len(x)
def cek():
    print("parkiran motor sudah terisi: ",str(hitung(motorcycle_parking)))
    cekparkiranmotor()
    print("parkiran mobil sudah terisi: ",str(hitung(car_parking)))
    cekparkiranmobil()
    print("parkiran bus sudah terisi: ",str(hitung(bus_parking)))
    cekparkiranbus()
def cari(plat):
    for bus in bus_parking:
        if bus[0] == plat:
            print("bus dengan nomor plat ditemukan pada berada di posisi: lantai 3 Huruf: ", bus[1], " nomor: ", bus[2])
            return
    for mobil in car_parking:
        if mobil[0] == plat:
            print("mobil dengan nomor plat ditemukan pada berada di posisi: lantai ",mobil[1] ," Huruf: ", mobil[2], " nomor: ", mobil[3])
            return
    for motor in motorcycle_parking:
        if motor[0] == plat:
            print("motor dengan nomor plat ditemukan pada berada di posisi: lantai ",motor[1] ," Huruf: ", motor[2], " nomor: ", motor[3])
            return
    print("plat nomor tidak terdaftar")
def mulai():
    global pendapatan
    stop=False
    while (not stop):
        print('''\
                sistem parkir boy
                       menu
                  1 parkir motor
                  2 parkir mobil
                  3 parkir bus
                  4 cek plat nomor
                  5 cek parkir
                  6 pendapatan hari ini
                       stop 
            ''')
        menu=(input("masukkan nomor menu: ")).lower()
        if menu == '1':
            print("__________________________________________")
            plat=input("masukkan plat nomor anda: ").upper()
            ParkirMotorUrut(plat)
            pendapatan += 2000
            print("__________________________________________")
        elif menu == '2':
            print("__________________________________________")
            plat=input("masukkan plat nomor anda: ").upper()
            ParkirMobilUrut(plat)
            pendapatan += 5000
            print("__________________________________________")
        elif menu == '3':
            print("__________________________________________")
            plat=input("masukkan plat nomor anda: ").upper()
            ParkirBusUrut(plat)
            pendapatan += 10000
            print("__________________________________________")
        elif menu == '4':
            print("__________________________________________")
            plat=input("masukkan plat nomor anda: ").upper()
            cari(plat)
            print("__________________________________________")
        elif menu == '5':
            print("__________________________________________")
            cek()
            print("__________________________________________")
        elif menu == '6':
            print("__________________________________________")
            print("pendapatan hari ini: ",str(pendapatan))
            print("__________________________________________")
        elif menu == 'stop':
            stop = True
def program():
    if percobaanlogin():
        print("login berhasil")
        mulai()
    else:
        print("login gagal") 
program()