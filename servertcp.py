import socket
from time import ctime

HOST=''
PORT=19638
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
tcpSerSock.listen(5)

while True:
    print 'waiting for connection...'
    tcpCliSock,addr=tcpSerSock.accept()
    print '...connected from:',addr
    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print data
        tcpCliSock.send('[%s] %s' %(ctime(),data))
        
        
tcpCliSock.close()
tcpSerSock.close()
