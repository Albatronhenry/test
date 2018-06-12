import sys , socket
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clienthost = socket.gethostname()

clientport = 8090

clientsocket.connect((clienthost,clientport))

msg = clientsocket.recv(1024)

clientsocket.close()

print(msg.decode('utf-8'))