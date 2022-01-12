d09 = 'DESAFIO 009'
print('{:=^60}'.format(d09))
n = int(input('digite um número inteiro qualquer para ver a sua tabuada: '))
print('{:=^60}'.format('TABUADA DO {}'.format(n)))
c = int(1)
for c in range(1, 11):
    print('{} X {:2} = {}'.format(n, c, n*c))
    print('='*60)
print('='*60)