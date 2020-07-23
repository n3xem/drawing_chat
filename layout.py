import PySimpleGUI as sg
import server
import threading


def create_server_func():
    server.create_server()


def create_draw_server_func():
    server.create_draw_server()


layout_chatroom = [
    [sg.Text('サーバーを建てました', key='-ConnectWait-')],
    [sg.Output(size=(80, 20), key='-Draw-')]
]


def main_window():
    sg.theme('Topanga')
    window = sg.Window('お絵描きチャット', layout_chatroom)

    thread1 = threading.Thread(target=create_server_func, daemon=True)
    thread2 = threading.Thread(target=create_draw_server_func, daemon=True)
    thread1.start()
    thread2.start()
    while True:
        event, values = window.read()
        #print(event, values)
        if event in (None, 'Quit'):
            break

    window.close()
