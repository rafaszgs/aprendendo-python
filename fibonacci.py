a = 1
b = 1
c = int(input(""))
while a < 17:
    print (a)
    print (b)
    a = a + b
    b = b + a
if b < a:
    print (b)
print (f"esse e o seu numero de fibonacci")