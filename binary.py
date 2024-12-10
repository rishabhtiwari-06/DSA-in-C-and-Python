class Solution:
    def binary(self, n: int, l: list) -> int:
        left = 0
        right = len(l) - 1
        while left <= right:
            mid = (left + right) // 2
            if n == l[mid]:
                return mid
            else:
                if n > l[mid]:
                    left = mid
                else:
                    right = mid
        return -1


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7]
    n = 6
    sol = Solution()
    print(sol.binary(n, l))
