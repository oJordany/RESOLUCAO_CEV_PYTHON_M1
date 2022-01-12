from math import sqrt, pow, hypot
print('{:=^50}'.format('DESAFIO 017'))
c1 = float(input('insira o valor do primeiro cateto do triângulo retângulo: '))
c2 = float(input('insira o valor do segundo cateto do triângulo retângulo: '))
print('o valor da hipotenusa desse triângulo retângulo é: {:.2f}'.format(sqrt(pow(c1,2)+pow(c2,2))))
print('='*50)
#ou
c11 = float(input('insira o valor do primeiro cateto do triângulo retângulo: '))
c22 = float(input('insira o valor do segundo cateto do triângulo retângulo: '))
print('o valor da hipotenusa desse triângulo retângulo é: {:.2f}'.format(hypot(c11, c22)))