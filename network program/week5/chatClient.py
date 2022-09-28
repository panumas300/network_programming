from socket import *
from unicodedata import name

HOST = 'localhost'
PORT = 5000
BUFSIZE = 4096
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
messageFromServer = bytes.decode(server.recv(BUFSIZE))
print(messageFromServer)
name = input('Enter your name: ')
userName = str.encode(name)
server.send(userName)

while True:
    receiveMessage = bytes.decode(server.recv(BUFSIZE))
    if not receiveMessage:
        print('Server disconnected')
        break
    print(receiveMessage)
    sendMessagr = input ('> ')
    if not sendMessagr:
        print('Server disconnected')
        break
    server.send(str.encode(sendMessagr))
server.close()