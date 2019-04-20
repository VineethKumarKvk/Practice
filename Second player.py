import socket
s=socket.socket()
s.connect((socket.gethostbyname('127.0.0.1'),80))
data=s.recv(1024)
cpnum=int(data.decode())
s.send('I am ready'.encode())
while True:
    data=s.recv(1024)
    print(data.decode())
    if data:
        mynum=int(input('Enter ur number:'))
        if (data.decode())=='game over':
            print('player 2 won')
            break
        
        
        if mynum<cpnum:
            print('Required is higer')
            s.send('its ur turn'.encode())
        elif mynum>cpnum:
            print('Required is lesser')
            s.send('its ur turn'.encode())
        else:
            print('player 1 won')
            s.send('game over'.encode())
            
            break
s.close()
                


