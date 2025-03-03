
class Solution:
    def NinzaTraining(self,n):
        l = len(n)
        dp = [[-1] * l for _ in range(l)]
        print(dp)
        def Ninza(days , last):
            if days == 0:
                maxi = 0
                for i in range(3):
                    if (i != last):
                        maxi = max(maxi, n[0][i])
                return maxi
            maxi = 0
            if dp[days][last] != -1:
                return dp[days][last]
            for i in range(3):
                if (i!= last):
                    points = n[days][i] + Ninza(days-1, i)
                    maxi = max(points, maxi)
            dp[days][last] = maxi
            return dp[days][last]
        return Ninza(l-1,2)
    
        

if __name__ == "__main__":
    n = [[1,2,5],[3,1,1],[3,3,3]]
    sol = Solution()
    print(sol.NinzaTraining(n))


