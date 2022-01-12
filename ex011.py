d011 = 'DESAFIO 011'
print('{:=^40}'.format(d011))
A = float(input('Digite a altura da parede em metros: '))
L = float(input('Digite a largura da parede em metros: '))
S = A * L
#Dado q 1L de tinta pinta 2 metros quadrados
T = S/2
print('a sua área é de {:.2f}, \npor isso, será necessário {:.2f} litros de tinta para pintar essa parede'.format(S,T))
print('='*40)