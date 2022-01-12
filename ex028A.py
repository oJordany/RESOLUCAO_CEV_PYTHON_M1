print('{:=^60}'.format('DESAFIO 028'))
print('{:-^60}'.format('JOGO DA ADIVINHAÇÃO'))
from random import randint
from time import sleep
num = randint(0,5)
nuser = int(input('Tente acertar o número que eu estou pensando... \nDigite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if nuser == num:
    print('PARABÉNS, VOCÊ ACERTOU O NÚMERO! :)')
else:
    print('VOCÊ ERROU O NÚMERO :(')
    print('EU PENSEI NO NÚMERO {} E NÃO NO {}'.format(num, nuser))
print('='*60)