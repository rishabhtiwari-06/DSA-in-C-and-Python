
from typing import List
def adjecent(n: List[int]):
    l = len(n)
    prev = n[0]
    prev1 = 0
    curr = 0
    for i in range(1,l):
        take = n[i] 
        if i>1:
            take += prev1
        nontake = 0 + prev
        curr = max(take, nontake)
        prev1 = prev
        prev = curr
    return curr
        

n = [2,1,4,9]
print(adjecent(n))
# from typing import List
# def adjecent(n: List[int]):
#     l = len(n)
#     dp =[-1]*l
#     dp[0]= n[0]
#     for i in range(1,l):
#         take = n[i] 
#         if i>1:
#             take += dp[i-2]
#         nontake = 0 + dp[i-1]
#         dp[i] = max(take, nontake)
#     return dp[i]
        

# n = [2,1,4,9]
# print(adjecent(n))


#Max sum of non adjecent element
# from typing import List
# def adjecent(n: List[int]):
#     l = len(n)
#     dp =[-1]*l
#     def calculate(i):
#         if i <0:
#             return 0
#         if dp[i] != -1:
#             return dp[i]
#         sum_adjcent = calculate(i-2) + n[i]
#         skip = calculate(i-1)

#         dp[i] = max(sum_adjcent, skip)
#         return dp[i]
#     return calculate(l-1)
        

# n = [2,1,4,9]
# print(adjecent(n))