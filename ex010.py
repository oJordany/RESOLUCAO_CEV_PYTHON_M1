d010 = 'DESAFIO 010'
c = 'SUA CARTEIRA'
print('{:=^40}'.format(d010))
print('SUA CARTEIRA')
v = float(input('Quanto você tem na sua carteira? R$'))
print('certo, com R${:.2f} você pode comprar US${:.2f}'.format(v, v/5.26))
print('='*40)