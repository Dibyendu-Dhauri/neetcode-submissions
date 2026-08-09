class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x[0])

        left,right = 0 , len(intervals) -1
        target = newInterval[0]

        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] >= target:
                right = mid -1
            else:
                left = mid + 1
        intervals.insert(left,newInterval)




        merged = [intervals[0]]

        for B in intervals[1:]:
            A = merged[-1]
            if A[1] < B[0]:
                merged.append(B)
            else:
                merged[-1] = [A[0],max(A[1],B[1])]
        return merged
        