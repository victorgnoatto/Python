from random import randint
computador = randint(0, 10)
print('''Salve seres humanos. Acabei de pensar em um numero entre 1 a 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Maaais.... Tente outra vez: ')
        elif jogador > computador:
            print('Meeenos.... Tente outra vez: ')
print('Você acertou com {} palpites. Parabéns.'.format(palpite))