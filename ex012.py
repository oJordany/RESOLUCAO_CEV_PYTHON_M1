d012 = 'DESAFIO 012'
#faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto
print('{:=^40}'.format(d012))
p = float(input('Digite o preço do produto: R$'))
d = float(p*5/100)
print('O novo preço do produto, com o desconto de 5%, será R${:.2f}'.format(p-d))
print('='*40)