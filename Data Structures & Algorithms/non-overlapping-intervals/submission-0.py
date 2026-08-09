class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        A = intervals[0]
        res = 0

        for B in intervals[1:]:
            if A[1] <= B[0]:
                A = B
            else:
                res += 1
                if B[1] < A[1]:
                    A = B
        return res