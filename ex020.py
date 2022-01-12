print('{:=^60}'.format('DESAFIO 020'))
from random import shuffle
n1 = str(input('Insira o nome do(a) primeiro(a) aluno(a): '))
n2 = str(input('insira o nome do(a) segundo(a) aluno(a): '))
n3 = str(input('Insira o nome do(a) terceiro(a) aluno(a): '))
n4 = str(input('insira o nome do(a) quarto(a) aluno(a): '))
n = [n1, n2, n3, n4]
shuffle(n)
print('ordem de apresentação dos alunos: ', end = '')
print(n)
print('='*60)