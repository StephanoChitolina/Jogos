from random import randint
print('-=-' * 19)
print(' Vou pensar em um número entre 0 a 10. Tente adivinhar...')
print('-=-' * 19)
computador = randint(0, 22)
tentativas = 0
continuar = 's'
while continuar != 'n':
    acertou = False
    while not acertou:
        try:
            palpite = int(input('Qual é seu palpite, meu caro? '))
        except ValueError:
            print('Oops! Não valeu, somente um número entre 0 e 22')
        else:
            tentativas += 1
            if palpite >= 0 and palpite <= 22:
                if computador == palpite:
                    acertou = True
                else:
                    if palpite > computador:
                        print(f'É MENOR que {palpite}... Tente mais uma vez.')
                    else:
                        print(f'É MAIOR que {palpite}... Tente mais uma vez.')
            else:
                print(f'Oops! Não valeu, somente um número entre 0 e 22')
    print(f'Acertou com {tentativas} tentativas. Parabéns!!!')
    continuar = input('Gostaria de jogar novamente? [s/n] ').strip().lower()[0]
    while continuar not in 'sn':
        print('Oops! Resposta inválida. Digite apenas "s" para sim ou "n" para não.')
        continuar = input('Gostaria de jogar novamente? [s/n] ').strip().lower()[0]