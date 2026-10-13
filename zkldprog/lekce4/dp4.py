count=0
max=None
while True:
    line= input("cislo = (Enter = konec)")
    if line == "":
        break
    num=int(line)
    count +=1
    if max == None or num > max:
        max = num
if count == 0:
    print("Nebylo zadane zadne cislo")
else:
    print("max=",max," count=",count)