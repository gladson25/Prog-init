kperc = float(input('Informe a quantidade de KM percorrido: '))
dias = int(input('Informe quantidade de dias locados: '))
print(f"""O valor a pagar:
 - Total:  R$ {(dias * 60) + (kperc * 0.15)}
 """)