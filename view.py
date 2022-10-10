import tkinter
from tkinter import messagebox
from tkinter.tix import TList

class View(): 
    
    def __init__(self, controller):
         
        self.root = tkinter.Tk() 
        self.root.title('Jogo da Velha')
        self.root.geometry("480x600")
        self.root.resizable(width=0, height=0)
        self.controller = controller

        self.botoes()
        self.cadatrarJogadores()

    def rodar(self):
        self.root.mainloop()

    def cadatrarJogadores(self):
        #TEXTO EM TELA

        #PRIMEIRO JOGADOR
        jogador_um = tkinter.Label(self.root, width=20, text='Jogador 1:')
        jogador_um.place(x=40, y=10)
        #SEGUNDO JOGADOR
        jogador_dois = tkinter.Label(self.root, width=20, text='Jogador 2:')
        jogador_dois.place(x=40, y=40)

        #CAMPO PARA  DE TEXTO 

        #PRIMEIRO JOGADOR
        textoJogador_um = tkinter.Text(self.root, width=20, height= 1)
        textoJogador_um.place(x=165, y=10)
        #SEGUNDO JOGADOR
        textojogador_dois = tkinter.Text(self.root, width=20, height= 1)
        textojogador_dois.place(x=165, y=40)

        btnConfirmaNome = tkinter.Button(self.root, text= 'CONFIRMAR', width=10, height=1, command=lambda: self.controller.salvaNome(self.root, textoJogador_um.get("1.0", 'end-1c'), textojogador_dois.get("1.0", 'end-1c'), textoJogador_um, textojogador_dois ))
        btnConfirmaNome.place(x=190, y=65)

        novo = tkinter.Button(self.root, text= 'Novo Jogo', width=10, height=1, command=lambda:self.controller.novo())
        novo.place(x=350, y=20)

    def botoes(self):
        #BOTOES

        #PRIMEIRO BOTÃO
        btn01 = tkinter.Button(self.root, width=10, height=7, command=lambda:self.controller.comando(0, 0, btn01))
        btn01.place(x= 110, y= 100)

        #SEGUNDO BOTÃO
        btn02 = tkinter.Button(self.root, width=10, height=7, command=lambda:self.controller.comando(1, 0, btn02))
        btn02.place(x= 200, y= 100)

        #TERCEIRO BOTÃO
        btn03 = tkinter.Button(self.root, width=10, height=7, command=lambda:self.controller.comando(2, 0, btn03))
        btn03.place(x= 290, y= 100)

        #QUARTO BOTÃO
        btn04 = tkinter.Button(self.root, width=10, height=7, command=lambda:self.controller.comando(0, 1, btn04))
        btn04.place(x= 110, y= 220)

        #QUINTO BOTÃO
        btn05 = tkinter.Button(self.root, width=10, height=7, command=lambda:self.controller.comando(1, 1, btn05))
        btn05.place(x= 200, y= 220)

        #SEXTO BOTÃO
        btn06 = tkinter.Button(self.root, width=10, height=7, command=lambda:self.controller.comando(2, 1, btn06))
        btn06.place(x= 290, y= 220)

        #SETIMO BOTÃO
        btn07 = tkinter.Button(self.root, width=10, height=7, command=lambda:self.controller.comando(0 , 2, btn07))
        btn07.place(x= 110, y= 340)

        #OITAVO BOTÃO
        btn08 = tkinter.Button(self.root, width=10, height=7, command=lambda:self.controller.comando(1, 2, btn08))
        btn08.place(x= 200, y= 340)

        #NONO BOTÃO
        btn09 = tkinter.Button(self.root, width=10, height=7, command=lambda:self.controller.comando(2, 2, btn09))
        btn09.place(x= 290, y= 340)

    def botaoClicado(self, botao, jogador):
        botao.config(state=tkinter.DISABLED)
        botao.config(text=jogador)
    
    def nomes(self, root, nome1, nome2, text1, text2):
        jogador_1 = tkinter.Label(root, text=nome1, width=23, height=1)
        jogador_1.place(x=165, y=10)
        jogador_2 = tkinter.Label(root, text=nome2, width=23, height=1)
        jogador_2.place(x=165, y=40)
        text1.destroy()
        text2.destroy()

    def fimPartida(self, text):
        tkinter.messagebox.showinfo("Fim da partida", text)