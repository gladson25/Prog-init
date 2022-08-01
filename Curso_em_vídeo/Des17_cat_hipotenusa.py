from math import hypot
catop = float(input('Informe o valor do cateto oposto: '))
catadj = float(input('Informe o valor do cateto adjacente: '))
print(f'A hipotenusa dos catetos oposto: {catop} | adjacente: {catadj} é: {(catop ** 2 + catadj ** 2) ** (1/2)} - Fazendo o cálculo na mão!')
print(f'A hipotenusa dos catetos oposto: {catop} | adjacente: {catadj} é: {hypot(catop, catadj)} - Usando módulo hypot / math!')