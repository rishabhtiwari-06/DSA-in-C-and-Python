from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
        
if __name__ == "__main__":
    nums = [1,2,3,4,5,1]
    sol = Solution()
    print(sol.containsDuplicate(nums))
