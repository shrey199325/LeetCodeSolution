# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return f"[{self.start}, {self.end}]"

    def __repr__(self):
        return f"[{self.start}, {self.end}]"


class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) <= 1: return intervals
        intervals = self.merge_sort(intervals)
        # print([[i.start, i.end] for i in intervals])
        sol = []
        prev = intervals[0].end
        start = intervals[0].start
        for i in intervals[1:]:
            if prev < i.start:
                sol.append(Interval(start, prev))
                start = i.start
                prev = i.end
            else:
                prev = max(prev, i.end)
        if sol and sol[-1].start != start:
            sol.append(Interval(start, prev))
        elif not sol:
            sol.append(Interval(start, prev))
        return sol

    def merge_sort(self, intervals):
        # import pdb;pdb.set_trace()
        # print([[i.start, i.end] for i in intervals])
        if len(intervals) <= 1:
            return intervals
        l = 0
        h = len(intervals)
        mid = (l + h) // 2
        temp1 = self.merge_sort(intervals[:mid])
        # import pdb; pdb.set_trace()
        temp2 = self.merge_sort(intervals[mid:])
        return self.mer(temp1, temp2)

    def mer(self, a1, a2):
        i, j = 0, 0
        sol = []
        while i < len(a1) and j < len(a2):
            if a1[i].start <= a2[j].start:
                sol.append(a1[i])
                i += 1
            else:
                sol.append(a2[j])
                j += 1
        sol.extend(a1[i:])
        sol.extend(a2[j:])
        print(a1,a2)
        return sol


A = [ (54, 75), (56, 60), (61, 86), (22, 43), (56, 87), (32, 53), (14, 81), (64, 65), (9, 42), (12, 33), (22, 58), (84, 90), (27, 59), (41, 48), (43, 47), (22, 29), (16, 23), (41, 72), (15, 87), (20, 59), (45, 84), (14, 77), (72, 93), (20, 58), (47, 53), (25, 88), (5, 89), (34, 97), (14, 47) ]
for i in range(len(A)):
    A[i] = Interval(A[i][0],A[i][1])
print(Solution().merge(A))