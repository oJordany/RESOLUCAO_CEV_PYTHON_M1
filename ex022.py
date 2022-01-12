print('{:=^60}'.format('DESAFIO 022'))
nome = str(input('Insira o seu nome completo: ')).strip()#o .strip elimina os espaços excedentes nas bordas
print('O seu nome em letras maiúsculas é: ', nome.upper())
print('O seu nome em letras minúsculas é: ', nome.lower())
print('O seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' '))) #aqui ele mostra a casa em que está o primeiro espaço
separador = nome.split()
#ou pode fazer assim:
print('O seu primeiro nome é {} e tem {} letras'.format(separador[0],len(separador[0])))
print('='*60)