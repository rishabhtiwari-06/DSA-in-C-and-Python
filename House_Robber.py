from typing import List


class Solution:
    def Robbery(self, nums: List[int]) -> int:
        l = len(nums)
        if l==1:
            return nums[0]
        if l==0:
            return 0
        prev = nums[0]
        prev1 = 0
        curr = 0
        for i in range(1, l):
            steal = nums[i]
            if i > 1:
                steal += prev1
            notSteal = 0 + prev
            curr = max(steal, notSteal)
            prev1 = prev
            prev = curr
        return curr


n = [1]
sol = Solution()
print(sol.Robbery(n))

