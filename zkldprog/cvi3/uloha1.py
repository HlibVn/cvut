delka = float(input('Delka(mm) = '))

cm= delka/10
m= delka/1000
inch= delka/25.4
#print(inch)
print(f"{delka:.3f}mm = {cm:.3f}cm =  {m:.3f}m = {inch:.3f}in")