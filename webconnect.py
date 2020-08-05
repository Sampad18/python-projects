import socket
from time import sleep
my = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my.connect(("data.pr4e.org",80))
sleep(3)
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
my.send(cmd)

while True:
    data = my.recv(82)
    if (len(data)<1):
        break
    print(data.decode())
my.close()
