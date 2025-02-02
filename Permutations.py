from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                res.append(nums[:])
                return
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]  # Undo swap (backtrack)
        res = []
        backtrack(0,len(nums))
        return res

if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.permute(nums))
        