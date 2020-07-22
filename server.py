import socket
import threading

clients = []
draw_clients = []


def create_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
        skt.bind(('localhost', 50007))

        skt.listen(5)
        while True:
            connect, addr = skt.accept()
            clients.append((connect, addr))
            thread = threading.Thread(
                target=handler, args=(connect, addr), daemon=True)
            thread.start()


def create_draw_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
        skt.bind(('localhost', 50008))

        skt.listen(5)
        while True:
            connect, addr = skt.accept()
            draw_clients.append((connect, addr))
            thread = threading.Thread(
                target=draw_handler, args=(connect, addr), daemon=True)
            thread.start()


def close_connect(connect, addr):
    print('切断:', addr)
    connect.close()
    clients.remove((connect, addr))


def close_draw_connect(connect, addr):
    connect.close()
    draw_clients.remove((connect, addr))


def handler(connect, addr):
    with connect:
        while True:
            try:
                data = connect.recv(1024)
            except ConnectionResetError:
                close_connect(connect, addr)
                break

            if not data:
                close_connect(connect, addr)
                break
            print('{} : {}'.format(addr, data.decode('utf-8')))
            for client in clients:
                try:
                    client[0].sendall(
                        (data.decode('utf-8')).encode('utf-8'))
                except ConnectionResetError:
                    break


def draw_handler(connect, addr):
    with connect:
        while True:
            try:
                data = connect.recv(1024)
            except ConnectionResetError:
                close_draw_connect(connect, addr)
                break

            if not data:
                close_draw_connect(connect, addr)
                break
            #print('{} : {}'.format(addr, data.decode('utf-8')))
            for client in draw_clients:
                try:
                    if addr != client[1]:
                        client[0].sendall(
                            (data.decode('utf-8')).encode('utf-8'))
                except ConnectionResetError:
                    break
