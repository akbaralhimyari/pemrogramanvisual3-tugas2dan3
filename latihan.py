import PySimpleGUI as sg
window = sg.Window(title="profile",
                   layout=[[sg.Text("NPM : 2210010613")],
                   [sg.Text("NAMA : JAMILATUZZAHRA")],
                   [sg.Text("Kelas : 5E Regular Banjarmasin")],
                   [sg.Text("Matkul : Pemrograman Visual 3")]],
                   size=(400,200))
window()
window.close()