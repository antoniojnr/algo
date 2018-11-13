#!/usr/bin/python
# coding:utf8

import socket
import sys

# cria um socket TCP/IP
# socket.SOCK_STREAM indica que o socket é TCP
# socket.SOCK_DGRAM indica que o socket é UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor rodando no endereço 'localhost', porta 50000
server_address = ('localhost', 5432)
print 'Conectando a %s na porta %s' % server_address
# Conecta o socket ao host especificado, na porta especificada
sock.connect(server_address)

try:
    while True:
        # Mensagem para ser enviada
        message = raw_input('Sua mensagem <<< ')

        # Se a mensagem for 'EXIT', encerre
        if message == 'EXIT':
            break

        # Envia a mensagem para o servidor através do socket
        sock.sendall(message)

        # Recebe o que o servidor enviou de volta
        data = sock.recv(1024)
        print '>>> ', data
finally:
    print 'Fechando conexão'
    sock.close()
