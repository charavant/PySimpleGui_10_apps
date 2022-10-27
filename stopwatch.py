from tracemalloc import start
import PySimpleGUI as sg 
from time import time

sg.theme('black')
layout = [
    [sg.Push(),sg.Text('X', pad = 0, key='-CLOSE-', enable_events=True)],
    [sg.VPush()],
    [sg.Text('0.0', font='Calibri 40', key = '-TIME-')],
    [sg.Button('Start', button_color=('#FFFFFF','#FF0909'), border_width=0, key= '-STARTSTOP-'), 
     sg.Button('Lap', button_color=('#FFFFFF','#FF0000'),border_width=0, key='-LAP-')
     ],
    [sg.VPush()]
]

window = sg.Window(
    'Stopwatch',
    layout,
    size = (300,300),
    no_titlebar= True,
    element_justification='center'
)
start_time = 0
active = False

while True:
    event, values = window.read(timeout=10)   # type: ignore
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break
    
    if event == '-STARTSTOP-':
        start_time = time()
        active = True
    
    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)  # type: ignore
window.close()


