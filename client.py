import socket
import PySimpleGUI as sg
import threading

layout_chatroom = [
    [sg.Text('サーバーに接続しました', key='-Connect-')],
    [sg.Output(size=(40, 20), key='-Output-'),
        sg.Graph(
            canvas_size=(500, 300),
            graph_top_right=(0, 0),
            graph_bottom_left=(500, 300),
            key="graph",
            change_submits=True,
            background_color='white',
            drag_submits=True
    )

    ],
    [sg.InputText(key='-TextBox-', size=(43, 1)),
     sg.Radio('ペン', 1, key='-Pen-', default=True), sg.Radio('消しゴム', 1, key='-Erase-'), sg.InputText('#000000', key='-Color-'), sg.ColorChooserButton('カラー選択', target='-Color-')],
    [sg.Submit(button_text='送信'), sg.Text('名前'),
     sg.InputText("Anonymous", key='-Name-')]
]


def create_client():
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.connect(('localhost', 50007))
    thread = threading.Thread(target=handler, args=(skt,), daemon=True)
    thread.start()
    skt.sendall(b'connected')
    return skt


def create_draw_client():
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.connect(('localhost', 50008))
    thread = threading.Thread(target=draw_handler, args=(skt,), daemon=True)
    thread.start()
    return skt


def handler(skt):
    while True:
        data = skt.recv(1024)
        print(data.decode('utf-8'))


def draw_handler(skt):
    graph = window.Element('graph')
    while True:
        data = skt.recv(1024)
        xy_list = data.decode('utf-8').split(',')
        xy_tup = (int(xy_list[0]), int(xy_list[1]),
                  int(xy_list[2]), xy_list[3])
        graph.DrawCircle((xy_tup[0], xy_tup[1]), xy_tup[2],
                         fill_color=xy_tup[3], line_color=xy_tup[3])


sg.theme('Topanga')
window = sg.Window('お絵描きチャットクライアント', layout_chatroom)

pen = True
skt = create_client()
draw_skt = create_draw_client()
graph = window.Element('graph')
while True:
    event, values = window.read()
    if event in (None, 'Quit'):
        break
    elif event == '送信':
        skt.sendall((values['-Name-'] + ' : ' +
                     values['-TextBox-']).encode('utf-8'))
        window['-TextBox-'].update('')
    elif event.startswith('graph'):

        if values['-Pen-']:
            graph.DrawCircle(
                values['graph'], 3, fill_color=values['-Color-'], line_color=values['-Color-'])
            draw_skt.sendall(
                (str(values['graph'][0]) + ',' + str(values['graph'][1]) + ',' + str(3) + ',' + values['-Color-']).encode('utf-8'))
        elif values['-Erase-']:
            graph.DrawCircle(values['graph'], 10,
                             fill_color='white', line_color='white')
            draw_skt.sendall(
                (str(values['graph'][0]) + ',' + str(values['graph'][1]) + ',' + str(10) + ',' + 'white').encode('utf-8'))

    elif event == 'ペン':
        pen = True
    elif event == '消しゴム':
        pen = False

window.close()
