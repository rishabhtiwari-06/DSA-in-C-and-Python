from typing import List 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i]+1 != 10:
                digits[i] += 1
                return digits
            digits[i] = 0
            if i == 0:
                return [1]+digits

             



if __name__ =="__main__":
    digits = [1,2,3]
    sol = Solution()
    print(sol.plusOne(digits))