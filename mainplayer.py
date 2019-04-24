import socket
import random

s=socket.socket()
cpnum=str(random.randint(1,10))
s.bind((socket.gethostname(),70))

s.listen(5)

print('player 1 is ready')
con,addr=s.accept()
con.send(cpnum.encode('ascii'))
cpnum=int(cpnum)




while True:
    print('Think about the Number.....')
    data=con.recv(1024)
    if (data.decode())=='game over':
            print('player 2 won')
            break
        
    if data:
        mynum=int(input('Enter ur number:'))
            
        
        if mynum<cpnum:
            print('REQUIRED is HIGHER')
            con.send('its ur turn'.encode('ascii'))
        elif mynum>cpnum:
            print('REQUIRED is LESSER')
            con.send('its ur turn'.encode('ascii'))
        else:
            print('******** YOU WON *********')
            con.send('game over'.encode('ascii'))
            break
s.close()
con.close()


