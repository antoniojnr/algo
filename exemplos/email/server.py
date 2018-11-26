#!/usr/bin/python
# coding:utf8

import socket
import thread
import random
from datetime import datetime

caixas = {}

def fazer_login(usuario, senha):
    if usuario in caixas:
        caixa = caixas[usuario]
        if senha == caixa['senha']:
            return True
        else:
            return False
    else:
        return False

def on_new_client(clientsocket,addr):
    while True:
        try:
            msg = clientsocket.recv(1024)

            # Se a mensagem for de tamanho 0, a conexão se encerrou
            if len(msg) == 0:
                print addr, ' se desconectou'
                break
            else: # Se a conexão não se encerrou, mostre a mensagem
                comando = msg.split(' ')

                # crie nome senha
                if comando[0] == 'crie':
                    dono = comando[1]
                    senha = comando[2]
                    nova = {
                        'senha': senha,
                        'enviadas': [],
                        'recebidas': []
                    }

                    if dono in caixas:
                        clientsocket.send('Ja existe um usuario registrado com esse nome.\nEscolha outro nome.')
                    else:
                        caixas[dono] = nova
                        clientsocket.send('Voce se registrou com sucesso, %s.' % dono)
                # login nome senha
                elif comando[0] == 'login':
                    dono = comando[1]
                    senha = comando[2]

                    if fazer_login(dono, senha):
                        clientsocket.send('ok')
                    else:
                        clientsocket.send('Usuario ou senha incorretos.')
                # rec nome senha
                elif comando[0] == 'rec':
                    dono = comando[1]
                    senha = comando[2]

                    if fazer_login(dono, senha):
                        caixa = caixas[dono]
                        recebidas = caixa['recebidas']

                        if len(recebidas) == 0:
                            clientsocket.send('Voce nao tem mensagens.')
                        else:
                            retorno = "RECEBIDAS\n---------\n\n"
                            for indice, msg in enumerate(recebidas):
                                retorno += '%s - %s\n' % (indice, msg['assunto'])
                            clientsocket.send(retorno)
                    else:
                        clientsocket.send('Usuario ou senha incorretos.')
                # enviar nome senha destinatario assunto mensagem
                elif comando[0] == 'env':
                    dono = comando[1]
                    senha = comando[2]
                    dest = comando[3]
                    ast = comando[4]
                    msg = comando[5:]

                    if fazer_login(dono, senha):
                        if dest in caixas:
                            nova = {
                                'rem': dono,
                                'dest': dest,
                                'assunto': ast,
                                'msg': ' '.join(msg),
                                'data': str(datetime.now())
                            }
                            caixa_remt = caixas[dono]['enviadas']
                            caixa_dest = caixas[dest]['recebidas']

                            caixa_remt.append(nova)
                            caixa_dest.append(nova)

                            clientsocket.send('Sua mensagem foi enviada: %s' % str(nova))
                        else:
                            clientsocket.send('Destinatario inexistente.')
                    else:
                        clientsocket.send('Usuario ou senha incorretos.')
                else:
                    clientsocket.send('Nao entendi seu comando.')

                    # Responda com uma mensagem de volta para o cliente que enviou
                    # msg = raw_input('Sua msg <<< ')
                    # Envie a mensagem através do socket
                    clientsocket.send(msg.upper())
        except socket.error:
            print addr, 'se desconectou'
            break
    clientsocket.close()


s = socket.socket()         # Criar um socket
host = 'localhost'        # Endereço da máquina local
port = 5432                # Reserve uma porta para o serviço

print 'Servidor iniciado!'
print 'Aguardando clientes...'

s.bind((host, port))        # Conecte-se ao endereço e porta especificados
s.listen(5)                 # Espere por conexões (5 é o num. máximo de conexões em fila)

while True:
   cli_sock, endereco = s.accept()     # Estabeleça conexão

   thread.start_new_thread(on_new_client, (cli_sock, endereco))
s.close()
