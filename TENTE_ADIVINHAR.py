from random import randint


def pega_palpite(max_numero):
    try:
        palpite = int(input('Qual é seu palpite, meu caro? '))
    except ValueError:
        print(f'Oops! Não valeu, somente um número entre 0 e {max_numero}')
        palpite = pega_palpite()
    if palpite < 0 or palpite > max_numero:
        print(f'Oops! Não valeu, somente um número entre 0 e {max_numero}')
        palpite = pega_palpite()
    return palpite


def da_dica(palpite, computador):
    if palpite > computador:
        print(f'É MENOR que {palpite}... Tente mais uma vez.')
    else:
        print(f'É MAIOR que {palpite}... Tente mais uma vez.')


def joga_adivinhacao(numero_sorteado, max_numero):
    tentativas = 0
    acertou = False
    while not acertou:
        palpite = pega_palpite(max_numero)
        tentativas += 1
        if numero_sorteado == palpite:
            acertou = True
        else:
            da_dica(palpite, numero_sorteado)
    print(f'Acertou com {tentativas} tentativas. Parabéns!!!')


def continuar_jogando():
    continuar = input('Gostaria de jogar novamente? [s/n] ').strip().lower()[0]
    while continuar not in 'sn':
        print('Oops! Resposta inválida. Digite apenas "s" para sim ou "n" para não.')
        continuar = continuar_jogando()
    return continuar


max_numero = 6
print('-=-' * 19)
print(f' Vou pensar em um número entre 0 a {max_numero}. Tente adivinhar...')
print('-=-' * 19)
numero_sorteado = randint(0, max_numero)
continuar = 's'

while continuar != 'n':
    joga_adivinhacao(numero_sorteado, max_numero)
    continuar = continuar_jogando()
