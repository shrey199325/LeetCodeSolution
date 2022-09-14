"""
trains: t1, t2, .., tn
timings: [[dt1, dt3], [dt2,dt10],..., [d5,d6]]
total stations (delay)
arr_arr
dep_arr
timings = [[1, 6],[3, 5],[4, 8],[7, 9], [9, 11]]
arr ->
dep ->
"""


def solution(timings):
    arrival_sorted = [a[0] for a in timings].sort()
    departure_sorted = [a[1] for a in timings].sort()
    i = 1
    j = 0
    max_stations = 0
    while i < len(arrival_sorted) and j < len(departure_sorted):
        if arrival_sorted[i] <= departure_sorted[j]:
            max_stations = max(i - j + 1, max_stations)
            i += 1
        else:
            j += 1
    return max_stations