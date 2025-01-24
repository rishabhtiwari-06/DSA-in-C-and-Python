
from typing import List
class Solution:
    def chcekPrime(self,num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
        
    def Prime(self, l): 
        res = set()
        list = [int(i) for i in str(l)]  #1,1,3,7,3
        for i in range(len(list)):
            num = 0
            for j in range(i,len(list)):
                num = num*10 + list[j]
                if self.chcekPrime(num):
                    res.add(num)
        if res:
            return sorted(res)
        else:
            return ("No Primes ")


if __name__ == "__main__":
    l = 11373
    sol = Solution()
    result = sol.Prime(l)
    if result == "No Primes ":
        print(result)
    else:
        print(" ".join(map(str, result)))
