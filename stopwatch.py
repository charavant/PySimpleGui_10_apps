import PySimpleGUI as sg 

sg.theme('black')
layout = [
    [sg.Push(),sg.Text('X', pad = 0, key='-CLOSE-', enable_events=True)],
    [sg.VPush()],
    [sg.Text('time')],
    [sg.Button('Start'), sg.Button('Lap')],
    [sg.VPush()]
]

window = sg.Window(
    'Stopwatch',
    layout,
    size = (300,300),
    no_titlebar= True,
    element_justification='center'
)

while True:
    event, values = window.read()   # type: ignore
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break
    
    
window.close()


