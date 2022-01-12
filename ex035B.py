print('{:=^60}'.format('DESAFIO 035 (RESOLUÇÃO GUANABARA)'))
print('{:=^60}'.format('ANALISADOR DE SEGMENTOS'))
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
print('='*60)
