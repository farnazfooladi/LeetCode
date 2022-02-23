class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        n = 3
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        
        player = 1
        
        for row, col in moves:
            
            # Update the row value and column value.
            rows[row] += player
            print(rows[row])
            cols[col] += player
            
            # If this move is placed on diagonal or anti-diagonal, 
            # we shall update the relative value as well.
            if row == col:            
                diag += player
            if row + col == n - 1:
                anti_diag += player
                
            if abs(rows[row]) == n or abs(cols[col])  == n or abs(diag) == n or abs(anti_diag) == n:
                if player == 1:
                    return "A"
                else:
                    return "B"
                
            # # check if this move meets any of the winning conditions.
            # if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
            #     return "A" if player == 1 else "B"
        
            # If no one wins so far, change to the other player alternatively. 
            # That is from 1 to -1, from -1 to 1.
            player *= -1
        
        return "Draw" if len(moves) == n * n else "Pending" 
        