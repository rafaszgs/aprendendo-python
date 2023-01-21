tempo = int(input('quantos minutos vc ficou no telefone?'))
if tempo < 200:
    minutos = tempo * 0.20
elif tempo <= 400:
    minutos = tempo * 0.18
elif tempo <= 800:
    minutos = tempo * 0.15
else: 
    minutos = tempo * 0.08
print(f'voce foi cobrado em {minutos:.2f}')