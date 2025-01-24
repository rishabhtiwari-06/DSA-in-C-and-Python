# Substring repeat ho rhi h yani len(s) puri tarah len(sub) se devide hogi
# yani len of substring ke lie hme loop sirf len(s)//2 half tk chalana hoga
#Ab agar subs string hogi to len(s)//2 ko substring ke len se devide krenge to vo bhi puri tarah devide ho jaegi 
#ab kuch ni krna h bs sub string me len(s)//2 se multiply krke s se check kra do if true then good if not then false

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1): 
            print(n // 2 + 1) 
            if n % i == 0:  
                substring = s[:i]  
                if substring * (n // i) == s:  #
                    return True
        
        return False
        # n= len(s)
        # for i in range(1,(n//2)+1):
        #     if n%i == 0:
        #         sub = s[:i]
        #         if sub * (n//2) == s:
        #             return True
        # return False


if __name__ == "__main__":
    s = "ab"
    sol = Solution()
    print(sol.repeatedSubstringPattern(s))