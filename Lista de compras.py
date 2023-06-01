"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inssrir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

import os 

lc = []

while True:
    indice = range(len(lc))
    cmd = input('O que você quer fazer na lista?\n[i]nserir [a]pagar [l]istar [s]air\n')
    os.system('cls')
    cp = 'ials'

    if cmd in cp:

        if len(cmd) == 1:

            if cmd == 'i':
                item = input('O que você quer adicionar?\n')
                lc.append(item)
                os.system('cls')
                print(f'{item} foi adicionado a lista de compras!')
                continue

            if cmd == 'a':
                try:
                    item = int(input('Qual o índice do item que você quer apagar?\n'))
                    os.system('cls')
                    print(lc.pop(item), 'foi apagado da lista de compras!')
                except:
                    os.system('cls')
                    print('Este índice não existe! ')

            if cmd == 'l':
                os.system('cls')
                if len(lc) > 0:
                    for i in indice:
                        print(i, lc[i],'\n')
                        continue
                else:
                    os.system('cls')
                    print('Não há nada para ser mostrado!\n ')
                    continue

            if cmd == 's':
                break

        else:
            os.system('cls')
            print('Digite apenas um comando!\n')
    
    else:
        print('Digite um comando válido!\n')