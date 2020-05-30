import sys


def get_time_offset():
    with open('config.txt', 'r') as config:
        try:
            return int(config.read())
        except ValueError:
            return None


def start_server(time_offset):
    print(time_offset)


if __name__ == '__main__':
    if len(sys.argv) == 2:
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
