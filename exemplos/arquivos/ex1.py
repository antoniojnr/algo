with open('ex1', 'r') as arquivo:
    soma = 0
    for linha in arquivo:
        soma += int(linha)
    print soma
