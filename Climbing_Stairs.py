def waysToClimbStairs(n):
    def count(i):
        if i <=2: return i
        left = count(i-1)
        right = count(i-2)
        return left + right
    return count(n)

n = 5
print(waysToClimbStairs(n))
