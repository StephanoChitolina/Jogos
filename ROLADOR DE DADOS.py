from random import randint
from time import sleep


class RoladorDados:
    def __init__(self, n_lados, n_dados):
        self.n_lados = n_lados
        self.n_dados = n_dados

    def rolar_dado(self):
        soma_total = 0
        for dado in range(1, self.n_dados + 1):
            rolagem = randint(1, self.n_lados)
            print(f'resultado do {dado}º dado: {rolagem}')
            soma_total += rolagem
        print(f'O resultado da soma dos dados é {soma_total}')


def pega_n_lados():
    n_lados = 0
    try:
        n_lados = int(input('Quantos lados tem o dado que você quer rolar? '))
    except ValueError:
        print('Oops! Digite apenas números')
        n_lados = pega_n_lados()
    else:
        while n_lados <= 1:
            print('O número de lados deve ser maior que 1!')
            n_lados = int(input('Quantos lados tem o dado que você quer rolar? '))
    return n_lados


def pega_n_dados():
    n_dados = 0
    try:
        n_dados = int(input('Quantos dados você quer jogar? '))
    except ValueError:
        print('Oops! Digite apenas números')
        n_dados = pega_n_dados()
    else:
        while n_dados < 1:
            print('O número de dados não pode ser menor que 1!')
            n_dados = int(input('Quantos dados você quer jogar? '))
    return n_dados


while True:
    numero_lados = pega_n_lados()
    numero_dados = pega_n_dados()
    roladorX = RoladorDados(numero_lados, numero_dados)

    print('Rolando o dado...')
    sleep(1)
    roladorX.rolar_dado()
    print('Fim da rolagem!')

    continuar = input('Quer fazer outra rolagem? [s/n] ').strip().lower()
    if continuar == 'n':
        break
    elif continuar == 's':
        continue
    else:
        print('Digite somente "s" para sim e "n" para não!')
