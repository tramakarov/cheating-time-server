import sys
import socket
import datetime


def get_time_offset():
    """Parse config file and return offset"""
    with open('config.txt', 'r') as config:
        try:
            return int(config.read())
        except ValueError:
            return None


def get_time(time_offset):
    """Get time plus offset"""
    official_time = datetime.datetime.now()
    cheated_time = official_time + datetime.timedelta(0, time_offset)
    return str(cheated_time)


def start_server(time_offset):
    """Main server method"""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('localhost', 123))
        while True:
            data, addr = sock.recvfrom(1024)
            print('Telling time to {ip}: {port}'.format(ip=addr[0], port=addr[1]))
            time = get_time(time_offset)
            message = time
            sock.sendto(message.encode('utf-8'), addr)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[-1] in ['-h', '--help']:
            with open('help.txt', 'r', encoding='utf-8') as help_text:
                print(help_text.read())
            exit(0)
        try:
            time_offset = int(sys.argv[-1])
        except ValueError:
            time_offset = None
    else:
        time_offset = get_time_offset()

    if time_offset is not None:
        start_server(time_offset)
    else:
        print('Cheating offset must ve an integer')
