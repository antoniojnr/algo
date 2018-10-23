try:
    with open('aula1', 'r') as f:
        for linha in f:
            print linha,
except IOError:
    print 'nao existe. escrevendo...'
    with open('aula1', 'w') as f:
        f.write('novalinha')

    with open('aula1', 'r') as f:
        for linha in f:
            print linha,
