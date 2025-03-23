from heapq import nlargest
class Solution:
    def solve(self, nums,k):
        index_nums = list(enumerate(nums)) # we get a tuple of element along with its index
        k_largest = nlargest(k,index_nums, key = lambda x: x[1]) #It gives us k large pairs 
        k_largest.sort(key= lambda x: x[0])#this line is for safety nothing much
        return [x[1] for x in k_largest] 


nums = [2,1,3,3]
k = 2
sol = Solution()
print(sol.solve(nums,k))

# nums = [-1, -2, 3, 4]
# k = 3