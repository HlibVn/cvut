#Hřídel má jmenovitý průměr 25,00 mm s tolerancí ±0,05 mm. Naměřené průměry deseti kusů máte v programu:
w=0
total=0
diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
for i,d in enumerate(diameters, start=1):
    if 24.95<=d<=25.05:
        print(i,": ",d,"mm OK")
        total +=1
    elif d<24.95: 
            print(i,": ",d,"mm MALY")
            w+=1
            total +=1
    else:
            print(i,": ",d,"mm VELKY") 
            w+=1
            total +=1

zm=(w/total)*100
print("Zmetku: ", w ," z ",total,"(",float(zm),"%)")