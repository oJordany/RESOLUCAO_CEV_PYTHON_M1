d012 = 'DESAFIO 014'
print('{:=^40}'.format(d012))
T = float(input('Informe a tempertura em °C: '))
# T/100 = (F - 32)/212 - 32
F = ((9 * T) + 160) / 5
print('{:.2f} °C equivale a {:.2f} °F'.format(T,F))
print('='*40)
# OBS.: Se eu numerar as máscaras, eu posso escolher qual variável vai aparecer em qual máscara
# Ex.: print('{2}...{0}...{1}'.format(T,F,d012)
# Ex.: print('d012...T...F'.format(T,F,d012)