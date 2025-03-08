def maze(arr, m, n):
    dp = [[-1] * n for i in range(m)]
    def check(m,n):
        if m==0 and n ==0:
            return 1
        if m<0 or n<0:
            return 0
        if arr[m][n] == 1:
            return 0
        if dp[m][n] != -1:
            return dp[m][n]
        left = check(m,n-1)
        right = check(m-1,n)
        dp[m][n] = left + right
        return dp[m][n]
    return check(m-1,n-1)


arr = [[0,0,0],[0,1,0],[0,0,0]]
m =3
n = 3
print(maze(arr, m,n))




# def maze(arr, m, n):
#     def check(m,n):
#         if m==0 and n ==0:
#             return 1
#         if m<0 or n<0:
#             return 0
#         if arr[m][n] == 1:
#             return 0
#         left = check(m,n-1)
#         right = check(m-1,n)
#         return left+right
#     return check(m-1,n-1)


# arr = [[0,0,0],[0,1,0],[0,0,0]]
# m =3
# n = 3
# print(maze(arr, m,n))