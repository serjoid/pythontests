import hashlib
import getpass
import os

def signup():
    email = input("Digite o seu endereço de email: ")
    pwd = getpass.getpass("Digite sua senha: ")
    conf_pwd = getpass.getpass("Confirme sua senha: ")
    if email == '' or pwd =='' or conf_pwd =='':
        print('Os dados não podem ficar em branco!')
    elif conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "a") as f:
            f.write(f'{email},{hash1}\n')
        f.close()
        print("Você foi registrado com sucesso!")
    else:
        print('As senhas digitadas não são as mesmas!')

def login():
    email = input("Digite seu email: ")
    pwd = getpass.getpass("Digite sua senha: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open('credentials.txt', 'r')as f:
        for l in f:
            if f'{email},{auth_hash}'==l.split('\n'):
                print('Usuário logado com sucesso!')

def clear():
    os.system('clear')

while True:
    opcao = input('Selecione a opção que deseja: \n[1] Novo cadastro\n[2] Login\n[3] Sair\n')
    if opcao == '1':
        clear()
        signup()
    elif opcao == '2':
        clear()
        login()
    elif opcao == '3':
        clear()
        print('Você saiu do programa!')
        break
    else:
        clear()
        print('Você não digitou uma opção válida!')