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

def consultar():
    print "\n-----------------"
    print "Consultar contato"
    print "-----------------"
    nome = raw_input("Digite o nome: ")

    for contato in agenda:
        if nome.lower() in contato["nome"].lower():
            print '------------'
            print 'Nome: %s' % contato["nome"]
            print '%s' % contato["numero"]
            print '------------'

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

    with open(caminho, "w") as arquivo:
        json.dump(agenda, arquivo)

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
        print "Ainda não implementado"
    elif opcao == "3":
        consultar()
    elif opcao == "4":
        print "Ainda não implementado"
    elif opcao == "5":
        print "Ainda não implementado"
    elif opcao == "6":
        print "Ainda não implementado"
    elif opcao == "7":
        break
    else:
        print "---------------------------------"
        print "Opção inválida"
        print "---------------------------------"
