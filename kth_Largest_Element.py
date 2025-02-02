
                                       #Kth Largest
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stack = []
        for num in nums:
            stack.append(num)
            if len(stack)>k:
                print("Before Remove:",stack)
                stack.remove(min(stack))
                print("After Remove:",stack)
                
        return min(stack)

if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k=2
    sol = Solution()
    print(sol.findKthLargest(nums, k))




                               #Kth Smallest
# from typing import List
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         stack = []
#         for num in nums:
#             stack.append(num)
#             if len(stack)>k:
#                 print("Before Remove:",stack)
#                 stack.remove(max(stack))
#                 print("After Remove:",stack)
                
#         return max(stack)


# if __name__ == "__main__":
#     nums = [3,2,1,5,6,4]
#     k=1
#     sol = Solution()
#     print(sol.findKthLargest(nums, k))



