from string import digits, ascii_letters
from random import choice

VERMELHO = '\033[31m'
AZUL = '\033[34m'
AMARELO = '\033[33m'
VERDE = '\033[32m'
RESET = '\033[m'

def Gerador_de_senha():
    titulo = 'GERADOR DE SENHA'
    linha = '-=-' * 30
    
    print(f'{AZUL}-=-{RESET}' * 30)
    print(f'{VERDE}{titulo}{RESET}'.center(len(linha)))
    print(f'{AMARELO}créditos: MafiaBoyBR{RESET}')
    print(f'{AZUL}-=-{RESET}' * 30)
    print()
    
    try:
        tamanho_senha = int(input("Informe o tamanho da sua senha: "))
        caracteres = digits + ascii_letters
        password = ''.join(choice(caracteres) for _ in range(tamanho_senha))
        return password
    except ValueError:
        print(f'{VERMELHO}Erro: Insira um valor numérico válido para o tamanho da senha!{RESET}')

senha = Gerador_de_senha()
if senha:
    print(f'Senha gerada: {VERMELHO}{senha}{RESET}')
