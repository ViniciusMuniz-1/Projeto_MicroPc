import PySimpleGUI as sg
from tkinter import Button, Tk, font
from tkinter.filedialog import askopenfilename

janela_padrao = Tk().withdraw()


sg.theme('Dark')
layout = [  [sg.Text('Converta Assembly para Hexadecimal aqui:')],
            [sg.Button('Converter',size=(10,5),font = ("Comic Sans", 10)),  sg.Button('Não converter',size=(10,5),font = ("Comic Sans", 10))]]

# Create the Window
window = sg.Window('Conversor', layout,size=(300, 300))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window()
    if event == sg.WIN_CLOSED or event == 'Não converter': # if user closes window or clicks cancel
        break
    caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos de texto", "*.txt"), ("Arquivos csv", "*.csv")))
    break

window.close()