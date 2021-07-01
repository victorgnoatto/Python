from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0

while opçao != 5:
    print('''    [ 1 ] Soma
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos número
    [ 5 ] Sair do programa''')
    opçao = int(input('>>>>>>> Qual é a sua opção? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}.'.format(n1, n2, soma))
    elif opçao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}.'.format(n1, n2, produto))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando.....')
    else:
        print('Opção invalida, tente novamente.')
    print('=-' * 15)
    sleep(1)
print('Fim do programa. Volte Sempre!')
