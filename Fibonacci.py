# def fibonacci(n):
#     if n <= 0:
#         return "Invalid"
#     dp = [-1] * (n+1)
#     def helper(n):
#         if n == 1:
#             return 0
#         elif n == 2:
#             return 1
#         if dp[n] != -1:
#             return dp[n]
#         dp[n] = helper(n-1) + helper(n-2)
#         return dp[n]
#     return helper(n)   
# print(fibonacci(8))

def fibonacci(n):
    dp = [-1] * (n+1)
    prev2 = 0
    prev1 =1
    for i in range(2,n):
        dp[i] = prev2 + prev1 
        prev2 = prev1
        prev1 = dp[i]
    return dp[i]
print(fibonacci(5))
