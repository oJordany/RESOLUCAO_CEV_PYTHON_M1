d08 = 'DESAFIO 08'
print('{:=^40}'.format(d08))
v = float(input('digite um valor em metros: '))
print('='*40)
print('o valor {} em metros corresponde a {} em km, {} em hm, {} em dam, {} em dm, {} em cm e {} em mm'.format(v, v/1000, v/100, v/10, v*10, v*100, v*1000))
