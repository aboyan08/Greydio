import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
CHUNK = 1024
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(CHUNK)
    #print('Server received', repr(data))

    filename='ohbanana.wav'
    f = open(filename,'rb')
    l = f.read(CHUNK)
    while (l):
       conn.send(l)
       #print('Sent ',repr(l))
       l = f.read(CHUNK)
    f.close()

    print('Done sending')
    conn.close()