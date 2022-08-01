algo = input('Digite algo: ')
print('O tipo primitivo deste valor é: ',type(algo))
print(f"""- O valor digitado é alfanumérico? {algo.isalnum()} 
- O valor digital é alfabético? {algo.isalpha()} 
- O valor digitado é numérico? {algo.isnumeric()}
- O valor só tem espaços? {algo.isspace()} 
- O valor está somente em maiúsculo? {algo.isupper()} 
- O valor está somente em minúsculo? {algo.islower()} 
- O valor está capitalizado? {algo.istitle()}
- O Valor é um decimal? {algo.isdecimal()} """)