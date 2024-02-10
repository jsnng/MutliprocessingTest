import socket

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '127.0.0.1'
    port = 50514
    sock.bind((host, port))

    while True:
        message, addr = sock.recvfrom(1024)
        message = message.decode()

        print(message)
