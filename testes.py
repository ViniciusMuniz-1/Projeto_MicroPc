from tkinter import *
from tkinter.filedialog import askopenfilename
janela_padrao = Tk().withdraw()
janela = Tk()

janela.title("Insira aqui o seu título")

texto = Label(janela, text="Insira aqui o seu texto do botão")

texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Insira aqui a ação do seu botão", command=askopenfilename(filetypes = (("Arquivos de texto", "*.txt"), ("Arquivos csv", "*.csv"))))

botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")

texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()