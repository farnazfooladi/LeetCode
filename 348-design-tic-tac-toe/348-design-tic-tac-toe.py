class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.diag = 0
        self.anti = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        win = self.n   
        
        if player == 1:
            self.rows[row] += 1
            if self.rows[row] == win: return player
            
            self.cols[col] += 1
            if self.cols[col] == win: return player
            
            if col == row:
                self.diag += 1
                if self.diag == win: return player
            
            if col+row == self.n - 1:
                self.anti += 1
                if self.anti == win: return player
            
        if player == 2:
            self.rows[row] -= 1
            if self.rows[row] == -win: return player
            
            self.cols[col] -= 1
            if self.cols[col] == -win: return player
            
            if col == row:
                self.diag -= 1
                if self.diag == -win: return player
            
            if col+row == self.n - 1:
                self.anti -= 1
                if self.anti == -win: return player
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
