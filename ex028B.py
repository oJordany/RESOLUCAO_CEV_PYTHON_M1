print('{:=^60}'.format('DESAFIO 028B (RESOLÇÃO GUANABARA)'))
print('{:-^60}'.format('JOGO DA ADIVINHAÇÃO'))
from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "PENSAR"
print("-=-" *20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
print("-=-"*20)
if computador == jogador:
    print('PARABÉNS! VOCÊ CONSEGUIU ME VENCER!')
else:
    print('GANHEI, EU PENSEI NO NÚMERO {} E NÃO NO {}'.format(computador, jogador))
print('='*60)
