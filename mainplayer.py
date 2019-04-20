import socket
import random

s=socket.socket()
cpnum=str(random.randint(1,10))
s.bind((socket.gethostname(),80))
s.listen(5)
print('player 1 is ready')
con,addr=s.accept()
con.send(cpnum.encode())
cpnum=int(cpnum)


while True:
    print('Waiting for Player 2')
    data=con.recv(1024)
    if data:
        mynum=int(input('Enter ur number:'))
        if (data.decode())=='game over':
            print('player 1 won')
            break
            
        
        elif mynum<cpnum:
            print('Required is higer')
            con.send('its ur turn'.encode('ascii'))
        elif mynum>cpnum:
            print('Required is lesser')
            con.send('its ur turn'.encode('ascii'))
        else:
            print('player 2 won')
            con.send('game over'.encode('ascii'))
            break
s.close()

    
    
