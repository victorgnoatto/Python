from time import sleep
tot18 = totM = totF = 0
print('-=' * 15)
print('     CADASTRE UMA PESSOA')
print('-=' * 15)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    cont = ' '
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totM += 1
    if sexo == 'F' and idade < 20:
        totF += 1
    while cont not in 'SN':
        cont = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('PROCESSANDO....')
sleep(2)
print(f'''Total de pessoas com mais de 18 anos: {tot18}.
Ao todo temos {totM} homens cadastrados.
E temos {totF} mulher(es) com menos de 20 anos.''')