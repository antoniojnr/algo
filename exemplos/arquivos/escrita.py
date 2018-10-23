#r - read
#w - write
#a - append

path = raw_input('Qual o nome do arquivo? ')

with open(path, 'a') as arq:
    print 'Insira as linhas. Deixe uma linha vazia para terminar.'

    while True:
        novalinha = raw_input()
        if novalinha == "":
            break
        arq.write(novalinha + '\n')
