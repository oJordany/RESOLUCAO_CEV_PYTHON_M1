print('{:=^60}'.format('DESAFIO 024'))
city = str(input('insira o nome de uma cidade: ')).upper().strip()
print('A sua cidade tem "Santo" no nome? {}'.format('SANTO' in city))
#ou
print(city[:5] == 'SANTO')
print('='*60)