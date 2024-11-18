#16
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n == 0 or n == 1:
                return 1
            if n in memo:
                return memo[n]

            total = 0
            for i in range(1, n + 1):  
                left = helper(i - 1)   
                right = helper(n - i)  
                total += left * right  
            memo[n] = total
            return total
        return helper(n)

if __name__ == "__main__":
    solution = Solution()
    test_cases = [1, 2, 3, 4, 5]  
    for n in test_cases:
        print(f"Number of unique BSTs for n = {n}: {solution.numTrees(n)}")
