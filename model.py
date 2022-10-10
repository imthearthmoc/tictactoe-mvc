class Model:
    def __init__(self, controller):
        #grade do jogo da velha
        self.gradeJogo = [['','',''], ['','',''],['','','']]
        #variavel de define de quem é a vez
        self.vezJogador = 0
        #inicia sem perdedores
        self.jogoPerdedor = False
        #variavel que indica quem venceu
        self.jogoVencedor = ''
        #salva o nome do jogador 1
        self.jogador1 = ''
        #salva o nome do jogador 2
        self.jogador2 = ''
        self.controller = controller
        


    def ganhador(self, ganhador):
        if ganhador == 'X':
            if self.jogador1 == '':
                self.jogador1 = 'Jogador 1'
            self.jogoVencedor = self.jogador1

        else:
            if self.jogador2 == '':
                self.jogador2 = 'Jogador 2'          
            self.jogoVencedor = self.jogador2
        self.jogoPerdedor = True
                

    def novoJogo(self):
        self.vezJogador = 0
        self.gradeJogo = [['','',''], ['','',''],['','','']]
        self.jogoPerdedor = False
        self.jogoVencedor = ''
    
    def checagem(self):
        coluna01 = []
        coluna02 = []
        coluna03 = []
        a = 0

        b = 0
        c = 2
        ldiagonal = []
        ldiagonal2 = []

        for elementos in self.gradeJogo:
            coluna01.append(self.gradeJogo[a][0])
            coluna02.append(self.gradeJogo[a][1])
            coluna03.append(self.gradeJogo[a][2])

            ldiagonal.append(self.gradeJogo[a][b])
            ldiagonal2.append(self.gradeJogo[a][c])
            a += 1
            b += 1
            c -= 1

            contX = 0
            contO = 0

            for i in elementos:
                if i == 'X':
                    contX += 1
                elif i == 'O':
                    contO += 1
            if contX == 3:
                self.ganhador('X') 
                print("Linha")
            elif contO == 3:
                self.ganhador('O')
                print("Linha2")
        
        if (len(set(ldiagonal)) == 1 and ldiagonal[0] != '') or (len(set(ldiagonal2)) == 1 and ldiagonal2[0] != ''):
            if self.gradeJogo[1][1] == 'X':
                self.ganhador('X')
                print("diagonal1")
            else:
                self.ganhador('O')
                print("diagonal1")

        if len(set(coluna01)) == 1 and coluna01[0] != '':
            self.ganhador(coluna01[0])
            print("coluna1")

        elif len(set(coluna02)) == 1 and coluna02[0] != '':
            self.ganhador(coluna02[0])
            print("coluna2")

        elif len(set(coluna03)) == 1 and coluna03[0] != '':
            self.ganhador(coluna03[0])
            print("coluna3")

    def fimJogo(self):
        if self.checagemEmpate() and self.jogoVencedor == '':
            text = 'Empatado'
            self.controller.view.fimPartida(text=text)
        
        elif self.jogoPerdedor:
            print("Jogo Perdedor")
            text = self.jogoVencedor + ' Venceu a Partida'
            self.controller.view.fimPartida(text=text)

    def checagemEmpate(self):
        contador = 0
        for elementos2 in self.gradeJogo:
            for elementos in elementos2:
                if elementos == '':
                    contador += 1
        if contador == 0:
            print("teste")
            self.jogoPerdedor = True
            return True
        else:
            return False
    
    def jogador(self):
        self.vezJogador += 1
        if self.vezJogador % 2 == 1:
            return 'X'
        else:
            return 'O'
    
    def pressionarBotao(self, x, y, botao):
        jogador = self.jogador()
        self.gradeJogo[y][x] = jogador
        self.controller.view.botaoClicado(botao, jogador)

    
    def trocaNomes(self, root, nome1, nome2, text1, text2):
        self.jogador1 = nome1
        self.jogador2 = nome2
        self.controller.view.nomes(root, nome1, nome2, text1, text2)