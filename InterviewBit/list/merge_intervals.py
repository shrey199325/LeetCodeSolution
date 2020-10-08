"""
Merge Intervals
Problem Description

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Problem Constraints
1 <= |intervals| <= 105



Input Format
First argument is the vector of intervals

second argument is the new interval to be merged



Output Format
Return the vector of intervals after merging



Example Input
Input 1:

Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
Input 2:

Given intervals [1, 3], [6, 9] insert and merge [2, 6] .


Example Output
Output 1:

 [ [1, 5], [6, 9] ]
Output 2:

 [ [1, 9] ]


Example Explanation
Explanation 1:

(2,5) does not completely merge the given intervals
Explanation 2:

(2,6) completely merges the given intervals

"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

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
        if i<len(intervals) and (sol[-1].end >= intervals[i].end > intervals[i].start):
            i += 1
        while i<len(intervals):
            sol.append(intervals[i])
            i += 1
        return sol