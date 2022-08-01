vcart = float(input('Informe o valor em carteira em R$: '))
vdolar = float(input('Valor do dólar hoje: '))
print(f"""O valor em carteira em R$ é: {vcart}
O valor do dólar hoje: USD {vdolar}
Valor em dólar que pode ser comprado: USD {vcart/vdolar}.""")