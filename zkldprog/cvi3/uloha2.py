
sek = int(input("sekundy: "))
d = sek // 86400
zb = sek % 86400
hod = zb // 3600
min = (zb % 3600) // 60
sek = zb % 60
if d > 0:
    print(f"{d} d {hod}:{min:02d}:{sek:02d}")
else:
    print(f"{hod}:{min:02d}:{sek:02d}")
