# bus_parking = [["A 3756 BA", "H", 0], ["B 7891 SD", "H", 1],["D 12831 WQ", "H", 2]]

# def ParkirBusUrut(plat):
#     global bus_parking
#     for huruf in range(ord('H'), ord('K') + 1):
#         for i in range(6):
#             slot = [chr(huruf),i]
#             is_slot_empty = all(bus[1:] != slot for bus in bus_parking)
#             print(is_slot_empty)
#             if is_slot_empty:
#                 bus_parking.append([plat,chr(huruf),i])
#                 print(f"Bus {plat} parked in slot {slot}.")
#                 return
#     print("All parking slots are occupied.")
# def is_slot_empty(slot):
    # print("sebelum" ,slot)
    # for bus in bus_parking:
        # print(bus[1:])
        # if bus[1:] == slot:
            # print("yang fix",bus[1:])
            # return False
    # return True

# def ParkirBusUrut(plat):
    # global bus_parking
    # for huruf in range(ord('H'), ord('K') + 1):
        # for i in range(6):
            # slot = [chr(huruf),i]
            # if is_slot_empty(slot):
    #             print(is_slot_empty(slot))
    #             bus_parking.append([plat, chr(huruf),i])
    #             print(f"Bus {plat} parked in slot {slot}.")
    #             return
    # print("All parking slots are occupied.")
# Example usage:
# ParkirBusUrut("C 1234 EF")
# print(len(bus_parking))
# for bus in bus_parking:
#     print(bus)
bus_parking = [["A 3756 BA", "H", 0], ["B 7891 SD", "H", 1],["D 12831 WQ", "H", 2]]

nomor_plat_cari = "A 3756 BA"

# Loop melalui setiap elemen dalam bus_parking
for bus in bus_parking:
    if bus[0] == nomor_plat_cari:
        print("Nomor plat ditemukan pada berada di posisi: ", bus[1], " nomor: ", bus[2])
        break
else:
    print("Nomor plat tidak ditemukan dalam daftar.")
