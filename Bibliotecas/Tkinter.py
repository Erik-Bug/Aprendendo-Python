from tkinter import *

def funcClicar():
    print("Botão clicado")

janelaPrincipal = Tk()
texto = Label(master=janelaPrincipal, text="Minha janela jembles")
texto.pack()

botao = Button(master=janelaPrincipal, text="butão")
botao.pack()

janelaPrincipal.mainloop()
#era para gerar uma pagina nova... mas o github não deixa