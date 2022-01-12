print('{:=^60}'.format('DESAFIO 035'))
print('{:-^60}'.format('VERIFICADOR DE TRIÂNGULOS'))
print('ATENÇÃO: DIGITE O VALOR DAS RETAS EM UMA ÚNICA UNIDADE DE \nCOMPRIMENTO')
r1 = float(input('Insira o comprimento de uma reta qualquer: '))
r2 = float(input('Insira o comprimento de outra reta qualquer: '))
r3 = float(input('Insira o comprimento de mais outra reta qualquer: '))
if r1 >= r2 and r2 >= r3 and r1 >= r3 :
    if r1 + r2 > r3 and r1 - r2 < r3 and r2 + r3 > r1 and r2 - r3 < r1 and r3 + r1 > r2 and r1 - r3 < r2:
        print('Essas retas podem formar um triângulo')
    else:
        print('Essas retas não podem formar um triângulo')
else:
    if r1 >= r2 and r2 >= r3 and r3 >= r1 :
        if r1 + r2 > r3 and r1 - r2 < r3 and r2 + r3 > r1 and r2 - r3 < r1 and r3 + r1 > r2 and r3 - r1 < r2:
            print('Essas retas podem formar um triângulo')
        else:
            print('Essas retas não podem formar um triângulo')
    else:
        if r1 >= r2 and r3 >= r2 and r1 >= r3:
            if r1 + r2 > r3 and r1 - r2 < r3 and r2 + r3 > r1 and r3 - r2 < r1 and r3 + r1 > r2 and r1 - r3 < r2:
                print('Essas retas podem formar um triângulo')
            else:
                print('Essas retas não podem formar um triângulo')
        else:
            if r1 >= r2 and r2 >= r3 and r1 >= r3 :
                if r1 + r2 > r3 and r1 - r2 < r3 and r2 + r3 > r1 and r2 - r3 < r1 and r3 + r1 > r2 and r1 - r3 < r2:
                    print('Essas retas podem formar um triângulo')
                else:
                    print('Essas retas não podem formar um triângulo')
            else:
                if r1 >= r2 and r3 >= r2 and r3 >= r1 :
                    if r1 + r2 > r3 and r1 - r2 < r3 and r2 + r3 > r1 and r3 - r2 < r1 and r3 + r1 > r2 and r3 - r1 < r2:
                        print('Essas retas podem formar um triângulo')
                    else:
                        print('Essas retas não podem formar um triângulo')
                else:
                    if r2 >= r1 and r2 >= r3 and r1 >= r3 :
                        if r1 + r2 > r3 and r2 - r1 < r3 and r2 + r3 > r1 and r2 - r3 < r1 and r3 + r1 > r2 and r1 - r3 < r2:
                            print('Essas retas podem formar um triângulo')
                        else:
                            print('Essas retas não podem formar um triângulo')
                    else:
                        if r2 >= r1 and r2 >= r3 and r3 >= r1:
                            if r1 + r2 > r3 and r2 - r1 < r3 and r2 + r3 > r1 and r2 - r3 < r1 and r3 + r1 > r2 and r3 - r1 < r2:
                                print('Essas retas podem formar um triângulo')
                            else:
                                print('Essas retas não podem formar um triângulo')
                        else:
                            if r2 >= r1 and r3 >= r2 and r1 >= r3 :
                                if r1 + r2 > r3 and r2 - r1 < r3 and r2 + r3 > r1 and r3 - r2 < r1 and r3 + r1 > r2 and r1 - r3 < r2:
                                    print('Essas retas podem formar um triângulo')
                                else:
                                    print('Essas retas não podem formar um triângulo')
                            else:
                                if r1 + r2 > r3 and r2 - r1 < r3 and r2 + r3 > r1 and r3 - r2 < r1 and r3 + r1 > r2 and r3 - r1 < r2:
                                    print('Essas retas podem formar um triângulo')
                                else:
                                    print('Essas retas não podem formar um triângulo')
print('='*60)