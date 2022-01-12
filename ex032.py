print('{:=^60}'.format('DESAFIO 032'))
print('{:-^60}'.format('VERIFICADOR DE ANO BISSEXTO'))
from datetime import date #boblioteca para importar o ano atual
ano = int(input('Que ano vc quer analisar? (Coloque 0 para analisar o ano atual):'))
if ano == 0: #condicional simples para quando o usuário quiser o ano atual
    ano = date.today().year #ano recebe apenas o ano da data de hoje
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 : # equação completa para saber se um ano é bissexto
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
print('='*60)