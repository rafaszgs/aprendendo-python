a = int(input('a'))
b = int(input('b'))
c = int(input('c'))

if a == b and b != c:
    print ("entao seu triangulo e un triangulo isoceles!")

if a == b and b == c:
    print ("entao seu triangulo e um triangulo equilatero!")

if a != b and b != c and a != c:
    print ("entao seu triangulo e um triangulo escaleno!")

else:
    print ("entao seu triangulo e un triangulo isoceles!")
