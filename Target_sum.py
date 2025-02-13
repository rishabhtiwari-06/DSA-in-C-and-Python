from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} #index nd total
        def backtrack(i, total):
            if i == len(nums):
                return 1 if target == total else 0
            if (i, total) in dp:
                print("Dp[(i, total)] is :", dp[(i, total)])
                return dp[(i, total)]
            dp[(i, total)] = backtrack(i+1, total + nums[i]) + backtrack( i+1, total - nums[i])
            return dp[(i, total)]
        return backtrack(0,0)

if __name__ == "__main__":
    nums = [1,1,1,1,1]
    target = 3
    sol = Solution()
    print(sol.findTargetSumWays(nums, target))