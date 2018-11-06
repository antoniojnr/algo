# coding:utf8
import os
import json

caminho = "agenda.json"
agenda = []

# Cria o arquivo da agenda se não existe
# Se existir, carrega o arquivo
if not os.path.exists(caminho):
    with open(caminho, "w") as arquivo:
        json.dump(agenda, arquivo)
else:
    with open(caminho, "r") as arquivo:
        agenda = json.load(arquivo)

def criterioOrdenar(elemento):
    return elemento['nome']

def buscar(texto, por_letra=False):
    print '------------'
    agenda.sort(key=criterioOrdenar)
    for contato in agenda:
        if por_letra:
            if texto.lower() == contato["nome"].lower()[0]:
                print 'Nome: %s' % contato["nome"]
                print '%s' % contato["numero"]
                print '------------'
        else:
            if texto.lower() in contato["nome"].lower():
                print 'Nome: %s' % contato["nome"]
                print '%s' % contato["numero"]
                print '------------'

def consultar():
    print "\n-----------------"
    print "Consultar contato"
    print "-----------------"

    nome = raw_input("Digite o nome: ")
    buscar(nome)

def listar_por_letra():
    print "\n-----------------"
    print "Consultar contato"
    print "-----------------"

    letra = raw_input("Digite a letra: ")
    buscar(letra, True)

def editar():
    print "\n--------------"
    print "Editar contato"
    print "--------------"

    nome = raw_input("Digite o nome: ")
    indice = None

    for i, contato in enumerate(agenda):
        if nome.lower() == contato["nome"].lower():
            indice = i
            break

    if indice is None:
        print "\n----------------------"
        print "Contato não encontrado"
        print "----------------------"
    else:
        print '------------'
        print 'Nome: %s' % agenda[indice]["nome"]
        print '%s' % agenda[indice]["numero"]
        print '------------'
        opcao = raw_input("Mudar nome? (s/n) ")
        modificou = False
        if opcao == "s":
            nome = raw_input("Novo nome: ")
            agenda[indice]["nome"] = nome
            modificou = True

        opcao = raw_input("Mudar numero? (s/n) ")
        if opcao == "s":
            numero = raw_input("Novo número: ")
            agenda[indice]["numero"] = numero
            modificou = True

        if modificou:
            with open(caminho, "w") as arquivo:
                json.dump(agenda, arquivo)

def remover():
    print "\n---------------"
    print "Remover contato"
    print "---------------"

    nome = raw_input("Digite o nome: ")
    indice = None

    for i, contato in enumerate(agenda):
        if nome.lower() == contato["nome"].lower():
            indice = i
            break

    if indice is None:
        print "\n----------------------"
        print "Contato não encontrado"
        print "----------------------"
    else:
        print '------------'
        print 'Nome: %s' % agenda[indice]["nome"]
        print '%s' % agenda[indice]["numero"]
        print '------------'
        conf = raw_input("Tem certeza? (s/n) ")

        if conf == "s":
            del agenda[indice]
            print "\n----------------------"
            print "Contato removido"
            print "----------------------"
            with open(caminho, "w") as arquivo:
                json.dump(agenda, arquivo)

def inserir():
    print "\n------------"
    print "Novo contato"
    print "------------"
    nome = raw_input("Digite o nome: ")
    numero = raw_input("Digite o número: ")

    contato = {
        "nome": nome,
        "numero": numero
    }

    agenda.append(contato)
    agenda.sort(key=criterioOrdenar)
    with open(caminho, "w") as arquivo:
        json.dump(agenda, arquivo)

def listar():
    print "\n-----------------"
    print "Todos os contatos"
    print "-----------------"

    print '------------'
    agenda.sort(key=criterioOrdenar)
    for contato in agenda:
        print 'Nome: %s' % contato["nome"]
        print '%s' % contato["numero"]
        print '------------'

while True:
    print "------- AGENDA TELEFONICA -------"
    print "              MENU"
    print "---------------------------------"
    print "1 - Adicionar"
    print "2 - Editar"
    print "3 - Consultar"
    print "4 - Listar todos"
    print "5 - Listar por letra"
    print "6 - Excluir"
    print "7 - Sair"

    opcao = raw_input("Digite a opção: ")

    if opcao == "1":
        inserir()
    elif opcao == "2":
        editar()
    elif opcao == "3":
        consultar()
    elif opcao == "4":
        listar()
    elif opcao == "5":
        listar_por_letra()
    elif opcao == "6":
        remover()
    elif opcao == "7":
        break
    else:
        print "---------------------------------"
        print "Opção inválida"
        print "---------------------------------"
