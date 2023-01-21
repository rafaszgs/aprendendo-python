a = int(input("Primeiro valor: "))
b = int(input("segundo valor "))
c = int(input("terceiro valor "))
if c > a and c > b:
     print (f'o maior numero e {c}')
if a > b and a > c:
     print (f"o maior numero e {a}")
if b > a and b > c:
     print (f"o maior numero e {b}")
if b == a and b == c:
     print (f"todos os numeros sao iguais")
