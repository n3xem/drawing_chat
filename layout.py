import PySimpleGUI as sg
import server
import threading


def create_server_func():
    server.create_server()


def create_draw_server_func():
    server.create_draw_server()


layout_main = [
    [sg.Submit(button_text='サーバーを作成', key='-CreateServer-')]
]

layout_chatroom = [
    [sg.Text('サーバーを建てました', key='-ConnectWait-')],
    [sg.Output(size=(80, 20), key='-Draw-')]
]


def main_window():

    wait = False
    sg.theme('Topanga')
    window = sg.Window('お絵描きチャット', layout_main)

    thread1 = threading.Thread(target=create_server_func, daemon=True)
    thread2 = threading.Thread(target=create_draw_server_func, daemon=True)
    while True:
        event, values = window.read()
        #print(event, values)
        if event in (None, 'Quit'):
            break

        elif event == '-CreateServer-':
            print('createserver')
            window.close()
            window = sg.Window('チャットルーム', layout_chatroom)
            thread1.start()
            thread2.start()
            wait = True

        elif wait == True:
            wait = False

    window.close()
