d012 = 'DESAFIO 15'
print('{:=^40}'.format(d012))
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado
km = float(input('Quantos km o carro rodou?'))
d = int(input('por quantos dias o carro foi alugado?'))
print('O total a pagar pelo aluguel do carro é R${:.2f}'.format((km * 0.15)+(d * 60)))
print('=' * 40)