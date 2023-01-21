salario = int(input("quanto vc ganha por hora?"))
horario = int(input("quantas horas vc trabalha por mes?"))
salarioBruto = salario * horario
impostos = salarioBruto * 0.24
salarioLiquido = salarioBruto - impostos

print (f"seu salario bruto e de {salarioBruto:.2f} ")

print (f"o valor dos impostos {impostos:.2f}")

print (f"seu salario líquido e de {salarioLiquido:.2f} ")