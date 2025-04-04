from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x1,y1 = points.pop()
        res = 0
        while points:
            x2,y2 = points.pop()
            res += max(abs(y2-y1), abs(x2-x1))
            x1,y1 = x2,y2
        return res