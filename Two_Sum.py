from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate (nums):
            if (target- val) in d:
                return [d[target-val], i]
            d[val] = i
        return []
        

if __name__ == "__main__":
    nums = [2,11,7,15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))