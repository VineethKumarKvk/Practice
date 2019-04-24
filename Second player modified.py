import socket
s=socket.socket()
s.connect((socket.gethostname(),70))
data=s.recv(1024)
cpnum=int(data.decode())
s.send('I am ready'.encode())
print('Waiting for Player 1')
while True:
    data=s.recv(1024)
    if (data.decode())=='game over':
            print('player 1 won')
            break
    print(data.decode())
    if data:
        mynum=int(input('Enter ur number:'))
        
        
        if mynum<cpnum:
            print('REQUIRED is HIGHER')
            s.send('its ur turn'.encode())
        elif mynum>cpnum:
            print('REQUIRED is LESSER')
            s.send('its ur turn'.encode())
        else:
            print('********** YOU WON ********')
            s.send('game over'.encode())
            break
s.close()
                


