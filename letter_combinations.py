from itertools import product
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l=[]
        if digits == "":
            return l
        dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"xyz"}
        for digit in digits:
            if digit in dict:
                l.append(dict.get(digit))
        res = [''.join(chars) for chars in product(*l)]
        return res

if __name__ == "__main__":
    digits = ""
    sol = Solution()
    print(sol.letterCombinations(digits))