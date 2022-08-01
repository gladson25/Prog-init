from random import shuffle
aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('Informe o numero do quarto aluno: ')
list = [aluno1, aluno2, aluno3, aluno4]
shuffle(list)
print(f'A sequencia de apresentação dos trabalhos será: {list}')