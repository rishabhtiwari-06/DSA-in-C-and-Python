class Solution:
    def Mary(self, n):
        num = n
        sum = 0
        while n>0:
            r = n%10
            sum = sum + r
            n= n//10
        x = num // sum
        return x

if __name__ == "__main__":
    n = 5678
    sol = Solution()
    print(sol.Mary(n))