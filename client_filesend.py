import socket
import pyaudio
import wave

s = socket.socket()
host = socket.gethostname()
port = 60000
CHUNK = 1024

s.connect((host, port))
s.send("Hello server!".encode())

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

wf = wave.open(f.name, 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)
print('playing audio')
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)

print('file ended')

stream.stop_stream()
stream.close()
wf.close()
p.terminate()

f.close()
s.close()
print('connection closed')