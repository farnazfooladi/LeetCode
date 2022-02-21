class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if (r<0 or r==ROWS or c<0 or c==COLS or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r, c))
            return (1+ dfs(r+1, c) +
                        dfs(r-1, c) +
                        dfs(r, c+1) +
                        dfs(r, c-1))
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not grid:
#             return 0
#         rows, cols = len(grid), len(grid[0])
#         visit = set()
        
        
#         def bfs(r, c):
#             q = collections.deque()
#             visit.add((r,c))
#             q.append((r,c))
#             area = 1

#             while q:
#                 row, col = q.popleft()
#                 direction = [[1,0], [-1,0], [0,1], [0,-1]]
#                 for dr, dc in direction:
#                     ro, co = row+dr, col+dc
#                     if (ro in range(rows) and co in range(cols) and grid[ro][co] == 1 and (ro,co) not in visit):
#                         q.append((ro,co))
#                         visit.add((ro,co))
#                         area += 1
#                         print(area)
#             return area
        
#         maxArea = 0
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1 and (r,c) not in visit:
#                     a = bfs(r,c)
#                     if a > maxArea:
#                         maxArea = a
                        
                    
#         return maxArea
        