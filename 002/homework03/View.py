class View():
    # playerNumber
    # isGameOver
    def __init__(self):
        super().__init__()
        self.isGameOver = False

    def setPlayerNumber(self, number):
        self.playerNumber = number

    def _printGameField(self, cells):
        for i in cells:
            for j in i:
                print(j, end=" ")
            print()  

    def _printPlayerInfo(self):
        print(f"> waiting for Player {self.playerNumber} push a button..")
    
    def _printPlayerWon(self):
        print(f"> Player {self.playerNumber} is won!")

    def showGameStatus(self, cells):
        print("+------------------------+")
        print("|--- Tic Tac Toe Game ---|")
        print("|----- x - Player 1 -----|")
        print("|----- o - Player 2 -----|")
        print("+------------------------+")

        if self.isGameOver:
            self._printPlayerWon()
        else:
            self._printPlayerInfo()
            
        print()
        self._printGameField(cells)
        print()


        


