class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        print(preMap)
        
        visit = set()
        
        def dfs(crs):
            if crs in visit:
                return False 
            if preMap[crs] == []:
                return True
            visit.add(crs)
            
            for p in preMap[crs]:
                if not dfs(p):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        