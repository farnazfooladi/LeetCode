class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for c in range(numCourses):
            preMap[c] = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        output = []
        visit, cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle: return False
            if crs in visit: return True
            
            cycle.add(crs)
            
            for p in preMap[crs]:
                if dfs(p) == False: return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False: return []
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         test = [0] * numCourses
#         output = []
        
#         prereq = {c:[] for c in range(numCourses)}
#         for crs, pre in prerequisites:
#             prereq[crs].append(pre)
            
#         counter = 0
                
#         for i in prereq:
#             if not prereq[i]:
#                 output.append(i)
#                 test[i] = 1
#                 counter += 1
                
#         size = len(prereq) - counter
                
        
        
#         for t in range(size):
#             for i in prereq:
#                 if test[i] == 1:
#                     continue
#                 x = True
#                 for count in range(len(prereq[i])):
#                     if (test[prereq[i][count]] != 1):
#                         x = False
#                         break
#                 if x:
#                     output.append(i)
#                     test[i] = 1
        
#         if (len(output) == numCourses):
#             return output
            
            
#         return []
            
        