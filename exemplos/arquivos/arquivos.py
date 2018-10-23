# coding:utf8

import os

print "Escolha uma das opções a seguir:"
print "1 - ler arquivo completo"
print "2 - ler arquivo linha por linha"
print "3 - adicionar uma linha ao arquivo (sobrescrever)"
print "4 - adicionar uma linha ao arquivo (anexar)"
print "5 - remover arquivo"

opcao = raw_input("Opção: ")

if opcao == "1":
    path = raw_input('Digite o caminho do arquivo: ')
    try:
        with open(path, 'r') as file:
            conteudo = file.read()
        print conteudo
    except IOError:
        print "(!) O arquivo '%s' não existe" % path
elif opcao == "2":
    path = raw_input('Digite o caminho do arquivo: ')
    try:
        with open(path, 'r') as file:
            for line in file:
                print line,
    except IOError:
        print "(!) O arquivo '%s' não existe" % path
elif opcao == "2":
    path = raw_input('Digite o caminho do arquivo: ')
    try:
        with open(path, 'r') as file:
            for line in file:
                print line,
    except IOError:
        print "(!) O arquivo '%s' não existe" % path
elif opcao == "3":
    path = raw_input('Digite o caminho do arquivo: ')

    if os.path.exists(path):
        print "O arquivo já existe. Continuando..."
    else:
        print "O arquivo não existe e foi criado"

    with open(path, 'w') as file:
        linha = raw_input("O que você vai escrever? ")
        print "Atenção: Todo o conteúdo do arquivo será sobrescrito"
        conf = raw_input("Continuar? (s/n) ")
        if conf == "s":
            file.write(linha + '\n')
elif opcao == "4":
    path = raw_input('Digite o caminho do arquivo: ')
    conf = "n"

    if os.path.exists(path):
        conf = raw_input("O arquivo já existe. Continuar? (s/n) ")
    else:
        print "O arquivo não existe e foi criado"
        conf = "s"

    if conf == "s":
        with open(path, 'a') as file:
            linha = raw_input("O que você vai escrever? ")
            file.write(linha + '\n')
elif opcao == "5":
    path = raw_input('Digite o caminho do arquivo: ')

    if os.path.exists(path):
        conf = raw_input("Tem certeza que deseja remover '%s'? (s/n) " % path)
        if conf == "s":
            os.remove(path)
            print "O arquivo '%s' foi removido" % path
    else:
        print "(!) O arquivo '%s' não existe" % path
