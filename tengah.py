import PySimpleGUI as sg

sg.theme("DarkGrey")
sg.theme_text_color('#fff')
layout = [
    [sg.Text("UNISKA MAAB", font=('helvatica', 25))],
    [sg.Text("UNISKA MAAB", font=('courier', 18))],
]

window = sg.Window(title='Element Text',
                    layout=layout,
                      size=(600, 300),
                        font=('Georgia', 20),
                        element_justification='center'
                        )
window()
window.close()