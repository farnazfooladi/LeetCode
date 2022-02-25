class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        time, fresh = 0, 0
        q = deque()
        Rows, Cols = len(grid), len(grid[0])
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        direction = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    row, col = dr+r, dc+c
                    if (row < 0 or row == len(grid) or 
                        col < 0 or col == len(grid[0]) or 
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
                
                