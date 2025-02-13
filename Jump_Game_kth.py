
from typing import List
def GameJump(n: List[int], k) -> int:
    l = len(n)
    dp = [0] * k
    for i in range(1,l):
        min_steps = float('inf')
        for j in range(1,k+1):
            if i-j >= 0:
               jump_diff = dp[(i-j)%k] + abs(n[i]-n[i-j])
               min_steps = min(jump_diff, min_steps)
        dp[i% k] = min_steps
    return dp[(l-1) %k]
        
n = [10, 20, 30, 10, 40, 50, 30]
k = 2
print(GameJump(n, k))
# from typing import List
# def GameJump(n: List[int], k) -> int:
#     l = len(n)
#     dp = [-1] * (l)
#     dp[0]= 0
#     for i in range(1,l):
#         min_steps = float('inf')
#         for j in range(1,k+1):
#             if i-j >= 0:
#                jump_diff = dp[i-j] + abs(n[i]-n[i-j])
#                min_steps = min(jump_diff, min_steps)
#         dp[i] = min_steps
#     print(dp)
#     return dp[l-1]
        
# n = [10, 20, 30, 10, 40, 50, 30]
# k = 2
# print(GameJump(n, k))



#Memoization
# from typing import List
# def GameJump(n: List[int], k) -> int:
#     l = len(n)
#     dp = [-1] * (l)

#     def calculate(i):
#         if i == 0:
#             return 0
#         if dp[i] != -1:
#             return dp[i]
#         min_steps = float("inf")
#         for j in range(1, k + 1):
#             if i - j >= 0:
#                 jump_diff = calculate(i - j) + abs(n[i] - n[i - j])
#                 min_steps = min(jump_diff, min_steps)
#         dp[i] = min_steps
#         return dp[i]

#     return calculate(l - 1)

# n = [10, 20, 30, 10, 40, 50, 30]
# k = 2
# print(GameJump(n, k))


# Recursive Way
# from typing import List
# def GameJump(n: List[int],k):
#     l = len(n)
#     def calculate(i):
#         if i == 0:
#             return 0
#         min_steps = float('inf')
#         for j in range(1,k+1):
#             jumpPower = (calculate(i-j) + abs(n[i]-n[i-j]))
#             min_steps = min(jumpPower, min_steps)
#         return min_steps
#     return calculate(l-1)


# n = [10,20,30,10,40,50,30]
# k=1
# print(GameJump(n,k))
