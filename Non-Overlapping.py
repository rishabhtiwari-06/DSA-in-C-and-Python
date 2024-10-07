from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        count = 0
        intervals.sort(key= lambda x : x[1])
        first = intervals[0][1]
        for i in range(1,len(intervals)):
            if(intervals[i][0]<first):
                count +=1
            else:
                first = intervals[i][1]
        return count

if __name__ == "__main__":
    sol = Solution()
    intervals = [
        [1, 2],
        [2,3],
        [3,4],
        [1,3]
    ]
    print("Count : ",sol.eraseOverlapIntervals(intervals))