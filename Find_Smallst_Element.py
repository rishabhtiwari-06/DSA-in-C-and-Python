from typing import List
class Solution:
    def smallest_Element(self, arr: List) -> int:
        small = arr[0]
        for i in arr:
            if(small>i):
                small = i
        return small
if __name__ == "__main__":
    arr = [2,3,5,1]
    sol = Solution()
    print(sol.smallest_Element(arr))
