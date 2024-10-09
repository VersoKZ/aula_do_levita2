quantidade = 0
soma = 0
media = 0

valor = float(input('digite a nota: '))

if valor >= 0 and valor < 11:
    perg = input('deseja continuar? (s/n): ')
    while perg == 's':
        soma = soma + valor
        quantidade = quantidade + 1
        valor = float(input('digite a nota: '))
        perg = input('deseja continuar? (s/n): ')

    res = soma / quantidade
    print(range(res, 2))

else:
    print('valor é invalido')

