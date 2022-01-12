print('{:=^60}'.format('DESAFIO 019'))
from random import choice
n1 = str(input('digite o nome do 1o. aluno: '))
n2 = str(input('digite o nome do 2o. aluno: '))
n3 = str(input('digite o nome do 3o. aluno: '))
n4 = str(input('digite o nome do 4o. aluno: '))
n = [n1,n2,n3,n4]
print('o(a) aluno(a) escolhido(a) para apagar o quadro foi: {}'.format(choice(n)))
print('='*60)
#random.choice -> escolhe um valor