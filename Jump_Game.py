#Greedy Algorithm to solve jumping questions with constrainsts, avoid backtracking

from typing import List
class Solution:
    def canJump(sol, nums: List[int])-> bool:
        max_reach = 0  
        for i in range(len(nums)):
            if i > max_reach: 
                return False
            max_reach = max(max_reach, i + nums[i])  
        return True

if __name__ == "__main__":
    nums = [3,2,1,0,4]
    sol = Solution()
    print(sol.canJump(nums))