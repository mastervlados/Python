import keyboard
import time
import os

class Controller():
    # view
    # model
    # playerNumber
    def __init__(self, view, model):
        super().__init__()
        self.view = view
        self.model = model
        self.playerNumber = 1
        self.view.setPlayerNumber(1)
        self.runGame()
    
    def _changePlayer(self):
        if self.playerNumber == 2:
            self.playerNumber = 1
            self.view.setPlayerNumber(1)
        else:
            self.playerNumber = 2
            self.view.setPlayerNumber(2)
    
    def _gameStep(self, i, j):
        if self.model.checkCell(i, j, self.playerNumber):
            if self.model.checkForWinner():
                self.view.isGameOver = True
            else:
                self._changePlayer()

    def runGame(self):
        while True:
            os.system('cls')
            self.view.showGameStatus(self.model.getGameField())
            pressedButton = keyboard.read_key()
            time.sleep(1)
            match pressedButton:
                case "7": # top: ? - -
                    self._gameStep(0, 0)
                case "8": # top: - ? -
                    self._gameStep(0, 1)
                case "9": # top: - - ?
                    self._gameStep(0, 2)
                case "4": # middle: ? - -
                    self._gameStep(1, 0)
                case "5": # middle: - ? -
                    self._gameStep(1, 1)
                case "6": # middle: - - ?
                    self._gameStep(1, 2)
                case "1": # bottom: ? - -
                    self._gameStep(2, 0)
                case "2": # bottom: - ? -
                    self._gameStep(2, 1)
                case "3": # bottom: - - ?
                    self._gameStep(2, 2)
                case _:
                    print("!")
        