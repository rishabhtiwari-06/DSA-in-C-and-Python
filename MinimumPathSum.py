class Solution:
    def minimumPathSum(self, grid):
        m, n = len(grid), len(grid[0]) 
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j ==0:
                    dp[i][j] = grid[i][j]
                else:
                    left = dp[i][j-1] if j>0 else float('inf')
                    right = dp[i-1][j] if i>0 else float('inf')
                    dp[i][j] =grid[i][j] + min(left, right)
        return dp[m-1][n-1]
        
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
sol = Solution()
print(sol.minimumPathSum(grid)) 



# class Solution:
#     def minimumPathSum(self, grid):
#         m, n = len(grid), len(grid[0]) 
#         dp = [[-1]*n for i in range(m)]
#         def calculate(i, j):
#             if i == 0 and j == 0:
#                 return grid[i][j]
#             if i < 0 or j < 0:
#                 return float('inf')
#             if dp[i][j] != -1:
#                 return dp[i][j]
#             left = grid[i][j] + calculate(i, j - 1)
#             up = grid[i][j] + calculate(i - 1, j)
#             dp[i][j] =min(left, up)
#             return dp[i][j]
#         return calculate(m - 1, n - 1) 
        
# grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# sol = Solution()
# print(sol.minimumPathSum(grid)) 


# class Solution:
#     def minimumPathSum(self, grid):
#         m, n = len(grid), len(grid[0])  
#         def calculate(i, j):
#             if i == 0 and j == 0:
#                 return grid[i][j]
#             if i < 0 or j < 0:
#                 return float('inf')
#             left = grid[i][j] + calculate(i, j - 1)
#             up = grid[i][j] + calculate(i - 1, j)
#             return min(left, up)
#         return calculate(m - 1, n - 1) 

# grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# sol = Solution()
# print(sol.minimumPathSum(grid))  


