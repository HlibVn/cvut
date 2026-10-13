total = 0
for number in [3, -1, 4]:
    if number > 0:
        total += number
print(total)    


result = []
for x in [1,2,3]:
    result.append(x*2)
print(result)

re=[x*2 for x in [0,1,2,3,4] if x]
print(re)
