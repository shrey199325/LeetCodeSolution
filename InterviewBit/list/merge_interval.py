# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return str((self.start, self.end))

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if newInterval.start > newInterval.end:
            newInterval.start, newInterval.end = newInterval.end, newInterval.start
        start = newInterval.start
        end = newInterval.end
        i = 0
        sol = []
        while i<len(intervals) and (intervals[i].start <= intervals[i].end <= start):
            sol.append(intervals[i])
            i += 1
        temp = Interval()
        if i<len(intervals) and (intervals[i].start <= start <= intervals[i].end):
            temp.start = min(start, intervals[i].start)
        else:
            temp.start = start
        while (i<i+1<len(intervals)) and (intervals[i].end <= end and intervals[i+1].start <= end):
            i += 1
        if i<len(intervals) and (intervals[i].start <= end <= intervals[i].end):
            temp.end = max(end, intervals[i].end)
        else:
            temp.end = end
        sol.append(temp)
        if sol[-1].end >= intervals[i].end > intervals[i].start:
            i += 1
        while i<len(intervals):
            sol.append(intervals[i])
            i += 1
        return sol

q = [ (3, 6), (8, 10) ]
ques = []
for i in q:
    ques.append(Interval(*i))
print(Solution().insert(ques, Interval(*(1,2))))