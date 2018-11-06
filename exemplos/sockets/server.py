#!/usr/bin/python
# coding:utf8

import socket
import thread

def on_new_client(clientsocket,addr):
    while True:
        try:
            msg = clientsocket.recv(1024)

            # Se a mensagem for de tamanho 0, a conexão se encerrou
            if len(msg) == 0:
                print addr, ' se desconectou'
                break
            else: # Se a conexão não se encerrou, mostre a mensagem
                print addr, ' >>> ', msg

            # Responda com uma mensagem de volta para o cliente que enviou
            msg = raw_input('Sua msg <<< ')
            # Envie a mensagem através do socket
            clientsocket.send(msg)
        except socket.error:
            print addr, 'se desconectou'
            break
    clientsocket.close()


s = socket.socket()         # Criar um socket
host = '10.5.53.145'        # Endereço da máquina local
port = 50000                # Reserve uma porta para o serviço

print 'Servidor iniciado!'
print 'Aguardando clientes...'

s.bind((host, port))        # Conecte-se ao endereço e porta especificados
s.listen(5)                 # Espere por conexões (5 é o num. máximo de conexões em fila)

while True:
   cli_sock, endereco = s.accept()     # Estabeleça conexão
   print endereco, 'se conectou'
   thread.start_new_thread(on_new_client, (cli_sock, endereco))
s.close()
