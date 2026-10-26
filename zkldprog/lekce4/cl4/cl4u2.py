total=int(0)
for i,t in enumerate(range(1890,2030)): 
    if t%4==0:
        print(t)
        total +=1
print("pocet roku= ",total)
