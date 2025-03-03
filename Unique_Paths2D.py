from typing import List

#Tabulation with 1d better for space 
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) 
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = [0]*n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j>0:
                    dp[j] += dp[j-1]
        return dp[-1]

if __name__ == "__main__":
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))


#Memoized Solution good but can be better
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid) 
#         n = len(obstacleGrid[0])
#         if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
#             return 0
#         dp = [[-1] * n for i in range(m)]

#         def paths(i, j):
#             if i == 0 and j == 0:
#                 return 1
#             if i < 0 or j < 0:
#                 return 0
#             if obstacleGrid[i][j] == 1: 
#                 return 0
#             if dp[i][j] != -1:
#                 return dp[i][j]
#             left = paths(i - 1, j)
#             right = paths(i, j - 1)
#             dp[i][j] = left + right
#             return dp[i][j]

#         return paths(m-1,n-1)




#Recurisve Solution also the worst in this case
# def uniquePaths(i, j):
#     if i == 0 and j == 0:
#         return 1
#     if i<0 or j<0:
#         return 0
#     left = uniquePaths(i-1, j)
#     right = uniquePaths(i, j-1)
#     return left + right

# m = 2
# n = 2

# print(uniquePaths(m-1, n-1))
