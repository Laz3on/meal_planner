import PySimpleGUI as sg


layout = [ 
    [sg.Text('Meal Planner')],
    [sg.Input(), sg.FileBrowse()],
    [sg.Button('Add Meal'), sg.Button('Edit Meal'), sg.Button('Delete Meal'), sg.Button('Display Meal')]
]

window = sg.Window('Window will stay open', layout)

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    print(event, values)


window.Close()

