
import PySimpleGUI as sg

layout = [
    [sg.Text('Output', key = '-OUTPUT-')],
    [sg.Button('Clear'),sg.Button('Enter')],
    [sg.Button(),sg.Button(),sg.Button(),sg.Button()],
    [sg.Button(),sg.Button(),sg.Button(),sg.Button()],
    [sg.Button(),sg.Button(),sg.Button(),sg.Button()],
    [sg.Button(),sg.Button(),sg.Button()]
]

window = sg.Window('Calculator', layout)

while True:
    event, values = window.read()  # type: ignore
    if event == sg.WIN_CLOSED:
        break

window.close()