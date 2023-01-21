ano = int(input("qual e seu ano seu ano?"))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("seu ano e um ano bisexto")
        else:
            print("seu ano e um ano normal")
    else:
        print("seu ano e um ano bisexto")
else:
    print("seu ano e um ano normal")
