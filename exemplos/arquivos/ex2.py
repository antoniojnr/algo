
def contarPalavra(caminho, palavra):
    contador = 0
    with open(caminho, 'r') as arquivo:
        for linha in arquivo:
            for p in linha.split():
                if p == palavra:
                    contador += 1
    return contador

print contarPalavra('ex2', 'qwe')
