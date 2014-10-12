import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('1.0.0.9',666))
while True:
        data,addr = s.recvfrom(1024)
        if not data:
                print 'client has exited!'
                break
        print 'received:',data,'from',addr
s.close()

 
