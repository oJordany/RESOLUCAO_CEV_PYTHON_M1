print('{:=^60}'.format('DESAFIO 034'))
salário = float(input('Insira o seu salário atual em reais: R$'))
if salário <= 1250.00:
    print('O seu novo salário, com o aumento de 15%, será de : {:.2f}'.format((salário * 15/100) + salário))
else:
    print('O seu novo salário, com o aumento de 10%, será de : {:.2f}'.format((salário * 10/100) + salário))
print('='*60)
