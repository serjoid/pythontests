import os
def gerador1():
    n_cpf = input('Digite os 9 primeiros dígitos do seu CPF (apenas os 9 primeiros números): ')
    while len(n_cpf) != 9:
        n_cpf = input('Digite os 9 primeiros dígitos do seu CPF (apenas os 9 primeiros números): ')
    n1=(int(n_cpf[0])*10)
    n2=(int(n_cpf[1])*9)
    n3=(int(n_cpf[2])*8)
    n4=(int(n_cpf[3])*7)
    n5=(int(n_cpf[4])*6)
    n6=(int(n_cpf[5])*5)
    n7=(int(n_cpf[6])*4)
    n8=(int(n_cpf[7])*3)
    n9=(int(n_cpf[8])*2)
    
    soma = n1+n2+n3+n4+n5+n6+n7+n8+n9
    multiplica = soma * 10
    digito1 = multiplica % 11
    if digito1 > 9:
        digito1 = 0
    else:
        digito1 = digito1
    #gerador do dígido 2
    n1=(int(n_cpf[0])*11)
    n2=(int(n_cpf[1])*10)
    n3=(int(n_cpf[2])*9)
    n4=(int(n_cpf[3])*8)
    n5=(int(n_cpf[4])*7)
    n6=(int(n_cpf[5])*6)
    n7=(int(n_cpf[6])*5)
    n8=(int(n_cpf[7])*4)
    n9=(int(n_cpf[8])*3)
    n10=(int(digito1)*2)
    
    soma2 = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
    multiplica2 = soma2*10
    digito2 = multiplica2%11
    if digito2 > 9:
        digito2 = 0
    else:
        digito2 = digito2

    cpf_final =(n_cpf)

    os.system('clear')    
    print(f'O seu cpf com o dígito verificador é: ´{cpf_final}-{digito1}{digito2}')

gerador1()