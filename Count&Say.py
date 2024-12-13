class Solution:
    def countAndSay(self,n):
        if n == 1:
            return "1"
        
        previous_term = self.countAndSay(n - 1)
        result = ""
        y = previous_term[0]
        count = 1
        for i in range(1,len(previous_term)):
            if previous_term[i]==y:
                count+=1
            else:
                result+=str(count)
                result+=str(y)
                y=previous_term[i]
                count=1
        result+=str(count)
        result+=str(y)
        return result

if __name__ == "__main__":
    n = 4
    sol = Solution()
    print(sol.countAndSay(n))
