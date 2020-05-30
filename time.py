import socket


def get_time():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(b'', ('localhost', 123))
        data = sock.recvfrom(1024)
        print(data[0].decode())


if __name__ == '__main__':
    get_time()
