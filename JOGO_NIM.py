print('=*=' * 38)
print('''JOGO NIM - Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro.
Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas
peças possíveis ganha o jogo.

Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1)
peças ao jogador oponente.
''')
print('=*=' * 38)

from time import sleep

def computador_escolhe_jogada(n, m):
    sleep(2.5)
    if n <= m:     # Retira todas peças e ganha a partida
        return n
    jogada = n - ((n // (m + 1)) * (m + 1))
    if jogada == 0:    # Se não puder deixar multiplo de m+1 retira o máximo de peças possíveis
        return m
    return jogada      # Se não só devolve a estratégia jogada


def usuario_escolhe_jogada(n, m):
    sleep(2.5)
    jogada = int(input('Quantas peças você vai tirar? '))
    while jogada > m or jogada < 1 or jogada > n:
        print('Oops! Jogada inválida! Tente outra jogada! ')
        jogada = int(input('Quantas peças você vai tirar? '))
    return jogada


def partida():
    n = int(input('   -> Quantas peças no jogo? '))
    m = int(input('   -> Limite de peças por jogada? '))
    jogador_atual = None
    if n % (m + 1) == 0:
        print('>>> Você começa!!')
        sleep(1)
        jogador_atual = 'usuario'
    else:
        print('>>> Computador começa!!')
        sleep(1)
        jogador_atual = 'computador'
    while n > 0:        # A partida continua até que não haja mais peças no tabuleiro!
        if jogador_atual == 'usuario':
            jogada = usuario_escolhe_jogada(n, m)
            print(f'Você tirou {jogada} peça(s)')
            jogador_atual = 'computador'    # passa a vez de jogar para o computador
        else:
            jogada = computador_escolhe_jogada(n, m)
            print(f'O computador tirou {jogada} peça(s)')
            jogador_atual = 'usuario'       # passa a vez de jogar para o usuário
        n = n - jogada     # Este é o marcador que mostra quantas peças sobraram no tabuleiro
        if n > 0:
            print(f'Agora resta(m) apenas {n} peça(s) no tabuleiro')
            print('=!=' * 15)
    if jogador_atual == 'usuario':
        print('Fim do jogo! O computador Ganhou!')     # Pois no final do laço muda de jogador!
        return (1, 0)    # vai devolver (1, 0) -> (ponto_pc, ponto_jogador)
    else:
        print('Fim do jogo! Você venceu!')
        return (0, 1)    # vai devolver (0, 1) -> (ponto_pc, ponto_jogador)


def campeonato():
    placar_pc = 0
    placar_jogador = 0
    for p in range(1, 4):     # Ou seja 3 partidas do campeonato
        print(f'   **** RODADA {p} ****')
        (ponto_pc, ponto_jogador) = partida()     # corresponde ao return de partida()
        placar_pc += ponto_pc                # adiciona o return a variável placar_pc
        placar_jogador += ponto_jogador      # adiciona o return a variável placar_jogador
    print('  **** FINAL DO CAMPEONATO ****')
    print(f' >>> PLACAR:  Você {placar_jogador}  X  {placar_pc} Computador')


print('    Bem vindo ao jogo de NIM! Escolha:')
escolha_partida = int(input('''
    1 - para jogar uma partida isolada
    2 - para jogar um campeonato 
    >>> Qual sua é sua escolha? >>> '''))
print('=*=' * 15)
while escolha_partida > 2:
    print('Opção inválida! (digite somente 1 ou 2)')
    escolha_partida = int(input('>>> Qual sua é sua escolha? >>> '))
if escolha_partida == 1:
    print('   >>> Você escolheu uma partida isolada! <<<')
    sleep(2)
    partida()
else:
    print('   >>> Você escolheu um campeonato! <<<')
    sleep(2)
    campeonato()
