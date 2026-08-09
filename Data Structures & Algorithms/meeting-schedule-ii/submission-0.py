"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        points = []
        for interval in intervals:
            points.append((interval.start,'S'))
            points.append((interval.end,'E'))
        points.sort(key = lambda x: (x[0],x[1]))
        active_intervals = 0
        max_overlaps = 0
        for time, point_type in points:
            if point_type == 'S':
                active_intervals += 1
            else:
                active_intervals -= 1
            max_overlaps = max(max_overlaps,active_intervals)
        return max_overlaps