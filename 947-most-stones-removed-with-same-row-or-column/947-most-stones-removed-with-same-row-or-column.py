class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if len(stones) == 1:
            return 0
    
        rows, cols, components, visited = defaultdict(list), defaultdict(list), 0, set()

        def dfs(r,c):
            visited.add((r,c))

            for new_col in rows[r]:
                if (r, new_col) not in visited:
                    dfs(r, new_col)


            for new_row in cols[c]:
                if (new_row, c) not in visited:
                    dfs(new_row, c)


        for r,c in stones:
            rows[r].append(c)
            cols[c].append(r)


        for r,c in stones:
            if (r,c) in visited:
                continue

            dfs(r,c)

            components += 1

        return len(stones) - components