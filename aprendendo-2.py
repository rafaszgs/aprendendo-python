ano = int(input("qual e seu ano seu ano?"))

if ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0:
    print ("seu ano e bissexto")
    
else:
    print ("seu ano e normal")