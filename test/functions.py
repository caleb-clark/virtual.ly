import socket

def startServer(portno):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('127.0.0.1', portno))

        sock.listen()
        sock_c, addr = sock.accept()

        with sock_c: 
            msg = sock_c.recv(1024)

            print(msg)

            sock_c.sendall('Received' + msg)

def startClient(server_ip, portno, msg):

    sock = socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((server_ip, portno))

    sock.sendall(msg)

    msg_recvd = sock.recv(1024)

    print(msg_recvd)

