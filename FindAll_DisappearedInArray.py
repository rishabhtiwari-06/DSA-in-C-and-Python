from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        s= set(nums)
        res = []
        for i in range(1,l+1):
            if i not in s:
                res.append(i)
        return res

        
if __name__ == "__main__":
    nums = [1,1]
    sol = Solution()
    print(sol.findDisappearedNumbers(nums))