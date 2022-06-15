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
        return soma_total


try:
    n_lados = int(input('Quantos lados tem o dado que você quer rolar? '))
    n_dados = int(input("quantos dados você quer jogar? "))
except ValueError:
    print('Oops! Digite apenas números')
else:
    rolador = RoladorDados(n_lados, n_dados)
    print('Rolando o dado...')
    sleep(1)
    resultado = rolador.rolar_dado()





