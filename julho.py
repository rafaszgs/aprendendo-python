velocidade = int(input('com quantos quilometros seu carro passou no medidor?'))
if velocidade > 110:
    multa = (velocidade - 110) * 5
    print (f'voce ganhou uma multa de {multa:.2f}')
if velocidade <= 110:
    print ('ok obrigado pela atencao')