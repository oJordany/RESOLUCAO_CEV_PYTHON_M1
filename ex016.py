from math import trunc
print('{:=^40}'.format('DESAFIO 016'))
num = float(input('insira um número real qualquer: '))
print('A parte inteiraa do número {} é {}'.format(num,trunc(num)))
print('='*40)
#ou
'''num2 = float(input('insira um número real qualquer: '))
print('A parte inteira do número {} é {}'.format(num,int(num2)))'''