def normalize(birth_number):
    s = birth_number.replace("/", "").replace(" ", "")
    if len(s) == 10 and s.isdigit():
        return s
    return None
def is_valid(birth_number):
    s = normalize(birth_number)
    if s is None:
        return False
    if int(s) % 11 != 0:
        return False
    month = int(s[2:4])
    if month > 50:
        month -= 50
    return 1 <= month <= 12
def gender(birth_number):
    s = normalize(birth_number)
    month = int(s[2:4])
    return "žena" if month > 50 else "muž"
def birth_date(birth_number):
    s = normalize(birth_number)
    yy = int(s[0:2])
    month = int(s[2:4])
    day = int(s[4:6])
    if month > 50:
        month -= 50
    year = 2000 + yy if yy <= 53 else 1900 + yy
    return f"{day}. {month}. {year}"
for rc in ["736028/5163", "990101/1230", "736028/5164"]:
    if is_valid(rc):
        print(rc, "-> platné,", gender(rc) + ",", birth_date(rc))
    else:
        print(rc, "-> neplatné")