import socket

port = 60006
CHUNK = 1024
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print('Server listening....')

#while True:
conn, addr = s.accept()     # Establish connection with client.
print('Got connection from', addr)
data = conn.recv(CHUNK)

with open('uploaded_file.wav', 'wb') as f:
    print('file opened')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

conn.close()