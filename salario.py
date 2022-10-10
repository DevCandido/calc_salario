valor_hora = float(input('Informe o quanto você ganha por hora: '))
horas_trabalhadas = int(input('Informe quantidade de horas trabalhadas no mês: '))
minutos_trabalhados = int(input('Informe quantidade de minutos trabalhados no mês: '))

minutos_decimal = round(minutos_trabalhados/60, 2)
salario_mes = round((horas_trabalhadas + minutos_decimal) * valor_hora, 2)
print()
print(f'O salario a receber é : R$ {salario_mes:.2f}')