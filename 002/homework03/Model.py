class Model():
    # gameField
    def __init__(self):
        super().__init__()
        self.gameField = [
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."]
        ]

    def getGameField(self):
        return self.gameField
    
    def checkCell(self, i, j, player):
        if self.gameField[i][j] == ".":
            if player == 1:
                self.gameField[i][j] = "x"
            else:
                self.gameField[i][j] = "o"
            return True
        return False
    
    def checkForWinner(self):
        if self.gameField[0][0] == "x" and self.gameField[0][1] == "x" and self.gameField[0][2] == "x":
            return True
        if self.gameField[0][0] == "o" and self.gameField[0][1] == "o" and self.gameField[0][2] == "o":
            return True
        if self.gameField[1][0] == "x" and self.gameField[1][1] == "x" and self.gameField[1][2] == "x":
            return True
        if self.gameField[1][0] == "o" and self.gameField[1][1] == "o" and self.gameField[1][2] == "o":
            return True    
        if self.gameField[2][0] == "x" and self.gameField[2][1] == "x" and self.gameField[2][2] == "x":
            return True
        if self.gameField[2][0] == "o" and self.gameField[2][1] == "o" and self.gameField[2][2] == "o":
            return True 
        
        if self.gameField[0][0] == "x" and self.gameField[1][1] == "x" and self.gameField[2][2] == "x":
            return True
        if self.gameField[0][0] == "o" and self.gameField[1][1] == "o" and self.gameField[2][2] == "o":
            return True
        if self.gameField[0][1] == "x" and self.gameField[1][1] == "x" and self.gameField[2][1] == "x":
            return True
        if self.gameField[0][1] == "o" and self.gameField[1][1] == "o" and self.gameField[2][1] == "o":
            return True    
        if self.gameField[2][0] == "x" and self.gameField[1][1] == "x" and self.gameField[0][2] == "x":
            return True
        if self.gameField[2][0] == "o" and self.gameField[1][1] == "o" and self.gameField[0][2] == "o":
            return True 
        
        return False