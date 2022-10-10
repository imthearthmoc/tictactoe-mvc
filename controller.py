from view import View
from model import Model

class Controller:
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)
        self.view.rodar()
    
    def comando(self, x, y, botao):
        self.model.pressionarBotao(x, y, botao)
        self.model.checagem()
        self.model.fimJogo()

    def novo(self):
        self.model.novoJogo()
        self.view.botoes()
    
    def salvaNome(self, root, nome1, nome2, text1, text2):
        self.model.trocaNomes(root, nome1, nome2, text1, text2)


i = Controller()