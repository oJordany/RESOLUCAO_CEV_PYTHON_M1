print('{:=^60}'.format('DESAFIO 030'))
num = int(input('Digite um número inteiro qualquer: '))
if num == 0 :
    print('0 é nulo')
else:
    if num %2 == 0 :
        print('Esse número é par')
    else:
        print('Esse número é ímpar')
if num < 0:
    print('Esse número é negativo')
else:
    if num == 0:
        print('0 não é negativo nem positivo, é nulo')
    else:
        print('Esse número é positivo')
print('='*60)
