a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

 
if a > b and a > c:
    print(f"entao o maior numero e o {a}")

if b > a and b > c:
     print(f"entao o maior numero e o {b}")

if c > b and c > a:
      print(f"entao o maior numero e o {c}")
 
if a < b and a < c:
    print(f"e o menor numero e o {a}")

if b < a and b < c:
     print(f"e o menor numero e o {b}")

if c < b and c < a:
      print(f"e o menor numero e o {c}")

elif a == b and b == c and c == a:
    print("todos sao iguais")