print('{:=^60}'.format('DESAFIO 029'))
vel = int(input('Qual a velocidade do carro em Km/h: ')) #usuário insere a sua velocidade
if vel > 80:
    print('Velocidade inadequada. \nSua multa será de R${:.2f}'.format((vel - 80) * 7)) #ultrapassou o limite de 80Km/h + mostrar o valor da sua multa
else:
    print('Velocidade adequada.') #velocidade adequada ao limite da via
print('Tenha um bom dia! Dirija com segurança')
print('='*60)