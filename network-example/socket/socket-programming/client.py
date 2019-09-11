import socket

host = 'localhost'
port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    file = open('./text.txt', 'br')
    a = s.sendfile(file)
    data = s.recv(1024)
    print(a)
    print(data)
