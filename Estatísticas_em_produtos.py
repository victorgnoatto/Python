soma = totmil = cont = menor = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    soma += preco
    cont += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    if preco >= 1000:
        totmil += 1

    conti = ' '
    while conti not in 'SN':
        conti = str(input('Deseja continuar:[S/N] ')).strip().upper()[0]
    if conti == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total de compras foi R${soma:.2f} .')
print(f'Temos {totmil} custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f} .')