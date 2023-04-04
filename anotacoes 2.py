#print (f"{x} x {n} = {x * x }")
#   x = x + 1
 
t = int(input(f"numero: "))
n = 1

while t <= 10:
    print (f"tabuada do {t}")
    n = 1

    while n <= 10:
       print (f"{n} x {t} = {n * t}")
       n = n + 1
    t = t + t
    print ()
    print ()
    print ()
    print ()