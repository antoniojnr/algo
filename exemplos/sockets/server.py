#!/usr/bin/python
# coding:utf8

import socket
import thread
import random

clientes = {}
perguntas = [
    {
        'desc': 'Quanto é 2 + 2?',
        'alt': [2, 3, 4, 5, 6],
        'certa': 2,
        'valor': 1
    },
    {
        'desc': 'Qual a cor do céu ao meio dia em um dia ensolarado, sem nuvens?',
        'alt': ['azul', 'vermelho', 'verde', 'preto', 'rosa'],
        'certa': 0,
        'valor': 2
    },
    {
        'desc': 'Quantos bits tem um byte?',
        'alt': [16, 32, 64, 128, 8],
        'certa': 4,
        'valor': 3
    }
]

def montar_quiz(quiz, indice):
    texto = """PERGUNTA: %s
    0. %s
    1. %s
    2. %s
    3. %s
    4. %s
    Para responder: resp %s [resposta]""" % (quiz['desc'], quiz['alt'][0], quiz['alt'][1], quiz['alt'][2], quiz['alt'][3], quiz['alt'][4], indice)

    return texto


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

                if comando[0] == 'msg':
                    cliente = None
                    for k, v in clientes.items():
                        if v['nome'] == comando[1]:
                            cliente = k

                    if cliente is not None:
                        sck = clientes[cliente]['socket']

                    sck.send(' '.join(comando[2:]))
                elif comando[0] == 'nome':
                    clientes[addr]['nome'] = comando[1]
                    clientsocket.send('Bem vindo, %s' % comando[1])
                elif comando[0] == 'pontos':
                    pontos = ['%s: %s' % (v['nome'], v['pontos']) for k, v in clientes.items()]

                    clientsocket.send(', '.join(pontos))
                elif comando[0] == 'quiz?':
                    indice = random.randint(0, len(perguntas) - 1)
                    pergunta = perguntas[indice]
                    clientsocket.send(montar_quiz(pergunta, indice))
                elif comando[0] == 'resp':
                    # resp 0 2
                    pergunta = perguntas[int(comando[1])]
                    if pergunta['certa'] == int(comando[2]):
                        clientes[addr]['pontos'] += pergunta['valor']
                        clientsocket.send('Você acertou! Ganhou %s pontos. Você tem %s pontos.' % (pergunta['valor'], clientes[addr]['pontos']))
                    else:
                        clientsocket.send('Você errou! Tente novamente.')

                elif comando[0] == 'quem':
                    nomes = [v['nome'] for k, v in clientes.items()]

                    clientsocket.send(', '.join(nomes))
                elif msg == 'diga tchau':
                    clientsocket.send('tchau')
                elif msg == 'desconecte':
                    s.close()
                else:
                    print addr, ' >>> ', msg

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
   clientes[endereco] = {
    'nome': 'Desconhecido',
    'pontos': 0,
    'socket': cli_sock }
   print 'clientes conectados', clientes
   thread.start_new_thread(on_new_client, (cli_sock, endereco))
s.close()
