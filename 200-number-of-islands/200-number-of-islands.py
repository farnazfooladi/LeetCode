class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0
        
        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            print(q)

            while q:
                row, col = q.pop()
                direction = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in direction:
                    ro, co = row+dr, col+dc
                    print(ro, co)
                    if (ro in range(rows) and co in range(cols) and grid[ro][co] == "1" and (ro,co) not in visit):
                        print("hello")
                        q.append((ro,co))
                        visit.add((ro,co))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island += 1
        
        
        return island
                    