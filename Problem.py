# Q1) Given an array of integers where every element appears even number of times except one element which appears odd number of times, write a program to find that odd occurring element in O(log n) time. The equal elements must appear in pairs in the array but there cannot be more than two consecutive occurrences of an element. 
from typing import List
class Solution:
    def probFind(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while left< right:
            mid = (left +right)//2  
            if mid%2 == 0:
                if arr[mid] == arr[mid+1]:
                    left = mid+2
                else: 
                    right = mid
            else:
                if arr[mid] == arr[mid-1]:
                    left = mid + 1
                else: 
                    right = mid-1
        return arr[left]


if __name__ =="__main__":
    arr = [2, 2, 3, 1, 1 ]
    sol = Solution()
    print(sol.probFind(arr))