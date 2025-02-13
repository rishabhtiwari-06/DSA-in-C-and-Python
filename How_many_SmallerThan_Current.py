from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}
        res = []
        for i, val in enumerate(temp):
            if val not in d:
                d[val] = i
        for i in nums:
            res.append(d[i])
        return res

if __name__ == "__main__":
    nums = [8,1,2,2,3]
    sol = Solution( )
    print(sol.smallerNumbersThanCurrent(nums))