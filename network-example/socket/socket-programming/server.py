import socket

host = 'localhost'
port = 50007

count =  0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected:', addr)
        while True:
            count += 1
            data = conn.recv(1024)
            print(count, '----',data)
            if not data: break
            conn.send(data)
