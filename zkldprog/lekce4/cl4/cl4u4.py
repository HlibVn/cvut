while True:
    n=int(input("Vyska= "))
    if n>0 and n%2==1:
        break
    print("zadejte kladne liche čislo")
s=n//2
for i in range(n):
    d=abs(i-s)
    print(" " * d + "*" * (n - 2 * d))
    