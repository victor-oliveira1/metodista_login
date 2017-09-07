#!/bin/python3
#Esta é uma biblioteca simples, criada para uso pessoal com o alvo de
#simplesmente automatizar o processo de logon na rede wifi da Metodista.
#Feito por Victor Oliveira

from urllib.request import urlopen
from urllib.parse import urlencode
from ssl import SSLContext

def _request(url, headers):
    '''Função interna para reutilizar código na requisição post
    Retorna a página solicitada (string)'''
    #Cria um contexto SSL vazio sem verificação de certificado
    ctx = SSLContext()

    #Efetua a requisição e retorna a página (string)
    return urlopen(url,
        urlencode(headers).encode(),
        context=ctx).read().decode()

def Login(usuario, senha):
    '''Função que efetua o login do usuário.
    Envia a URL e os dados post em DICT para a função _request'''
    #URL de login
    url = 'https://1.1.1.1/login.html'

    #Define os parâmetros do post
    headers = {'buttonClicked' : '4',
        'redirect_url' : '1.1.1.1/',
        'err_flag' : '0',
        'username' : usuario,
        'password' : senha}

    tmp = _request(url, headers)

    #Verifica se a senha está correta
    if 'Login Successful' in tmp:
        print('Login efetuado com sucesso!')
    else:
        print('Usuário e/ou senha inválidos!')

def Logout():
    '''Função que efetua o logout do usuário.
    Envia a URL e os dados post em DICT para a função _request'''
    #URL de logoff
    url = 'https://1.1.1.1/logout.html'

    #Define os parâmetros do post
    headers = {'userStatus' : '1',
        'err_flag' : '0',
        'err_msg' : ''}

    #Executa um teste básico para saber se fez o logout
    try:
        _request(url,
            headers)
        print('Logout efetuado com sucesso!')
    except:
        print('Não foi possível fazer logout.')
