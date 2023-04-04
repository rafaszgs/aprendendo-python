#a = int(input("qual e o seu primeiro numero?: "))
#b = int(input("qual e o seu segundo numero?: "))
# c = 2
#d = 2
#e = 
#f = False
#g = False

#while a != 1 and b != 1:
#    if a%c == 0:
#        a = a / c
#    else:
#        c = c + 1
#    if b%d == 0:    
#        b = b / d
#    else:
#        d = d + 1

#print (f"o mdc de {a} e de {b} e {c}") 

a = int(input("qual e o seu primeiro numero?: "))
b = int(input("qual e o seu segundo numero?: "))
while a % b != 0:
    a, b = b, a%b
print (f"o mdc e {b}") 