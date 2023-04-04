#print (edificio [0])edificio = ["familia souza",
#            "fammilia brito",
#            "sr jorge",
#            "familia tanaka"]
#
#
#print (edificio [1])
#print (edificio [2])
#print (edificio [3])

notas = []
k = 1
while k <= 4:
    notas.append(float(input("nota: ")))
    k = k + 1
soma = k = 0
while k <= 3:
    soma = soma + notas[k]
    k = k + 1
print (f"media {notas} e {soma/4:.1f}")