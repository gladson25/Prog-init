import math
angulo = float(input('Informe o ângulo desejado para saber o [Seno | Cosseno | Tangente]: '))
print(f"""O ângulo digitado foi: {angulo}:
- O Seno: {math.sin(math.radians(angulo)):.2f}
- O Consseno: {math.cos(math.radians(angulo)):.2f}
- A Tangente: {math.tan(math.radians(angulo)):.2f}""")