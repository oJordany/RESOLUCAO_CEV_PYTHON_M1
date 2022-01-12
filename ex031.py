print('{:=^60}'.format('DESAFIO 031'))
d = float(input('Insira a distância da sua viagem em Km: '))
if d > 200:
    print('O preço da sua viagem será de R${:.2f}'.format(0.45 * d))
else:
    print('O preço da sua viagem será de R${:.2f}'.format(0.50 * d))
print('='*60)
#ou
print('{:^60}'.format('FORMA DE IF IN LINE'))
d = float(input('Insira a distância da sua viagem em Km: '))
preço = d * 0.50 if d <= 200 else d * 0.45
print('O preço da sua viagem será de R${:.2f}'.format(preço))
print('='*60)