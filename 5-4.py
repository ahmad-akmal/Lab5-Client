import socket
import time
ClientSocket = socket.socket()
host = '192.168.230.5'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

print('Connected to ' + host)

while True:
    filename = input(str("Please enter the filename to send : "))

    if filename == '':
       ClientSocket.send(str.encode(filename))
       time.sleep(1)
       break

    ClientSocket.send(str.encode(filename))
    file = open(filename, 'rb')
    file_data = file.read(1024)
    ClientSocket.send(file_data)
    print("File has been transmitted successfully")

ClientSocket.close()
