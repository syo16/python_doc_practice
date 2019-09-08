import socket

host = 'localhost'
port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    a = s.sendall(b'Hello world')
    data = s.recv(1024)
    print(a)
    print(data.decode())
