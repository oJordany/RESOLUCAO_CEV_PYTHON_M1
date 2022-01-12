print('{:=^60}'.format('DESAFIO 023'))
'''num = str(input('Insira um número inteiro de 0 a 9999: '))
U = num[3]
D = num[2]
C = num[1]
M = num[0]
print('UNIDADE: {} \nDEZENA: {} \nCENTENA: {} \nMILHAR : {}'.format(U,D,C,M))'''
#nesse caso 1 ia ter que usar estrutura de repetição
#pois pode ser que o número não tenha os 4 dígitos
#Mas dá para fazer usando a forma matemática:
print('{:=^60}'.format('FORMA MATEMÁTICA'))
num = int(input('Insira um número de 0 a 9999: '))
u = (num//10**0)%10
d = (num//10**1)%10
c = (num//10**2)%10
m = (num//10**3)%10
print('UNIDADE: {} \nDEZENA: {} \nCENTENA: {} \nMILHAR: {}'.format(u,d,c,m))
print('='*60)