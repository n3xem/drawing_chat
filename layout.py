import PySimpleGUI as sg

sg.theme('Topanga')

layout_main = [
    [sg.Text('接続先'), sg.InputText()],
    [sg.Submit(button_text='サーバーに接続')],
    [sg.Submit(button_text='サーバーを作成')]
]

window = sg.Window('お絵描きチャット', layout_main)

def mainWindow():
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()

