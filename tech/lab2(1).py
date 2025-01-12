def ravnobed(a,b,c):
    return a == b or b == c or a == c

lam_function = lambda a , b, c: a == b or a == c or b == c

a = int(input("Enter a = ",))
b = int(input("Enter b = ",))
c = int(input("Enter c = ",))

if a == b or b == c or a == c:
    d = True
else:
    d = False

print (d)
print(ravnobed(a, b, c))
print(lam_function(a, b, c))