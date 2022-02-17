class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
           
        if image[sr][sc] != newColor:
            self.fill(image, sr, sc, image[sr][sc], newColor)
        
        return image
        
    def fill(self, image, i, j, oldColor, newColor):
        if 0 <= i <= len(image)-1 and 0 <= j <= len(image[0])-1 and image[i][j] == oldColor:
            image[i][j] = newColor
            self.fill(image, i, j-1, oldColor, newColor)
            self.fill(image, i+1, j, oldColor, newColor)
            self.fill(image, i, j+1, oldColor, newColor)
            self.fill(image, i-1, j, oldColor, newColor)
            
            
            
            
#         startPixel = image[sr][sc]
        
#         self.dfs(image, sr, sc, newColor, startPixel)
        
        
    
#     def dfs(self, image, sr, sc, newColor, startPixel):
#         if (sr < 0 or sc < 0 or sr > len(image) - 1, sc > len(image)-1 or image[sr][sc] == newColor or image[sr][sc] != startPixel):
#             return
#         image[sr][sc] = newColor
        
#         self.dfs(image, sr+1, sc, newColor, startPixel)
#         self.dfs(image, sr-1, sc, newColor, startPixel)
#         self.dfs(image, sr, sc+1, newColor, startPixel)
#         self.dfs(image, sr, sc-1, newColor, startPixel)
        
        
        
        
#         rows = len(image)
#         cols = len(image[0])
#         a = image[sr][sc]
        
#         def dfs(r, c):
#             nonlocal rows, cols, newColor, image
#             if r < 0 or c < 0 or r>rows-1 or c>cols-1 or image[r][c]==newColor or image[r][c]!=a:
#                 return
            
#             image[r][c] = newColor
#             dfs(r+1,c)
#             dfs(r-1,c)
#             dfs(r,c+1)
#             dfs(r,c-1)
        
#         dfs(sr, sc)
#         return image
        