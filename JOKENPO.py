from random import randint
from time import sleep


def usuario_escolhe_jogada():
    try:
        jogada_uso = int(input('Das opções:\n{ 0 } PEDRA\n{ 1 } PAPEL\n{ 2 } TESOURA\nQual será a sua jogada? '))
        while jogada_uso > 2 or jogada_uso < 0:
            print('Oops! Jogada inválida! Tente de novo! (apenas 0, 1, ou 2)')
            jogada_uso = int(input('Das opções:\n{ 0 } PEDRA\n{ 1 } PAPEL\n{ 2 } TESOURA\nQual será a sua jogada? '))
    except ValueError:
        print('Digite somente os números 0, 1 ou 2 humano, letras não valem!')
        jogada_uso = usuario_escolhe_jogada()
    return jogada_uso


def partida_jokenpo():
    cpu_vitorias = jogador_vitorias = empates = 0
    PEDRA = 0
    PAPEL = 1
    TESOURA = 2
    jogada_uso = usuario_escolhe_jogada()
    print('JOOOOOO...')
    sleep(1)
    print('KEEEEEEN...')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print('=+=' * 8)
    print(f'Computador jogou {itens[jogada_cpu]}\nJogador jogou {itens[jogada_uso]}')
    print('=+=' * 8)
    if jogada_cpu == jogada_uso:
        empates += 1
    elif (jogada_cpu == PEDRA and jogada_uso == TESOURA) or \
            (jogada_cpu == PAPEL and jogada_uso == PEDRA) or \
            (jogada_cpu == TESOURA and jogada_uso == PAPEL):
        cpu_vitorias += 1
    else:
        jogador_vitorias += 1
    print('=+=' * 8)
    return jogador_vitorias, cpu_vitorias, empates


def placar(jogador_vitorias, cpu_vitorias, empates):
    print('=+=' * 8)
    print(f'>>>  FIM DE JOGO!!!  <<< \nPLACAR: COMPUTADOR {cpu_vitorias}  X  {jogador_vitorias} JOGADOR '
          f'\nEMPATES: {empates}')
    print('=+=' * 8)


def continuar_jogando():
    continuar = input('Gostaria de jogar novamente humano? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        print('Oops! Opção inválida! Somente S ou N!')
        continuar = continuar_jogando()
    return continuar


print('=+=' * 40)
print('''JOKENPÔ - O clássico, Pedra, papel e tesoura, também chamado em algumas regiões do Brasil de jokenpô
(do japonês じゃんけんぽん, jankenpon), é um jogo de mãos recreativo e simples para duas ou mais pessoas,
que não requer equipamentos nem habilidade.
    No Jokenpô, os jogadores devem simultaneamente esticar a mão, na qual cada um formou um símbolo (que significa
pedra, papel ou tesoura). Então, os jogadores comparam os símbolos para decidir quem ganhou, da seguinte forma:

Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).''')
print('=+=' * 40, '\n')
print('=+=' * 18)
print(' Vamos jogar uma divertida partida de Jokenpô humano? ')
print('=+=' * 18)
continuar = 'S'
jogador_vitorias_total = 0
cpu_vitorias_total = 0
empates_total = 0
while continuar != 'N':
    itens = ('Pedra', 'Papel', 'Tesoura')
    jogada_cpu = randint(0, 2)
    jogador_vitorias, cpu_vitorias, empates = partida_jokenpo()
    jogador_vitorias_total += jogador_vitorias
    cpu_vitorias_total += cpu_vitorias
    empates_total += empates
    continuar = continuar_jogando()
placar(jogador_vitorias_total, cpu_vitorias_total, empates_total)

