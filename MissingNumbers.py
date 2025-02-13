from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = sum(range(len(nums)+1)) - sum(nums)
        return res
            
if __name__ == "__main__":
    nums = [0,3,1]
    sol = Solution()
    print(sol.missingNumber(nums))
            