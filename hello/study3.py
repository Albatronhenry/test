import sys
import socket
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverhost = socket.gethostname()

port = 8090

serversocket.bind((serverhost,port))

serversocket.listen(5)

while True:
    clientsocket,addr = serversocket.accept()

    print('link address: {}'.format(addr))

    msg = 'welcome to henry home青云之家 !' + '\n'

    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()


