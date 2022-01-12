print('{:=^60}'.format('DESAFIO 033'))
n1 = float(input('Digite o 1 o. número: '))
n2 = float(input('Digite o 2 o. número: '))
n3 = float(input('Digite o 3 o. número: '))
#verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número entre os três é : {}'.format(maior))
print('O menor número entre os três é : {}'.format(menor))
print('='*60)