import socket

s = socket.socket()
host = socket.gethostname()
port = 60006
CHUNK = 1024

s.connect((host, port))
s.send("Hello server!".encode())

filename='ohbanana.wav'
f = open(filename,'rb')
l = f.read(CHUNK)
while (l):
   s.send(l)
   l = f.read(CHUNK)
print("file sent")
f.close()

s.close()
print('connection closed')