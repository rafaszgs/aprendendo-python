m = '''janeiro fevereiro marco abril maio junho julho agosto setembro outubro novembro dezembro'''.split()
d,m,a=input(' dd/mm/aaaa: ').split("/")

naoPassarPelosTestes = True
while naoPassarPelosTestes == False:
   if m == 2:
    if d <= 28:
     print (f"hoje e dia {d} de {m} de {a}")

   if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    if d <= 31:
     print (f"hoje e dia {d} de {m} de {a}")

   if m == 4 or m == 6 or m == 9 or m == 11:
    if d <= 30:
     print (f"hoje e dia {d} de {m} de {a}")


print(f'{d} de {m[int(m)-1]} de {a}') 