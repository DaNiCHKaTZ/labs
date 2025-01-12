import re
print("")
six_number = r'^[1-9]\d{5}$'

number=input()
if re.match(six_number, number):
   print(True)
else:
    print(False)
